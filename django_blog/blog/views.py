from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, PostForm

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

#___________
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Post
#from .forms import PostForm
# عرض جميع التدوينات
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

# عرض تفاصيل تدوينة
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# إنشاء تدوينة جديدة
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# تعديل تدوينة
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm 
    template_name = 'blog/post_form.html'

    def form_valid(self, form): #form_valid is a built-in method in UpdateView
        form.instance.author = self.request.user #instance.author is the user who created the post
        return super().form_valid(form) 
    #returns a response after the form is valid ,
    # super() calls the parent class's form_valid method 
    # and saves the form with the current user as the author
    #.form_valid(form) is a built-in method that is called when the form is valid
    # it saves the form and redirects to the post detail page because of UpdateView
    #request.user is the user who is currently logged in
    #instance is the current post being edited , user is built-in attribute that represents the 
    # user who is currently logged in and it is in the request object
    #-form_valid() is a built-in method that is called when the form is valid
    # it saves the form and redirects to the post detail page

    def test_func(self): # test_func is a built-in method in UserPassesTestMixin
        post = self.get_object() # get_object() retrieves the current post being edited
        return self.request.user == post.author # this checks if the current user is the author of
        #the post is the user #
        # if the user is not the author, they will not be able to edit the post
#test_func is a built-in method that checks if the user has permission to perform the action
# and it is used in UserPassesTestMixin and returns True if the user has permission
# حذف تدوينة
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author