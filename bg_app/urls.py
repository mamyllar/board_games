#Defines URL patterns for bg_app.

from django.urls import path
from . import views

app_name = 'bg_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all games
    path('games/', views.games, name='games'),
    #Detail page for a single game
    path('games/<int:game_id>/', views.game, name='game'),
    # Page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
]