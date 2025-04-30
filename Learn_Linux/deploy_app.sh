#!/bin/bash

# update packages
echo "UPDATING PACKAGES ======================================================="
apt update
echo "UPGRADING PACKAGES ======================================================"
apt upgrade -y

# install dependencies
echo "INSTALLING DEPENDENCIES ================================================="
apt install nginx -y
systemctl enable nginx
bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
apt install nodejs -y
apt install unzip

# pull app code
echo "GETTING CODE FROM REMOTE ================================================"
wget https://github.com/BothersMcBitey/sparta_test_app/archive/refs/heads/main.zip
unzip main.zip

# install sparta app
echo "INSTALLING APP =========================================================="
cd sparta_test_app-main/app/
npm install

# Run App
echo "STARTING APP ============================================================"
npm start
