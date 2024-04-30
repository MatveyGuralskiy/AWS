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

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Demonstration.png?raw=true">

## Instance Alarm

At the beggining I created Security group for SSH port 22

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Security-group.png?raw=true">

After that I run Instance and connect to him and install stress

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-Instance-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-Instance-2.png?raw=true">

I went to CloudWatch --> Alarms --> Create Alarms --> EC2 Metric --> Per Instance --> Put the Instance ID --> CPU Utilization

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-5.png?raw=true">

I also choose to get SNS Message to email when I get Alarm types: OK, ALARM

I set Period 5 minutes, 80 >= Threshold, Datapoint Alarm 2 out of 2

I check with command *top* CPU Utilization of Instance and run command stress to up the CPU Utilization

I waited 10 minutes and got email from AWS CloudWatch

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-Instance-3-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-Instance-4-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-6-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-7-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SNS-Alarm-Instance-1.png?raw=true">

Then I stopped stress command in Instance and checked CPU Utilization again

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-Instance-5-stop-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Instance-Alarm-8-stop-stress.png?raw=true">

After 2 Datapoints I got email of Alarm type: OK

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SNS-Alarm-Instance-2.png?raw=true">

## Auto-Scaling Group (Two Alarms)

I already have Security group, So I started with creating Launch Template and Auto-Scaling Group, I connected to Instances with SSH and Install stress tool

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/Launch-Template-ASG.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-Instances-1.png?raw=true">

After that I created two Alarms for Auto-Scaling Group, The first Alarm for ASG: Alarm-HIGH

Create Alarm --> EC2 --> By Auto-Scaling-Group --> CPU Utilization

Period: 5 minutes, 80 >= Threshold, Datapoint Alarm 2 out of 2

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-Alarm-1.png?raw=true">

The second Alarm for ASG: Alarm-LOW with Period: 5 minutes, 20 <= Threshold, Datapoint Alarm 3 out of 3

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-Alarm-2.png?raw=true">

After that I need to configure Auto-Scaling Group Policy to make events because of CloudWatch

I went to ASG --> Automating Scaling --> Dynamic Policy --> Step Scaling

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-2-Policy.png?raw=true">

And we should create two Policies, the first one when we get a lot of CPU Utilization in Instances so we need to add Instance, and the second one if we don't really use all resources so we can terminate Instance

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-3-Policy.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-4-Policy.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-5-Policy.png?raw=true">

After that I ran stress tool in Instances of ASG and check Console if we get Alarm and ASG policy add Instance

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-ASG-3-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-ASG-4-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-Alarm-3-stress.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/ASG-Instances-2-stress.png?raw=true">

By the end I stopped stress in Instances of Auto-Scaling Group

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CloudWatch-Alarms/Screens/SSH-ASG-5-stop-stress.png?raw=true">
