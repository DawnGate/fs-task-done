from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('leads', views.addEmail.as_view()),
    path('list_email', views.getAllSignUpEmail.as_view())
]