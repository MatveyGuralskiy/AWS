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

<img src="">

## Steps:

### Create VPC

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Create IAM User

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Set up MGN

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Install MGN Agents

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Create Security Groups

<img src="">

<img src="">

<img src="">

### Modify Launch Template

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Export and Import with S3 Bucket

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Launch Testing and other stages

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

### Disconect from MGN Service

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">

<img src="">