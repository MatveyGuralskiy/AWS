# CodeBuild
Fully managed AWS service for automatically compiling source code, running tests, and creating deployment-ready software artifacts

I create CI CodeBuild with SNS Topic (the target buttom doesn't work) and IAM role for everything

Step 1: Create Private registry at ECR service for CodeBuild

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/ECR-1.png?raw=true">

Step 2: Create GitHub repository

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/GitHub.png?raw=true">

Step 3: Create IAM role for CodeBuild with SNS, CloudWatch

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/IAM-Role-CodeBuild.png?raw=true">

Step 4: Create CodeBuild project

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-4.png?raw=true">

Step 5: Run the Build

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-4-Created.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-5-Start.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/CodeBuild-6-Completed.png?raw=true">

Now are ECR repo looks like that

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/ECR-2.png?raw=true">

Step 6: Create SNS (it's doesn't work but Amazon will fix this issue)

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild/Screens/SNS-Notification-BAG.png?raw=true">
