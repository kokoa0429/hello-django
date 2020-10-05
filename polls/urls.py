from django.urls import path

from . import views

urlpatterns = [
    path('<str:question_id>/', views.index, name='index'),
]