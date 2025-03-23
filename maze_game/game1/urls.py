from django.urls import path
from . import views
from .views import do_voices


urlpatterns= [
  path('leaderboard/', views.leaderboard, name='leaderboard'),  # The leaderboard page
  path('save_score/', views.save_score, name='save_score'),
  path('do_voices/', views.do_voices, name='do_voices'),
  path('game1/', views.game1, name='game1'),
  path('start/',views.start, name='start')
]