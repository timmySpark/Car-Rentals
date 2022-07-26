from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from account.forms import *

# Create your views here.

def sign_up_view(request):
    template_name = 'acct/signup.html'
    context={}
    
    if request.POST:
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username,password=raw_password)
            return redirect('login')
        else:
            context = {
                "signupform":form
                }
    else: #GET Request
        form = RegistrationForm()
        context = {"signupform":form}
    return render(request, template_name,context)


def login_view(request):
    template_name = 'acct/login.html'
    form = AccountAuthenticationForm()

    user= request.user
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = AccountAuthenticationForm(request.POST or None)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)

            if user:
                login(request,user)
                return redirect('/')         

    else:
        form = AccountAuthenticationForm()
    context={ "loginform":form }
    return render(request,template_name,context)    


@login_required(login_url='acct/login')
def profile_view(request):
    template_name='acct/profile.html'
    context={}
    return render(request,template_name,context)                        

def logout_view(request):
    logout(request)
    return redirect('/')


def account_view(request):
    template_name='acct/profile.html'
    if not request.user.is_authenticated:
        return redirect('login') 

    context = {}

    if request.POST: 
        form = AccountUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            context['success_message'] = "Updated"  
    else:
        form = AccountUpdateForm(
                initial = {
                    "email":request.user.email,
                    "username":request.user.username,
                }
        )
    context['account_form'] = form
    return render(request,template_name,context)


