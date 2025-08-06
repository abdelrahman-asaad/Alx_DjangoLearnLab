from django import forms
from .models import Book

class ExampleForm(forms.ModelForm): 
    class Meta:
        model = Book
        fields = ['title', 'author']

    def clean_title(self):
        title = self.cleaned_data.get('title') #to clean field 'title'
        if "<script>" in title:                #to protect from xss if user tried to include javascript <script> code
            raise forms.ValidationError("Invalid title")
        return title

        #تم استخدام clean_title() في الفورم للتحقق من سلامة الحقول مثل عنوان الكتاب ضد XSS: