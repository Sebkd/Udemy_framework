# import os
# from sebkd_framework.templator import render
#
#
# class Index:
#     def __call__(self, *args, **kwargs):
#         # return os.environ.get('200_OK'), render('index.html')
#         return '200_OK', render('index.html')
#
#
# class About:
#     def __call__(self, *args, **kwargs):
#         return os.environ.get('200_OK'), 'about'
#--------------------------------------------------------
"""Модуль, содержащий контроллеры веб-приложения"""
from sebkd_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', 'about'
