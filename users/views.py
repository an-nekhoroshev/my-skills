from django.shortcuts import render, redirect
from .forms import UserOurRegistraion, ProfileImage, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Аккаунт {username} был создан, введите имя пользователя и пароль '
                                      f'для авторизации')

            # Письмо пользователю
            subject = 'Регистрация на сайте MySkills'
            plain_message = f'Регистрация на сайте MySkills. Имя пользователя: {username}; email: {email}; пароль: {password}'
            from_email = settings.EMAIL_HOST_USER
            to = email
            send_mail(subject, plain_message, from_email, [to])
            send_mail(subject, plain_message, from_email, [from_email])

            return redirect('user')
    else:
        form = UserOurRegistraion()
    return render(request, 'users/registraion.html', {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)
