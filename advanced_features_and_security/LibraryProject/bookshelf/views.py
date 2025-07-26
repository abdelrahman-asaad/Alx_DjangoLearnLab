

# Create your views here.
# bookshelf/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Book


@permission_required('bookshelf.can_view', raise_exception=True) #if true >> access denied 403
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') #book_list is name in urls.py
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})

    
'''# README - Permissions and Groups Setup

- تم تعريف صلاحيات مخصصة على نموذج Book: can_view, can_create, can_edit, can_delete.
- تم إنشاء ثلاث مجموعات:
    - Viewers: صلاحية العرض فقط.
    - Editors: صلاحيات العرض، الإنشاء، التعديل.
    - Admins: كل الصلاحيات.
- تم تأمين الـ views باستخدام @permission_required.
- يمكن إدارة المستخدمين والمجموعات من خلال لوحة تحكم Django Admin.
'''    
#__________________________________security
from .forms import ExampleForm  # تأكد أنك عامل form
from django.views.decorators.csrf import csrf_protect

@csrf_protect  # This is optional, because Django middleware handles it globally 
def create_book_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)  #ExampleForm in forms.py
        if form.is_valid():
            form.save()
            return redirect('book_list') #book_list is name in urls.py
    else:
        form = BookForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form}) #anyway render this html page

'''# form_example.html
<!DOCTYPE html>
<html>
<head>
    <title>Book Form</title>
</head>
<body>
    <h2>Create Book</h2>
    <form method="POST">
        {% csrf_token %}  <!-- Protect against CSRF -->
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>'''    