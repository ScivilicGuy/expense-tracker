from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login

def home(request):
  return render(request, 'home.html')

def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    pw = request.POST.get('password')

    # check for valid username
    if not User.objects.filter(username=username).exists():
      messages.error(request, 'Invalid Username')
      return redirect('/home/login/')
    
    # check for valid pw
    user = authenticate(username=username, password=pw)
    if user is None:
      messages.error(request, 'Invalid password')
      return redirect('/home/login/')
    else:
      login(request, user)
      return redirect('/home/')
  
  return render(request, 'login.html')

def register_page(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    pw = request.POST.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
      messages.info(request, 'Username already taken!')
      return redirect('/home/register/')
    
    user = User.objects.create_user(
      first_name=first_name,
      last_name=last_name,
      username=username
    )

    user.set_password(pw)
    user.save()

    messages.info(request, 'Account created successfully!')
    return redirect('/home/login/')
  
  return render(request, 'register.html')

