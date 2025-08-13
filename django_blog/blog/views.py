# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post


# 1- تسجيل مستخدم جديد
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


# 2- صفحة البروفايل
@login_required
def profile(request):
    return render(request, 'blog/registration/profile.html')


# 3- تسجيل دخول
class CustomLoginView(LoginView):
    template_name = 'blog/registration/login.html'


# 4- تسجيل خروج
class CustomLogoutView(LogoutView):
    template_name = 'blog/registration/logout.html'


# عرض جميع التدوينات
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


# عرض تفاصيل تدوينة
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


# إنشاء تدوينة جديدة
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'

    def get_form_class(self):
        from .forms import PostForm
        return PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# تعديل تدوينة
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'

    def get_form_class(self):
        from .forms import PostForm
        return PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# حذف تدوينة
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
