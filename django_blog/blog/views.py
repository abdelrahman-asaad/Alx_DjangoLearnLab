from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm

# 1-تسجيل مستخدم جديد
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/registration/register.html', {'form': form})

#2- صفحة البروفايل
@login_required
def profile(request):
    return render(request, 'blog/registration/profile.html')

# 3-تسجيل دخول باستخدام built-in views
class CustomLoginView(LoginView):
    template_name = 'blog/registration/login.html'

# 4-تسجيل خروج باستخدام built-in views
class CustomLogoutView(LogoutView):
    template_name = 'blog/registration/logout.html'

    #template_name is built-in attribute that specifies the template to render 

