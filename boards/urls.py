from .views import CreateBoard, CreateList, CreateCard, Display, DisplayList
from django.conf.urls import url

app_name = 'boards'

urlpatterns = [
    url(r'createBoard', CreateBoard, name='createBoard'),
    url(r'createList', CreateList, name='createList'),
    url(r'createCard', CreateCard, name='createCard'),
    url(r'display/(?P<obj_id>\w+)/$', Display, name='display'),
    url(r'display/list/(?P<obj_id>\w+)/$', DisplayList, name='display_list'),

]
