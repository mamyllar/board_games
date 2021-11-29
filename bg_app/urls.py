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
    # Page for adding a new loan
    path('new_loan/<int:game_id>/', views.new_loan, name='new_loan'),
    # Page for editing a game
    path('edit_game/<int:game_id>/', views.edit_game, name='edit_game'),
    # Page for editing a loan
    path('edit_loan/<int:loan_id>/', views.edit_loan, name='edit_loan'),
]