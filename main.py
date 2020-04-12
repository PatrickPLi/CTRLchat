from solace import *

import time


client = initialize()
while True:
    while client.message_received != True:
        time.sleep(0.01)

    client.message_received = False
    key = client.message_contents
    print(key)
