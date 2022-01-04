import time


def hello(event, context):
    time.sleep(4)
    print("second update")
    return "hello-world second"
