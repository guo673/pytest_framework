#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os
from api.http_api import http_api
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_admin_url = data.load_ini(data_file_path)["host"]["api_admin_url"]


class bcts_admin(http_api):

    def __init__(self, api_admin_url, **kwargs):
        super(bcts_user, self).__init__(api_admin_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

bcts_user = bcts_admin(api_admin_url)