#
from views import Index, About
#
# urlspatterns = {
#     '/': Index(),
#     '/about/': About(),
# }
#------------------------------------------------
from views import Index, About

# Набор привязок: путь-контроллер
routes = {
    '/': Index(),
    '/about/': About(),
}

