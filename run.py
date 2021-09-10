#!/usr/bin/python
# -*- encoding: utf-8 -*-
import os, time, shutil
import pytest
import allure,rsa

if __name__ == '__main__':
    shutil.rmtree('./allure-results')
    os.system('pytest -s . --alluredir=./allure-results')
    os.system('allure serve ./allure-results')