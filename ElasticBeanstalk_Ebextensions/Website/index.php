<?
if ($_SERVER['REQUEST_METHOD'] === 'POST')
{
  $file = '/tmp/sample-app.log';
  $message = file_get_contents('php://input');
  file_put_contents($file, date('Y-m-d H:i:s') . " Received message: " . $message . "\n", FILE_APPEND);
}
else
{
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web-Beanstalk</title>
    <style>
         @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap');

        .caveat {
            font-family: "Caveat", cursive;
            font-optical-sizing: auto;
            font-weight: 100;
            font-style: normal;
        }

        body {
            background-color: palevioletred;
            color: white;
            display: grid;
            align-items: center;
            justify-content: center;
        }

        h1 {
        font-size: 80px;
        background-color: dimgrey; 
        }

        p {
            font-size: 40px;
        }
    </style>
</head>
<body>
    <h1>Welcome to Web-Beanstalk Version 1.0</h1>
    <p>This Website created use ebextensions directory for deployment with AWS ElasticBeanstalk</p>
    <p>Matvey Guralskiy</p>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> Web-Beanstalk</p>
    </footer>
</body>
</html>
<? 
} 
?>