from solace import *
from motors import *

import time


client = initialize()
while True:
    while client.message_received != True:
        time.sleep(0.01)

    client.message_received = False
    key = client.message_contents
    if key == 'w':
        fwd()
    elif key == 'a':
        left()
    elif key == 's':
        back()
    elif key == 'd':
        right()

