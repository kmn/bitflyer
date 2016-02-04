import time

def make_nonce():
    '''
    return utc unix time in second

    TODO:
    - return utc unix time in micro second
    '''
    return str(int(time.time()))
