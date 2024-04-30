# CloudWatch Alarms
AWS CloudWatch Alarms is a monitoring tool that helps you create alarms on your AWS Resouces and AWS Services

For example: 

- I want to get email if CPU Utilization of my Webserver greater than 80% for last 10 minutes

- I want to add Instance into Auto Scaling Group if CPU Utilization of my Webserver greater than 80% for last 10 minutes

- I want to remove Instance into Auto Scaling Group if CPU Utilization of my Webserver lower than 20% for last 15 minutes

Threshold = it's numbers for Metrics

Alarm types:

1. OK = When Metrics doesn't lower/greater than Threshold so Alarm doesn't work

2. ALARM = When Metrics lower/greater than Threshold

3. INSUFFICIENT_DATA = When you starting to run Alarm

Settings for Alarm to understand when to switch his State:

1. Period = Time for Metrics to create Datapoint, for example: 60 sec, 100 sec, 300 sec

2. Evaluation Periods = How many Periods to use until CloudWatch switch State, for example: 1, 2, 3

3. Datapoints to Alarm = How many Periods from Evaluation Periods can be greater than Threshold

Example: 

- I want to create Alarm if CPU Utilization of my Webserver greater or equal to 80% for the last 6 minutes from 10 minutes

We create alarm with Period: 2 minutes, Statistic: Average, 80 >= Threshold, Datapoints to alarm: 3 out of 5

In my example let's create 2 Alarms:

- The first Alarm for EC2 Instance, if CPU Utilization of Instance greater or equal to 80% for the last 10 minutes

- The second Alarm for Auto-Scaling group with 2 Instances, if CPU Utilization of Auto-Scaling Group greater or equal to 80% for the last 10 minutes, add Instance, But if CPU Utilization lower than 20% for the last 15 minutes, terminate Instance

To up our CPU Utilization we use tool *stress*

```
# To install stress tool
sudo yum install stress

# To use stress for 100% CPU Utilization
sudo stress --cpu 8 -v
```

## Demonstration

<img src="">

## First Alarm - Instance

At the beggining I created Security group for SSH port 22

<img src="">

After that I run Instance and connect to him and install stress

<img src="">

<img src="">

I went to CloudWatch --> Alarms --> Create Alarms --> EC2 Metric --> Per Instance --> Put the Instance ID --> CPU Utilization


I also choose to get SNS Message to email when I get Alarm types: OK, ALARM

<img src="">

I set Period 5 minutes, 80 >= Threshold, Datapoint Alarm 2 out of 2

<img src="">

I check with command *top* CPU Utilization of Instance and run command stress to up the CPU Utilization

I waited 10 minutes and got email from AWS CloudWatch

<img src="">

Then I stopped stress command in Instance and checked CPU Utilization again

After 2 Datapoints I got email of Alarm type: OK

## Second Alarm - Auto-Scaling Group (Two Alarms)

I already have Security group, So I started with creating Launch Configuration and Auto-Scaling Group, I connected to Instances with SSH and Install stress tool

<img src="">

After that I created two Alarms for Auto-Scaling Group, The first Alarm for ASG: Alarm-HIGH

Create Alarm --> EC2 --> By Auto-Scaling-Group --> CPU Utilization

Period: 5 minutes, 80 >= Threshold, Datapoint Alarm 2 out of 2

The second Alarm for ASG: Alarm-LOW with Period: 5 minutes, 20 <= Threshold, Datapoint Alarm 3 out of 3

<img src="">

After that I need to configure Auto-Scaling Group Policy to make events because of CloudWatch

I went to ASG --> Automating Scaling --> Dynamic Policy --> Step Scaling

And we should create two Policies, the first one when we get a lot of CPU Utilization in Instances so we need to add Instance, and the second one if we don't really use all resources so we can terminate Instance

<img src="">

