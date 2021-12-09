from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, Loan 
from .forms import GameForm, LoanForm
from django.http import Http404


# Create your views here

def index(request):
    # Home page for Board Games
    return render(request, 'bg_app/index.html')

@login_required
def games(request):
    # Show all games
    games = Game.objects.order_by('name')
    context = {'games': games}
    return render(request, 'bg_app/games.html', context)

@login_required
def game(request, game_id):
    # Show a single game and its loan info
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('-date_loaned')
    context = {'game': game, 'loans': loans}
    return render(request, 'bg_app/game.html', context)

@login_required
def new_game(request):
    # Add a new game
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = GameForm()
    else:
        # POST data submitted; process data
        form = GameForm(data=request.POST)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.owner = request.user
            new_game.save()
            return redirect('bg_app:games')
    
    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'bg_app/new_game.html', context)

@login_required
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
            new_loan.loaner = request.user
            new_loan.save()
            return redirect('bg_app:game', game_id=game_id) 

    # Display a blank or invalid form
    context = {'game': game, 'form': form}
    return render(request, 'bg_app/new_loan.html', context)

@login_required
def edit_game(request, game_id):
    # Edit an existing loan 
    game = Game.objects.get(id=game_id)

    # Check if the game belongs to user trying to edit it
    if game.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current info
        form = GameForm(instance=game)

    else:
        # POST data submitted; process data.
        form = GameForm(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bg_app:game', game_id=game_id) 

    context = {'game': game, 'form': form}
    return render(request, 'bg_app/edit_game.html', context)    

@login_required
def edit_loan(request, loan_id):
    # Edit an existing loan 
    loan = Loan.objects.get(id=loan_id)
    game = loan.game

    # Check if loan belongs to user trying to edit it
    if loan.loaner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current info
        form = LoanForm(instance=loan)

    else:
        # POST data submitted; process data.
        form = LoanForm(instance=loan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('bg_app:game', game_id=game.id) 

    context = {'loan': loan, 'game': game, 'form': form}
    return render(request, 'bg_app/edit_loan.html', context)   
















