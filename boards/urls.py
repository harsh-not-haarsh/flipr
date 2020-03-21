from .views import CreateBoard, CreateList, CreateCard
from django.conf.urls import url

app_name = 'boards'

urlpatterns = [
    url(r'createBoard', CreateBoard, name='createBoard'),
    url(r'createList', CreateList, name='createList'),
    url(r'createCard', CreateCard, name='createCard'),

]
