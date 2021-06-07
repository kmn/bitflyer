import requests
import simplejson as json
from urllib.parse import urlencode

"""
document: https://lightning.bitflyer.jp/docs
"""

base_url = "https://api.bitflyer.jp/v1/"
api_urls = { 'getticker'     : '/getticker',
             'getexecutions' : '/getexecutions',
             'getboard'      : '/getboard',
             'gethealth'     : '/gethealth'
             }

class Public(object):
    def __init__(self):
        pass


    def public_api(self,url,**kwargs):
        ''' template function of public api'''
        try :
            url in api_urls
            api_url = base_url + api_urls.get(url)
            if kwargs:
                api_url += '?' + urlencode(kwargs)
            return json.loads(requests.get(api_url).text)
        except Exception as e:
            print(e)
    
    def getticker(self,**kwargs):
        '''Ticker を取得'''
        return self.public_api('getticker',**kwargs)
    
    def getboard(self,**kwargs):
        ''' 板情報を取得 '''
        return self.public_api('getboard',**kwargs)
    
    def getexecutions(self,**kwargs):
        ''' 約定の一覧を取得 '''
        return self.public_api('getexecutions',**kwargs)

    def gethealth(self,**kwargs):
        '''get exchange health'''
        return self.public_api('gethealth',**kwargs)
