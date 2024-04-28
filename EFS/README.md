# EFS - Elastic File System
EFS offers benefits for those needing shared storage for Linux machines running in their AWS cloud environment

It's disk for many Instances, automatically increase or decrease, when you add or delete files

Useful when you need Shared files for many Instances, for example Webserver

Disk supports: encryption of data on Rest and In Transit

You need to attach security group with NFS port (2049) Source can be your full CIDR Block VPC (192.168.0.0/16 for example)

To connect we used application: amazon-efs-utils

For auto-connection we need to edit our fstab file

In Bootstraping of EC2 Instance use my script in directory *Script*

I created Security group with NFS and SSH ports Inbound, After that I create EFS disk and 2 Instances

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/Security-group.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/EFS-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/EFS-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/Instances.png?raw=true">

I connected to them with SSH and went to *efs_disk* directory, I create some files and check in other Instance if they sync

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/Instance-SSH-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/EFS/Screens/Instance-SSH-2.png?raw=true">
