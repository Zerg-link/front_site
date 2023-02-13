from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils.timezone import datetime
from django.views.generic import ListView
from home import views
from home.forms import *
from home.models import *
# Create your views here.

def Home(request):
    return render(request, "home/Home.html")

def Calculator(request):
    return render(request, "home/Calculator.html", {'range':range(10,21)})

def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
    else:
        form = UserRegisterForm()
    return render(request, 'home/SignUp.html', {'form': form})


def SignIn(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = UserLoginForm()
    return render(request, 'home/SignIn.html', {'form': form})


@login_required
def SignOut(request):
    logout(request)
    return redirect('Home')

@login_required
def NewHouse(request):
    if User.is_superuser:
        if request.method == 'POST':
            form = HouseCreateForm(data=request.POST, files=request.FILES)
            
            if form.is_valid():
                post = form.save(commit=False)
                post.inDate = datetime.now()
                post.save()
                return redirect("Home")
        else:
            form = HouseCreateForm()
        return render(request, 'home/CreateHouse.html', {'form': form})

@login_required
def FollowHome(request):
    if request.method == 'POST':
        form = UserHouseForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("Favourites")
    else:
        form = UserHouseForm()
    return render(request, 'home/Account.html', {'form': form})

@login_required
def Favourites(request):
    House_list = views.UserHousesListView.as_view(
        queryset=UserHouse.objects.filter(user_id=request.user.id),
        context_object_name="House_list",
        template_name="home/Favourites.html",
    )
    return House_list(request)

class  HouseListView(ListView):
    model = House

    def get_context_data(self, **kwargs):
        context = super(HouseListView, self).get_context_data(**kwargs)
        return context

class UserHousesListView(ListView):
    model = UserHouse

    def get_context_data(self, **kwargs):
        context = super(UserHousesListView, self).get_context_data(**kwargs)
        return context