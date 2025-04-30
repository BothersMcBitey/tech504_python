#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "deploying in background"
sh ./deploy_app.sh &>> sparta_app_log.log &
echo "done"
