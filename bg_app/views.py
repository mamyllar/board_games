from django.shortcuts import render, redirect

from .models import Game, Loan 
from .forms import GameForm, LoanForm

# Create your views here

def index(request):
    # Home page for Board Games
    return render(request, 'bg_app/index.html')

def games(request):
    # Show all games
    games = Game.objects.order_by('name')
    context = {'games': games}
    return render(request, 'bg_app/games.html', context)

def game(request, game_id):
    # Show a single game and its loan info
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('-date_loaned')
    context = {'game': game, 'loans': loans}
    return render(request, 'bg_app/game.html', context)

def new_game(request):
    # Add a new game
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = GameForm()
    else:
        # POST data submitted; process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bg_app:games')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'bg_app/new_game.html', context)


def new_loan(request, game_id):
    # Add a new loan for a particular game.
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = LoanForm()

    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.game = game
            new_loan.save()
            return redirect('bg_app:game', game_id=game_id) 

    # Display a blank or invalid form
    context = {'game': game, 'form': form}
    return render(request, 'bg_app/new_loan.html', context)

def new_loan(request, game_id):
    # Add a new loan for a particular game.
    game = Game.objects.get(id=game_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = LoanForm()

    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
            new_loan = form.save(commit=False)
            new_loan.game = game
            new_loan.save()
            return redirect('bg_app:game', game_id=game_id) 

    # Display a blank or invalid form
    context = {'game': game, 'form': form}
    return render(request, 'bg_app/new_loan.html', context)    


















