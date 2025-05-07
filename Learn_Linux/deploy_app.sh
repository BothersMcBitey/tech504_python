#!/bin/bash
# built for Ubuntu 2020.04
# Works as of 2025/05/07

# update packages
echo "UPDATING PACKAGES ======================================================="
sudo apt update
echo "UPGRADING PACKAGES ======================================================"
sudo DEBIAN_FRONTEND=noninteractive apt -yq upgrade

#set env vars
echo "SETTING ENVIROMENT VARIABLES ============================================"
export DB_HOST=mongodb://10.204.0.8:27017/posts

# install dependencies
echo "INSTALLING DEPENDENCIES ================================================="
sudo apt install nginx -y
sudo sed -ri 's~^[^#]\s*try_files.*~proxy_pass "http://127.0.0.1:3000";~' /etc/nginx/sites-available/default
nginx -s reload
sudo systemctl enable nginx

sudo bash -c "curl -fsSL https://deb.nodesource.com/setup_20.x | bash -"
sudo apt install nodejs -y
sudo apt install unzip -y

# pull app code
echo "GETTING CODE FROM REMOTE ================================================"
wget https://github.com/BothersMcBitey/sparta_test_app/archive/refs/heads/main.zip
unzip -qu main.zip
sudo rm main.zip

# install sparta app
echo "INSTALLING APP =========================================================="
cd sparta_test_app-main/app/
npm install

# Install pm2
echo "INSTALLING PM2 =========================================================="
sudo npm install pm2@latest -g

# Run App
echo "STARTING APP ============================================================"
pm2 start app.js --name sparta_app
node seeds/seed.js
