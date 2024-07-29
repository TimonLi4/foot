from typing import Any
from django import forms
from .models import Category, Footballers, Wife
from django.core.validators import MinLengthValidator,MaxLengthValidator

"""@deconstructible
class RussianValidator:
    ALLOWED_CHARS='йцукенгшщзхъэждлорпавыфячсмитьбюЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ0123456789- '
    code = 'russian'

    def __init__(self,message) -> None:
    self.message = message if message else 'Должны присутствовать только русские символы, дефис и пробел'

    def __call__(self,value, *args, **kwds) -> Any:
        if not (set(value)<= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message,code=self.code)"""
        



class AddPostForm(forms.ModelForm):
    cat = forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Категория не выбрана',label='Категория')
    wife = forms.ModelChoiceField(queryset=Wife.objects.all(),required=False,empty_label='не женат',label='Жена')


    class Meta:
        model = Footballers
        fields = ['title','slug','content','photo','is_published','cat','wife','tags']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':50, 'rows':5})
        }
        lables= {'is_published':'Статус'}

class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')
