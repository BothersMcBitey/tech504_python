#!/bin/bash
# built and tested for Ubuntu 2022.04
# Works as of 2025/04/01

read -p "WARNING: THIS SCRIPT USES ROOT ACCESS. Are you sure you want to run it? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

echo "update linux packages ========================================================"
sudo apt update
sudo DEBIAN_FRONTEND=noninteractive apt -yq upgrade # might be an issue with confirmation dialogue

echo "install dependencies ========================================================="
sudo DEBIAN_FRONTEND=noninteractive apt -yq install gnupg
sudo DEBIAN_FRONTEND=noninteractive apt -yq install curl


echo "install mongodb 7.0.6 ======================================================="
echo "import mongodb public key ======================================================="
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo DEBIAN_FRONTEND=noninteractive gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --yes --dearmor

echo "create the file list ======================================================="
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | sudo DEBIAN_FRONTEND=noninteractive tee /etc/apt/sources.list.d/mongodb-org-7.0.list

echo  "reload package database ======================================================="
sudo DEBIAN_FRONTEND=noninteractive apt-get update

echo "install community server ======================================================="
sudo DEBIAN_FRONTEND=noninteractive apt -yq install \
   mongodb-org=7.0.6 \
   mongodb-org-database=7.0.6 \
   mongodb-org-server=7.0.6 \
   mongodb-mongosh \
   mongodb-org-shell=7.0.6 \
   mongodb-org-mongos=7.0.6 \
   mongodb-org-tools=7.0.6 \
   mongodb-org-database-tools-extra=7.0.6

echo "configure mongodb ============================================================"
echo "change bindIp from 127.0.0.1 (local host) to 0.0.0.0 (everyone)"
sudo sed -ri -E "s/bindIp:.*([0-9]+\.)+[0-9]+/bindIp: 0.0.0.0/"  /etc/mongod.conf

echo "start mongodb ================================================================"
sudo systemctl start mongod

echo "enable mongodb ==============================================================="
sudo systemctl enable mongod