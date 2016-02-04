import requests
import simplejson as json

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


    def public_api(self,url):
        ''' template function of public api'''
        try :
            url in api_urls
            return json.loads(requests.get(base_url + api_urls.get(url)).text)
        except Exception as e:
            print(e)
    
    def getticker(self):
        '''Ticker を取得'''
        return self.public_api('getticker') 
    
    def getboard(self):
        ''' 板情報を取得 '''
        return self.public_api('getboard') 
    
    def getexecutions(self):
        ''' 約定の一覧を取得 '''
        return self.public_api('getexecutions') 

    def gethealth(self):
        '''get exchange health'''
        return self.public_api('gethealth') 
