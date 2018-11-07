from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name="login.html", success_url="/"), name="login"),
    path('register', views.register, name="register"),
    path('logout/', auth_views.LogoutView.as_view(
        next_page="/"), name="logout"),
    # Initial password request
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html", email_template_name="password_reset_email.html", success_url="/accounts/password_reset/done/"), name="password_reset"),
    # When the email has been sent and they have received a link to reset their password.
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name="password_reset_done"),
    # This view is when the password reset was successful
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name="password_reset_complete"),
    # Shows a form for resetting the user's password
    path('password_reset/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html", success_url="/accounts/password_reset/complete/"), name="password_reset_confirm"),

]