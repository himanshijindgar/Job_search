from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.forms import UserCreationForm

def home(request):
  if request.method == 'POST':
      form = UserCreationForm(request.POST)
      return redirect('app_about')
  else:
      form = UserCreationForm()
  return render(request, 'home_app/home.html', {'form': form})
      '''if form.is_valid():
        form.save()
        return redirect('app_about')
  else:
      form = UserCreationForm()
  return render(request, 'home_app/home.html', {'form': form})'''
      #form.save()
      

def about(request):
  context = {
    'posts': Post.objects.all(),
    'title': 'Jobs Available',
  }
  return render(request, 'home_app/about.html', context)
