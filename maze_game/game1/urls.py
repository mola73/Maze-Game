from django.urls import path
from . import views
from .views import do_voices


urlpatterns= [
  path('do_voices/', views.do_voices, name='do_voices'),
  path('game1/', views.game1, name='game1'),
  path('start/',views.start, name='start')
]