import os
from sebkd_framework.templator import render


class Index:
    def __call__(self, *args, **kwargs):
        return os.environ.get('200_OK'), render('index.html')


class About:
    def __call__(self, *args, **kwargs):
        return os.environ.get('200_OK'), 'about'
