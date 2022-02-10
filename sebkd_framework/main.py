import os


class PageNotFound_404:
    def __call__(self, *args, **kwargs):
        return os.environ.get('ERROR_404'), os.environ.get('PAGE_NOT_FOUND_404')


class Sebkdframe:
    """wsgi"""

    def __init__(self, routs_obj):
        self.routs_lst = routs_obj # при иницилизации получаем список урлов


    def __call__(self, _environ, _start_response, *args, **kwargs):
        # Получаем адрес, по которому пользователь выполнил переход
        path = _environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

            # определяем есть ли у нас контроллер для отработки страницы
            if path in self.routs_lst:
               view = self.routs_lst[path]
            else:
                view = PageNotFound_404()

            #Запускаем контроллер
            code, body = view()
            _start_response(code, [('Content-Type', 'text/html')])
            return [body.encode('utf-8')]
