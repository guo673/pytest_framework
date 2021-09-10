#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
from api.http_api import http_api
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_user_url = data.load_ini(data_file_path)["host"]["api_user_url"]


class bcts_user(http_api):

    def __init__(self, api_user_url, **kwargs):
        super(bcts_user, self).__init__(api_user_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/api/login", **kwargs)


bcts_user = bcts_user(api_user_url)
