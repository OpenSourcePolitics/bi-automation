import urllib3


def init():
    global http
    http = urllib3.PoolManager()
