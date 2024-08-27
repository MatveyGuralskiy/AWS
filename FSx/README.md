# FSx
Amazon FSx is a fully managed service that provides highly reliable, scalable, and performant file storage solutions optimized for specific use cases. AWS offers different file systems under the FSx service, each designed to meet varying needs, such as Windows-based environments, high-performance computing, or Linux-based workloads.

Min: 300GB

Max: 16TB

Ports to open:
- SMB 445
- TCP 135
- TCP 55555

Source your VPC

## Types of Amazon FSx:

### Amazon FSx for Windows File Server:

Provides fully managed file storage built on Windows Server, offering native Windows file system features like SMB (Server Message Block) protocol, NTFS, and integration with Active Directory.
Ideal for Windows-based applications that require shared file storage, such as enterprise applications, home directories, and content management systems.
### Amazon FSx for Lustre:

Provides a high-performance, parallel file system optimized for compute-intensive workloads like machine learning, high-performance computing (HPC), media processing, and big data analytics.
Integrates natively with Amazon S3, allowing you to quickly process large datasets stored in S3 and scale throughput up to hundreds of gigabytes per second.
### Amazon FSx for NetApp ONTAP:

Provides the features of NetApp’s ONTAP file system, a popular choice for enterprise-grade storage with features like data deduplication, compression, tiering, and snapshots.
Supports both the NFS and SMB protocols and integrates with existing NetApp environments, making it suitable for organizations using NetApp on-premises or in hybrid environments.
### Amazon FSx for OpenZFS:

Offers a fully managed file system built on the OpenZFS file system, which is known for its reliability, snapshot capabilities, and performance.
Suitable for Linux-based workloads that need advanced data management features, such as software development, web services, or media workflows.
## Key Features Across FSx Services:

### Performance and Scalability:

FSx provides low-latency, high-throughput storage with the ability to scale based on workload requirements.
Ideal for workloads with demanding performance requirements, such as databases, analytics, and high-performance computing.

### Data Management:

FSx includes features like snapshots, data replication, backups, and lifecycle policies, allowing users to manage data efficiently and ensure durability.

### Security and Compliance:

Integrates with AWS Identity and Access Management (IAM), AWS Key Management Service (KMS), and supports encryption at rest and in transit.
Provides options for compliance with standards like GDPR, HIPAA, and SOC.
### Fully Managed:

Amazon FSx is a fully managed service, meaning AWS handles the maintenance, updates, and scaling of the file system, allowing customers to focus on their applications instead of infrastructure.
### Cost Optimization:

Offers flexible pricing models with pay-as-you-go options, enabling cost-effective storage for both small and large workloads.
Includes features like automated tiering and data deduplication to optimize storage costs.

## Use Cases:
Amazon FSx for Windows File Server: Enterprise file shares, Active Directory-integrated applications, content management, and backup/recovery solutions.

Amazon FSx for Lustre: High-performance computing (HPC), machine learning, big data processing, and financial modeling.

Amazon FSx for NetApp ONTAP: Enterprise IT workloads, hybrid cloud storage, disaster recovery, and DevOps environments.

Amazon FSx for OpenZFS: Linux-based applications requiring data consistency, snapshots, and high performance.

Amazon FSx allows organizations to choose the right file system for their specific needs, delivering both performance and simplicity in managing cloud-based file storage.
