# CodeDeploy with CodePipeline
To automate our CodeDeploy Deployment and to not check every time new commit id we can use CodePipeline, he could use last commit id for Deployment

All example from CodeDeploy directory

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodeDeploy_Deployment.png?raw=true">

Let's create Pipeline in CodePipeline

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-2.png?raw=true">

Connect to GitHub account to use Repository

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-3-GitHub.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-4-GitHub.png?raw=true">

The next steps of Configure CodePipeline to connect it to CodeDeploy

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-5.png?raw=true">

Skip the CodeBuild stage

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-6-Skip-Build.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-7.png?raw=true">

And we can see our results in console

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-8.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-9.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-10.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/CodeDeploy_CodePipeline/Screens/CodePipeline-11.png?raw=true">
