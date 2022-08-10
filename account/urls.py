from django.urls import path 
from account.views import *

urlpatterns = [
    path('signup',sign_up_view,name='signup'),
    path('login',login_view,name='login'),
    path('profile',profile_view,name='profile'), 
    path('update',account_view,name='update'),
    path('logout',logout_view,name='logout'),
] 