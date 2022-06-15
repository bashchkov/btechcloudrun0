from django.urls import path
from Apps.Web.Website import views

app_name = 'Website'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('about-us/', views.about_page, name='about_page'),
]
