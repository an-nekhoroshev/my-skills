from django.urls import path
from . import views as userViews
from django.contrib.auth import views as authViews

urlpatterns = [
    path('reg/', userViews.register, name='reg'),
    path('profile/', userViews.profile, name='profile'),
    path('', authViews.LoginView.as_view(extra_context={'title': 'Страница авторизации'}, template_name='users/user.html'), name='user'),
    path('pass-reset/', authViews.PasswordResetView.as_view(extra_context={'title': 'Восстановление пароля'}, template_name='users/pass_reset.html'), name='pass-reset'),
    path('password_reset_confirm/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(extra_context={'title': 'Восстановление пароля'}, template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', authViews.PasswordResetCompleteView.as_view(extra_context={'title': 'Восстановление пароля'}, template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset/done/', authViews.PasswordResetDoneView.as_view(extra_context={'title': 'Восстановление пароля'}, template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('exit/', authViews.LogoutView.as_view(extra_context={'title': 'Выход из аккаунта'}, template_name='users/exit.html'), name='exit'),
]
