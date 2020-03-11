from django.urls import path

from . import views

app_name = 'choropleth'
urlpatterns = [
    path('detail', views.detail, name='detail'),
    path('<str:state>', views.state, name='state'),
    path('<str:state>/<str:animal>', views.choropleth, name='choropleth')
]

