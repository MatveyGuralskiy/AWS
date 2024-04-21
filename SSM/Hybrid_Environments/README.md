# System Manager - Hybrid Environments
You can connect not only EC2 Instance (AWS Resources), for Example you can connect to your servers

In my example, I used Virtual Machine on Ubuntu 22.04

To connect On-premises servers (Instances not from AWS) we need to use Activations

Hybrid Environments --> Create Activations

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/AWS-Hybrid-Environments.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Activation-1.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Activation-2.png?raw=true">

## Enter this code to terminal [LINK](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-managed-linux.html)
Now Copy Activation Code and Actiovation ID and go your Server (VM) and replace instead activation-code, activation-id and region

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Process-VM.png?raw=true">

## Check Connection
Go to Service Manager --> Fleet Manager --> Managed nodes

Now you have connection to your Server not from Amazon

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Fleet-Manager-1.png?raw=true">


You could Run bash commands for example:

```
echo "I learn about service 'Service Manager' you can use it for automation like ansible for your Instances" > /YOUR PATH/FILE.txt
cat FILE.txt
uname -a
```

## Results in AWS and VM
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Fleet-Manager-2.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Fleet-Manager-3.png?raw=true">
<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/SSM/Hybrid_Environments/Screens/Result-VM.png?raw=true">

#
