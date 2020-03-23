from .views import CreateBoard, CreateList, CreateCard, Display, DisplayList, ShareBoard, JoinBoard
from django.conf.urls import url


app_name = 'boards'

urlpatterns = [
    url(r'createBoard', CreateBoard, name='createBoard'),
    url(r'(?P<obj_id>\w+)/createList', CreateList, name='createList'),
    url(r'(?P<obj_id>\w+)/createCard', CreateCard, name='createCard'),
    url(r'(?P<obj_id>\w+)/display', Display, name='display'),
    url(r'(?P<obj_id>\w+)/list', DisplayList, name='display_list'),
    url(r'(?P<obj_id>\w+)/shareBoard', ShareBoard, name='share_board'),
    url(r'joinBoard', JoinBoard, name='joinBoard'),


]
