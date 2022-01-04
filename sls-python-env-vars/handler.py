import os


def hello(event, context):
    response = os.environ["FIRST_NAME"]

    return response
