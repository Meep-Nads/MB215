from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index')
]

urlpatterns =[
     path('', views.index, name='index'),
	path('secondURL',views.secondURL, name='secondURL')
]

urlpatterns =[
    path('', views.index, name='index'),
    path('secondURL',views.secondURL, name='secondURL'),
    path('device/<int:device_id>',views.device,name='device')
]

