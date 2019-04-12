from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from .forms import UserForm, LoginForm
from rest_framework.views import APIView
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


# It is a homepage of app
# open in browser
# http://127.0.0.1:8000/
def homepage(request):
    return render(request=request,
                  template_name='home.html')


# It is a about page
# open in browser
# http://127.0.0.1:8000/about/
def about(request):
    return render(request=request,
                  template_name='about.html')


# It will create a user in database
# open in browser
# http://127.0.0.1:8000/signup/
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            User = authenticate(email=email,password=password)
            login(request, User)
            return redirect('OCR_app:home')
    else:
            form = UserForm(request.POST)
    return render(request=request,
                  template_name='signup.html',
                  context={'form': form})


# It will return users from batabase
# http://127.0.0.1:8000/userdetails/
# Return a jason format work in postman
class UserView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})



# It will login the user
# http://127.0.0.1:8000/login/
# work in browser
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
             email = request.POST.get('email')
             password = request.POST.get('password')
             User = authenticate(email=email,password=password)
             login(request, User)
             return redirect('OCR_app:home')
    else:
        form = LoginForm(request.POST)
    return render(request=request,
                  template_name='login.html',
                  context={'form': form})






