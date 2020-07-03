from django.urls import path, include
from . import views

app_name = 'survey'

urlpatterns = [
    path('',views.result,name='result'),
    path('participate/',views.index,name='index'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
