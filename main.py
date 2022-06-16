from multiping import MultiPing
import time
import traceback
import sys


def ping_check():
    mp = MultiPing(["8.8.8.8", "youtube.com", "127.0.0.1", "191.1.1.1"])
    try:
        mp.send()
        time.sleep(10)
        responses, no_responses = mp.receive(1)
        for good_respond in responses:
            print("this address pinges successfully ", good_respond)
        if no_responses:
            for bad_respond in no_responses:
                print("Address ", bad_respond, "Wasnt pinged seccuessfully!")
                if no_responses:
                     sys.exit(2)
            ping_check()
    except:
        print("There is an Error")
        sys.exit(3)

    ping_check()


while True:
    try:
        ping_check()
    except:
        print('There is a problem!!!')
        traceback.print_exc()
        sys.exit(3)
        pass