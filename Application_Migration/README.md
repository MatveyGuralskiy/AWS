# Application Migration Service
AWS Application Migration Service (AWS MGN) is a service provided by Amazon Web Services that simplifies and expedites the migration of applications from on-premises or other cloud environments to AWS. The service automates much of the migration process, reducing the manual work required and minimizing the risk of migration-related issues.

## Key Features:

### Lift-and-Shift Migration:
AWS MGN allows you to perform lift-and-shift migrations, where applications are moved to AWS with minimal changes, ensuring they can run as they do on-premises.

### Continuous Data Replication:
The service continuously replicates data from your source servers to AWS, ensuring minimal downtime during the migration process. This replication is done in real-time, keeping the data in sync.

### Automated Testing:
Before the actual cutover, AWS MGN allows you to test the migrated applications in AWS. This helps ensure that the migration will be successful and that the applications will perform as expected.

### Scalability:
AWS MGN scales to handle migrations of varying sizes, from a few servers to thousands of servers, making it suitable for both small and large-scale migrations.

### Support for Multiple Platforms:
It supports various operating systems and applications, including Windows, Linux, and applications that run on these platforms.

### Post-Migration Optimization: 
After migration, AWS MGN provides tools and recommendations for optimizing the performance and cost-efficiency of your migrated applications within AWS.

## Benefits:
Reduced Downtime: By using continuous data replication, AWS MGN minimizes downtime during the migration process.

Cost-Effective: It automates much of the migration process, reducing the need for manual intervention and lowering costs.

Simplified Process: AWS MGN provides a simplified migration process, allowing organizations to focus on business outcomes rather than the complexities of migration.

High Availability: The service is designed to ensure high availability of applications during and after the migration process.

AWS Application Migration Service is ideal for organizations looking to move their workloads to AWS efficiently and with minimal disruption to their operations.

# Example:
I Migrated 2 Servers to my Account, the first server based on Linux, Ubuntu with Web Server and the second one on Windows Server 2022

I Created 2 Servers on AWS different account so I want to migrate them

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Original-EC2-List.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Original-Webserver.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Connect-RDP-Original-1.png?raw=true">

To connect with RDP enter your Private Key and get decryption of your key

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Connect-RDP-Original-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Connect-RDP-Original-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Original-Windows.png?raw=true">

## Steps:

### Create VPC

Create some VPC with Public Subnets and Internet Gateway

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/VPC.png?raw=true">

### Create IAM User

Create IAM User for Migration and Attach for him policy to get accesses for that

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/IAM-User-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/IAM-User-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/IAM-User-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/IAM-User-4.png?raw=true">

### Set up MGN

Enable the Service first of all

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-1.png?raw=true">

Change Replication Template also

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-3-Replication-Template.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-4-Replication-Template.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-5-Replication-Template.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-6-Replication-Template.png?raw=true">

### Install MGN Agents

To Migrate Servers we should install on them MGN Agents and used AWS IAM Migration User credentials

Click on Add Server

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-MGN-Agent.png?raw=true">

Now use SSH and RDP and Install them

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-Agent-Ubuntu-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-Agent-Ubuntu-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-Agent-Windows-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-Agent-Windows-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Install-Agent-Windows-3.png?raw=true">

Check in Application Migration Service if he sees our Servers

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-7-with-agents.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-8-list.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-9-list.png?raw=true">

Wait until they finished to sync

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-10-Finished-Sync.png?raw=true">

### Create Security Groups

Create 2 security groups for Linux and Windows Server with some ports

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/SG-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/SG-2.png?raw=true">

### Modify Launch Template

Our Migration Service used Launch Template for every Server we want to migrate so we could change some parameters of them like Subnets, Security groups, Keys, Enable Public IP, Tags and more

#### Linux

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-11-Linux.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-12-Linux.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-13-Linux-Edit.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-14-Linux-Edit.png?raw=true">

Now Modify Launch Templates

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Enable-IP.png?raw=true">

Now set default version for this Template

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-6.png?raw=true">

#### Windows

Do the same things for Windows Server

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-15-Windows.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-16-Windows-Edit.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-18-Windows-Edit.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-7.png?raw=true">

### Export and Import with S3 Bucket

If we got many servers we can configure all of them more easily with CSV file

We can Export to S3 our configurations and change them and after Import them

I created S3 Bucket

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/S3-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/S3-2.png?raw=true">

Do Export and Download the file CSV

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Export-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/S3-Export-2.png?raw=true">

Changed some configurations for example: t2.micro --> t2.small

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/CSV-File.png?raw=true">

Upload them to S3 and Import him

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/S3-Export-Updated-CSV.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Import-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Import-2.png?raw=true">

### Launch Testing and other stages

We have different stages to Migrate our Resources:

- Launch test instances = for the first testing of our server
- Ready for cutover = at the end he will launch your server
- Launch cutover instances = he will recreate your server to analize and checked if migration is completed 100% successfully
- Finalize cutover = you get you final server in EC2
- Archive - to disconect from the MGN and used EC2

#### Linux

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-Job-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-Job-4.png?raw=true">

How EC2 testing looks like when you testing

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-EC2-5.png?raw=true">

MGN console

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-List-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-7.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-8.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-9.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Linux-Job-9.png?raw=true">

#### Windows

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Windows-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Launch-Windows-Job.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Windows-8.png?raw=true">

Results

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-Result-1.png?raw=true">

### Disconect from MGN Service

The last step is to disconect from the list of MGN and Archive and after that you can used your EC2 Instances 

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Finalize-Linux-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Finalize-Linux-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/Finalize-Linux-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/AM-Windows-Results-1.png?raw=true">

### Results

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/EC2-Results.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/LC-Linux-Result-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Application_Migration/Screens/SSH-Linux-Result.png?raw=true">
