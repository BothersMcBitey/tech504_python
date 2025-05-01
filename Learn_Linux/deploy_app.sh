#!/bin/bash
# built for Ubuntu 2020.04
# Works as of 2025/04/01

read -p "WARNING: THIS SCRIPT USES ROOT ACCESS. Are you sure you want to run it? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

# update packages
echo "UPDATING PACKAGES ======================================================="
sudo apt update
echo "UPGRADING PACKAGES ======================================================"
sudo apt upgrade -y

# install dependencies
echo "INSTALLING DEPENDENCIES ================================================="
sudo apt install nginx -y
sudo systemctl enable nginx
sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
sudo apt install nodejs -y
sudo apt install unzip -y

# pull app code
echo "GETTING CODE FROM REMOTE ================================================"
wget https://github.com/BothersMcBitey/sparta_test_app/archive/refs/heads/main.zip
unzip -q main.zip

# install sparta app
echo "INSTALLING APP =========================================================="
cd sparta_test_app-main/app/
npm install

# Run App
echo "STARTING APP ============================================================"
npm start &> ./sparta_app_log.log &
