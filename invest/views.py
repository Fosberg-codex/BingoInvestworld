from django.shortcuts import render,redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout  
from .models import *  

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth


###register
@unauthenticated_user
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        referral_code = request.POST['referral_code']

        if password==confirm_password:
            if Customer.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif Customer.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = Customer.objects.create_user( username=username,Phone=phone, password=password, 
                                        email=email,Referral_Code = referral_code )
                user.save()
                # username = request.GET['username']
                # group = Group.objects.get(name='customer')
                # user.groups.add(group)
                # #Added username after video because of error returning customer name if not added
                # Customer.objects.create(
				# user=user,
				# name=user.username,
				# )
                
                messages.success(request, 'Account was created for ' + username)
                
                return redirect('login_user')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'accounts/Register.html')


#### Let me finish with this one soon wai

#Login side
@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')



    else:
        return render(request, 'accounts/Login.html')


#login side
 
#logout user
def logout_user(request):
    auth.logout(request)
    return redirect('login_user')
#logout user
 
 
#@login_required(login_url='login_user')
# @allowed_users(allowed_roles=['Customer','Admin'])
def home(request):
        return render(request, 'accounts/index.html')
    
def terms_outside(request):
        return render(request, 'accounts/Terms outside.html')
    
def about(request):
        return render(request, 'accounts/about.html')

@login_required(login_url='login_user')
def dashboard(request):
    #customer = Customer.objects.all()
    # customer = request.user
    # new = customer.Personal_finances.all()
    # print(new)
    #new = request.user.customer.customers_personal_finance_set.all()
    
    context = {}
    
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login_user')
def market(request):
        return render(request, 'accounts/market.html')


@login_required(login_url='login_user')
def depositvip(request):
        return render(request, 'accounts/depositvip.html')

@login_required(login_url='login_user')
def deposit(request):
        return render(request, 'accounts/deposit.html')

@login_required(login_url='login_user')
def tc(request):
        return render(request, 'accounts/T and C.html')

@login_required(login_url='login_user')
def TranH(request,):
    customer = request.user
    naked = customer.Transaction_history.all()
    context = {'naked':naked}
    return render(request, 'accounts/Transaction History.html',context)

@login_required(login_url='login_user')
def withdrawal(request):
        return render(request, 'accounts/withdrawal.html')
# Create your views here.

