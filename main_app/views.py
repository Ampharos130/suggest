from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid credentials - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error':error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')

@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {
    'game': game, 
    })

class GameCreate( LoginRequiredMixin, CreateView):
    model = Game
    fields = ('title', 'genre', 'price')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GameUpdate( LoginRequiredMixin ,UpdateView):
  model = Game
  fields = ['genre', 'price']

class GameDelete( LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'