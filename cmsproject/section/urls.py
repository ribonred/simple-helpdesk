from django.urls import path
from .views import Homeview, user_login, MessageDetail,Compose,Sentmail
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', Homeview.as_view(), name='panel'),
    path('sent/', Sentmail.as_view(), name='sent'),
    path("compose/", Compose.as_view(), name="buat"),
    path('detail/<slug:slug>', MessageDetail.as_view(), name='detailemail'),
    path('login/', user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
