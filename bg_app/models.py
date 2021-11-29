from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200) #name of the game
    number_of_players = models.CharField(max_length=20) #number of the players 
    year_published = models.IntegerField() #year the game is published

    is_loaned = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True) #automatically save the date when added
    date_modified = models.DateTimeField(auto_now=True) #automatically save the date when modified 


    def __str__(self):
    #return a string representation of the model
        return self.name


class Loan(models.Model):
    #info about the loans
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    loaner = models.TextField()
    comment = models.TextField(max_length=300, blank=True, default='')#loaner may comment their loan
    date_loaned = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        #Return a string representation of the model.
        return self.loaner + " has loaned " + self.game.__str__()
    