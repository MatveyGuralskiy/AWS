import json

def lambda_handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>All in one</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400..700&display=swap');
    
            .caveat {
                font-family: "Caveat", cursive;
                font-optical-sizing: auto;
                font-weight: 100;
                font-style: normal;
            }
    
            body {
                background-color: cornflowerblue;
                color: white;
                display: grid;
                align-items: center;
                justify-content: center;
            }
    
            h1 {
               font-size: 90px;
               background-color: cadetblue; 
            }
    
            p {
                font-size: 45px;
            }
    
            img {
                border-radius: 50%;
                margin-left: 150px;
            }
    
            button {
                margin-left: 350px;
                padding: 20px;
                font-size: 30px;
                cursor: pointer;
            }
    
            button:hover {
                background-color: cadetblue;
            }
        </style>
    </head>
    <body class="caveat">
        <header>
            <h1>All in one Website</h1>
        </header>
        <main>
            <p>
                It's a simple Website used only one file index.html<br>
                Created by Matvey Guralskiy<br>
            </p>
            <img src="https://avatars.githubusercontent.com/u/156613328?v=4" alt="Author photo">
            <p>
                If you like my simple Website, you can check more Websites for you in my profile
            </p>
            <a href="https://github.com/MatveyGuralskiy" target="_blank"><button class="caveat">GitHub</button></a>
        </main>
    </body>
    </html>
    """
    return {
        'statusCode': 200,
        'headers'   : {'Content-type': 'text/html'},
        'body'      : html_content
    }
