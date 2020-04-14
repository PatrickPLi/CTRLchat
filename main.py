from solace import *
from motors import *

import time


client = initialize()
while True:
    while client.message_received != True:
        time.sleep(0.01)

    client.message_received = False
    # print(client.message_contents)
    if client.message_topic == "throttle":
        set_throttle(int(client.message_contents))
    elif client.message_topic == "steering":
        set_steering(int(client.message_contents))
