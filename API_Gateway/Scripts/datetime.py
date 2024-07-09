import datetime

def lambda_handler(event, context):
    datetime_now = datetime.datetime.now()
    israel_datetime = datetime_now + datetime.timedelta(hours=3)
    current_datetime = "Current Date and Time: " + str(israel_datetime.strftime("%d-%m-%Y %H:%M:%S"))

    return current_datetime