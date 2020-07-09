import  requests
class RequestUtil:
    def __init__(self):
        pass

    def request(self,url,method,headers=None,param=None,content_type=None):
        try:
            if method == 'get':
                result = requests.get(url=url,params=param,headers=headers).json()
                return result
            elif method == 'post':
                if content_type == 'application/json':
                    result = requests.post(url=url, params=param, headers=headers).json()
                    return result
                elif:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return  result
            else:
                print("http methon not allowed")
        except Exception as e:
            print("http请求报错：{0}".format(e))
