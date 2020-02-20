import time


def dd(*payloads):

    for payload in list(payloads):
        print(payload)

    quit()


def sleep(seconds):
    time.sleep(seconds)
