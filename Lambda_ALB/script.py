import json

def lambda_handler(event, context):
    default_html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Made with HTML and CSS basic Website">
        <title>Basic Website</title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <body>
        <center><h1>Basic Website</h1></center>
        <img src="https://github.com/MatveyGuralskiy/HTML-CSS-JS/blob/main/HtmlCSS-Websites/Basic_Website/Images/Forest.jpg?raw=true" style="height:750px; width:1000px">
        <p>Welcome to <em>Basic Website</em>!</p>
        <p>Webpage made by</p>
        <p class="username">@MatveyGuralskiy</p>
        <p><strong>I really hope</strong> you enjoy it</p>
    </body>
    </html>
    """

    if "queryStringParameters" in event and event["queryStringParameters"] and "name" in event["queryStringParameters"]:
        name = event["queryStringParameters"]["name"]
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta name="description" content="Made with HTML and CSS basic Website">
            <title>Basic Website</title>
            <link rel="stylesheet" type="text/css" href="style.css">
        </head>
        <body>
            <center><h1>Basic Website</h1></center>
            <img src="https://github.com/MatveyGuralskiy/HTML-CSS-JS/blob/main/HtmlCSS-Websites/Basic_Website/Images/Forest.jpg?raw=true" style="height:750px; width:1000px">
            <p>Welcome to <em>Basic Website {name}</em>!</p>
            <p>Webpage made by</p>
            <p class="username">@MatveyGuralskiy</p>
            <p><strong>I really hope</strong> you enjoy it</p>
        </body>
        </html>
        """
    else:
        html_content = default_html_content
    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': html_content
    }

    return response