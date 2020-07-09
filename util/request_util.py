# -*- coding: UTF-8 -*-
import json

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
                if content_type == 'application/json;charset=UTF-8':
                    result = requests.post(url=url, params=param, headers=headers).json()
                    return result

                else:
                    result = requests.post(url=url, data=param, headers=headers).json()
                    return  result
            else:
                print("http methon not allowed")
        except Exception as e:
            print("http请求报错：{0}".format(e))
#if __name__ == '__main__':
#     url = "https://api.xdclass.net/pub/api/v1/web/all_category"
#     u = RequestUtil()
#     result = u.request(url,'get')
#     print(json.dumps(result, ensure_ascii=False, indent=2))
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     print('..............................')
#     data = {"phone": "18801036284",
#             "pwd": "Sp123456!"}
#     url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
#     u = RequestUtil()
#     headers = {"content_type":"application/json"}
#     result = u.request(url,'post',param=data,headers=headers)
#     print(json.dumps(result, ensure_ascii=False, indent=2))
