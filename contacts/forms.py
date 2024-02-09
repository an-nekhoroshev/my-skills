from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(
        label='Ваше имя',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя'})
    )
    email = forms.EmailField(
        label='Ваш Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш Email'})
    )
    title = forms.CharField(
        label='Тема сообщения',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Укажите тему сообщения'})
    )
    text = forms.CharField(
        label='Текст сообщения',
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Напишите ваше сообщение'}),
        help_text='*Заполните все поля формы',
    )

    class Meta:
        model = Message
        fields = ['name', 'email', 'title', 'text']


# class MessageFormAdmin(forms.ModelForm):
#
#     def __init__(self, *args, **kwards):
#         super(MessageFormAdmin, self).__init__(*args, **kwards)
#         self.fields['read'].label = "Текст"
#
#     class Meta:
#         model = Message
#         fields = ['read']
