from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from .forms import MessageForm
from django.contrib import messages
from .models import Message


# Обработка писем от пользователей
def contacts(request):
    if request.method == 'POST':
        messageForm = MessageForm(request.POST)

        if messageForm.is_valid():
            messageForm.save()
            subject = messageForm.cleaned_data['title']
            plain_message = (f'Сообщение от пользователя {messageForm.cleaned_data['name']} ' +
                             f'({messageForm.cleaned_data['email']}): ') + messageForm.cleaned_data['text']
            from_email = f"From {messageForm.cleaned_data['email']}"
            to = settings.EMAIL_HOST_USER
            send_mail(subject, plain_message, from_email, [to])

            messages.success(request, 'Ваше сообщение было отправлено!')
            return redirect('contacts')

    else:
        messageForm = MessageForm()

    data = {
        'messageForm': messageForm,
        'title': 'Связаться с нами',
        'mess': Message.objects.all()
    }

    return render(request, 'contacts/contacts.html', data)


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = '/contacts'

    def test_func(self):
        if self.request.user.is_superuser:
            messages.success(self.request, 'Сообщение удалено')
            return True
        return False
