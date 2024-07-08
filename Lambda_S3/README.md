# Lambda with S3

Before we started to modified our code we should change IAM role permission and attach to the role if S3ReadOnlyAccess for ListBucket function and S3FullAccess for CreateBucket

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/ListBucket-Role.png?raw=true">

Let's start with CreateBucket function, copy the code Deploy it and change Timeout running to 8 seconds, now Test it

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/CreateBucket-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/CreateBucket-2.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/CreateBucket-Output.png?raw=true">

Now create function ListBucket and also modified IAM role for it and Timeout to 4 seconds

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/ListBucket-1.png?raw=true">

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/ListBucket-2.png?raw=true">

This is the result in console S3, we can see our S3 Buckets

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/Buckets.png?raw=true">

And this is our functions

<img src="https://github.com/MatveyGuralskiy/AWS/blob/main/Lambda_S3/Screens/Functions.png?raw=true">
