from django.urls import path
from OCR_app.views import UserView
from . import views


app_name = 'OCR_app'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('userdetails/',UserView.as_view()),

]

