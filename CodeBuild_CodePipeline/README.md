# CodeBuild with CodePipeline

To automate Build Start we can use CodePipeline

We need to modify our IAM role, attach S3FullAccess and CodeStar Connections

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/IAM-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/IAM-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/IAM-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/IAM-4.png?raw=true">

Create CodePipeline and automatically Build will start

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-3.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-4.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-5.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-6.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-7.png?raw=true">

Now to see if it works automatically modify GitHub repository files

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/GitHub-New-Version.png?raw=true">

CodePipeline starting to run

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/CodePipeline-8-New-Version.png?raw=true">

At the final this is our ECR registry

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeBuild_CodePipeline/Screens/ECR.png?raw=true">
