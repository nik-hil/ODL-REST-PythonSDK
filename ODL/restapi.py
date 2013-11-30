import requests
import json
import logging
from requests.auth import HTTPBasicAuth

#TODO: implement logger

class RestAPI():
    """Intialize the variable with default values
        Use this object to use rest api
    """
    def __init__(self, **kwargs):
        '''Pass a dict with following default variables
            o = RestAPI({ipaddress:'1.1.1.1',port:'80'})
        '''
        self.ipaddress = '127.0.0.1'
        self.port = '8080'
        self.username = 'admin'
        self.password = 'admin'
        self.http = 'http'
        if kwargs:
            for k,v in kwargs.iteritems():
                setattr(self, k, v)
    
        self.base_url = self.http + "://" + self.ipaddress + ":" + self.port
        self.auth = HTTPBasicAuth(self.username, self.password)
        
    def get_url(self,rawurl):
        '''converts raw url to url for rest api
        '''
        if not rawurl or not isinstance(rawurl , str):
            return "Error: rawurl is not valid"
        
        return self.base_url + rawurl
        
    def send_reqests(self,action,url,flow=None):
        '''Dyanmically determines the action type. Calls the respective function
            action : get or put or delete or post
            url : complete url to which you want to send request
            flow : dict data to sent along the request. It will be converted in Json format
            >>>send_requests('get','www.example.com')
        '''
        request_type = None
        if isinstance(action, str):
            if action:
                action = action.lower()
                if action in ['get', 'put', 'post', 'delete']:
                    request_type = getattr(requests, action)
        
        if not request_type:
            return 'Error: No action found'
        #FIXME: ADD try catch method along with logger
        if flow:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            data = json.dumps(flow)
            response = request_type(url, data=data, headers=headers, auth=self.auth)
        
        else:
            response = request_type(url, auth=self.auth)
            
        return response
    

    def url_modifier(self,raw_url, url_params):
        '''converts raw_url with dictionary supplied parameters
        '''
        if raw_url:
            url_list = raw_url.split('/')
            for i, ele in enumerate(url_list):
                if '{' in ele:
                    temp = ele.replace('{',"")
                    temp = temp.replace('}',"")
                    try:
                        url_list [i] = url_params[temp]
                        
                    except KeyError:
                        return "Error: " + temp + "  is not present in dictionary"
            
            return "/".join(url_list)
        return ""
        
    def get_result(self,action,raw_url,url_params,flow=None):
        ''' get_result
        '''
        if action and raw_url and url_params:
            url_call = self.url_modifier(raw_url,url_params)
            url = self.get_url(url_call)
            return self.send_reqests(action, url, flow)
        return "Error: one or more parameters were not valid"
    
    
if __name__=='__main__':
    api = RestAPI(ipaddress='192.168.56.101')
    raw_url = '/controller/nb/v2/statistics/{containerName}/flow'
    url_params = {'containerName':'default'}
    action = 'get'
    result = api.get_result(action, raw_url, url_params)
    print result.json()