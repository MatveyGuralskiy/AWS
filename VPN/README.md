# VPN with OpenVPN
A VPN masks your IP address by acting as an intermediary and rerouting your traffic. It also adds encryption, or a tunnel around your identity, as you connect.
The combination of the VPN server and the encryption tunnel blocks your ISP, governments, hackers, and anyone else from spying on you as you navigate the web

I work with AWS and OpenVPN, In AWS I created Security group with Ports: 22, 943, 443, 1194. And Run EC2 Instance in Ubuntu 22.04 LTS this server called VPN Server

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/Security-group.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-Server.png?raw=true">

After That I went to Access Server Portal of OpenVPN [Access Server Portal](https://as-portal.openvpn.com/quick-start) 

Get access server --> Linux Software Package --> Ubuntu LTS --> Copy strings to VPN Server

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/Install-VPN-Server.png?raw=true">

```
apt update && apt -y install ca-certificates wget net-tools gnupg

wget https://as-repository.openvpn.net/as-repo-public.asc -qO /etc/apt/trusted.gpg.d/as-repository.asc

echo "deb [arch=amd64 signed-by=/etc/apt/trusted.gpg.d/as-repository.asc] http://as-repository.openvpn.net/as/debian jammy main">/etc/apt/sources.list.d/openvpn-as-repo.list

apt update && apt -y install openvpn-as
```

Connect to your Instance with SSH port and paste those commands

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/SSH-Connection-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/SSH-Connection-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/SSH-Connection-3.png?raw=true">

Now copy the password you get from the terminal and go to your Public IP of Instance in browser

Enter the login: *openvpn* and password you get in the console

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-3.png?raw=true">

In User Management add password for openvpn user and create a new user with admin permissions

After that goes to VPN Settings and Network Settings

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-4.png?raw=true">

I went to new profile and Installed VPN Client on my PC

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-7.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-8.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-9.png?raw=true">

I turned on VPN and checked my IP Address

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/VPN/Screens/VPN-10.png?raw=true">
