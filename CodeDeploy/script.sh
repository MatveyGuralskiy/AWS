#!/bin/bash
apt-get update

# Install Apache
apt-get install -y apache2

# Enable and start Apache
systemctl enable apache2
systemctl start apache2

# Install Ruby and wget
apt-get install -y ruby wget

# Download the CodeDeploy agent installer
cd /home/ubuntu
wget https://aws-codedeploy-us-west-2.s3.us-west-2.amazonaws.com/latest/install

# Make the installer executable
chmod +x ./install

# Install the CodeDeploy agent
sudo ./install auto

# Start the CodeDeploy agent
sudo systemctl start codedeploy-agent

# Enable the CodeDeploy agent to start at boot
sudo systemctl enable codedeploy-agent