from django import forms

from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'number_of_players', 'year_published']
        labels = {'name': 'Name', 'number_of_players': 'Number of players', 'year_published': 'Year published'}


class LoanForm(forms.ModelForm):
    class Meta:
            model = Loan
            fields = ['comment']
            labels = {'comment': 'Comment'}