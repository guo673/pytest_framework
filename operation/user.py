#!/usr/bin/python
# -*- encoding: utf-8 -*-

from api.bcts_user import bcts_user
from api.http_api import ResultBase
from common.logger import logger


headers = {"SIGN" : "W1dmZcIoEygoUGW7H1BPP2BHP070MPNNmElpFb0lAiMd6GU67f3Adf14CahjiTsAFz14ZX/pGML17LC1Erkb42NP56Byfe8WF"
                    "7MKznUu6N4hFYL9/vp4p/fSLnW8sxyXRlr2bgRZxIk+MXEQAIhWyfQMEJe5OSdOrcEUm/ulbdjBlxF/+v48FsibZP1GqaE/u38"
                    "Zj9P5P7HEsgm03ZbksYgEriFs1SF4bt6MD7ah31BdemBzhWGUL+EcKVqcXLUlILnZ1vi9hnS6XaMtOVVOse9wOxdmDlW6oSXq4"
                    "dnYmTqOzItJQEoAVKC9yyUnfsQ463V9Z65pkzdJbvXDBQdzZQ=="}

def login_user(username, password):
    '''获取登录信息'''
    result = ResultBase()
    login_params = {
        'area_code' : "+86" ,
        'device_id' : '' ,
        'login_password' : password ,
        'two_factor_code' : 12 ,
        'type' : 1 ,
        'user_name' : username ,
        'verification_code' : "123456"
    }
    res = bcts_user.login(headers=headers,json=login_params)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
        result.token = res.json()["data"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
