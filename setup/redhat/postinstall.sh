#!/bin/sh

set -e

actpy_CONFIGURATION_DIR=/etc/actpy
actpy_CONFIGURATION_FILE=$actpy_CONFIGURATION_DIR/actpy.conf
actpy_DATA_DIR=/var/lib/actpy
actpy_GROUP="actpy"
actpy_LOG_DIR=/var/log/actpy
actpy_LOG_FILE=$actpy_LOG_DIR/actpy-server.log
actpy_USER="actpy"

if ! getent passwd | grep -q "^actpy:"; then
    groupadd $actpy_GROUP
    adduser --system --no-create-home $actpy_USER -g $actpy_GROUP
fi
# Register "$actpy_USER" as a postgres user with "Create DB" role attribute
su - postgres -c "createuser -d -R -S $actpy_USER" 2> /dev/null || true
# Configuration file
mkdir -p $actpy_CONFIGURATION_DIR
# can't copy debian config-file as addons_path is not the same
if [ ! -f $actpy_CONFIGURATION_FILE ]
then
    echo "[options]
; This is the password that allows database operations:
; admin_passwd = admin
db_host = False
db_port = False
db_user = $actpy_USER
db_password = False
addons_path = /usr/lib/python3.6/site-packages/actpy/addons
" > $actpy_CONFIGURATION_FILE
    chown $actpy_USER:$actpy_GROUP $actpy_CONFIGURATION_FILE
    chmod 0640 $actpy_CONFIGURATION_FILE
fi
# Log
mkdir -p $actpy_LOG_DIR
chown $actpy_USER:$actpy_GROUP $actpy_LOG_DIR
chmod 0750 $actpy_LOG_DIR
# Data dir
mkdir -p $actpy_DATA_DIR
chown $actpy_USER:$actpy_GROUP $actpy_DATA_DIR

INIT_FILE=/lib/systemd/system/actpy.service
touch $INIT_FILE
chmod 0700 $INIT_FILE
cat << EOF > $INIT_FILE
[Unit]
Description=actpy Open Source ERP and CRM
After=network.target

[Service]
Type=simple
User=actpy
Group=actpy
ExecStart=/usr/bin/actpy --config $actpy_CONFIGURATION_FILE --logfile $actpy_LOG_FILE
KillMode=mixed

[Install]
WantedBy=multi-user.target
EOF
