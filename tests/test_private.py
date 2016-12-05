import sys,os
from nose.tools import *
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(current_dir, '../bitflyer'))
from bitflyer.private import Private

import settings
import time

def test_getbalance():
    '''
    test bitflyer.private.getbalance()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(isinstance(p1.getbalance().get('response'),list))

def test_getcollateral():
    '''
    test bitflyer.private.getcollateral()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(isinstance(p1.getcollateral().get('response'),dict))

def test_sendchildorder():
    '''
    test bitflyer.private.sendchildorder()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    result = p1.sendchildorder(product_code='BTC_JPY',size=0.01,child_order_type='LIMIT',side='BUY', price=200000)
    ok_(isinstance(result.get('response'),dict))
    ok_(isinstance(result.get('response').get('child_order_acceptance_id'), str))
    return result.get('response').get('child_order_acceptance_id')

def test_sendparentorder():
    '''
    test bitflyer.private.sendparent()
    '''
    ...

def test_cancelchildorder():
    '''
    test bitflyer.private.cancelchildorder()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    result = p1.sendchildorder(product_code='BTC_JPY',size=0.1,child_order_type='LIMIT',side='BUY', price=30000)

    time.sleep(1)
    p2 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    result2 = p2.cancelchildorder(product_code='BTC_JPY',child_order_acceptance_id=result.get('response').get('child_order_acceptance_id'))
    eq_(result2.get('status_code'),200)

def test_cancelparentorder():
    '''
    test bitflyer.private.cancelparentorder()
    '''
    ...

def test_cancelallchildorders():
    '''
    test bitflyer.private.cancelallchildorders()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    result1 = p1.cancelallchildorders(product_code='BTC_JPY')
    eq_(result1.get('status_code'),200)

def test_getchildorders():
    '''
    test bitflyer.private.getchildorders()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(isinstance(p1.getchildorders().get('response'),list))

def test_getparentorders():
    '''
    test bitflyer.private.getparentorders()
    '''
    ...

def test_getparentorder():
    '''
    test bitflyer.private.getparentorder()
    '''
    ...

def test_getexecutions():
    '''
    test bitflyer.private.getexecutions()
    '''
    time.sleep(2)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(isinstance(p1.getexecutions().get('response'),list))

def test_getpositions():
    '''
    test bitflyer.private.getpositions()
    '''
    time.sleep(1)
    p1 = Private(access_key=settings.access_key, secret_key=settings.secret_key)
    ok_(isinstance(p1.getpositions().get('response'),dict))
