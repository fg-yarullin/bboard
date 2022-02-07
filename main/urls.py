from atexit import register
from django.urls import path, reverse_lazy
from .views import index, other_page, profile, user_activate, password_reset_request
from .views import BBLoginView, BBLogoutView
from .views import ChangeUserInfoView, BBPasswordChangeView
from .views import RegisterUserView, RegisterDoneView, DeleteUserView
from django.contrib.auth import views as auth_views
from .views import by_rubric, detail, profile_bb_detail

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register', RegisterUserView.as_view(), name='register'),
    path('accounts/profile/delete', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/<int:pk>', profile_bb_detail, name='profile_bb_detail'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/change', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password/reset', password_reset_request, name='password_reset'),
    path('<int:rubric_pk>/<int:pk>', detail, name='detail'),
    path('<int:pk>/', by_rubric, name='by_rubric'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('accounts/password/main/password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password/main/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_confirm.html", success_url=reverse_lazy('main:password_reset_complete')), name='password_reset_confirm'),
    path('accounts/password/main/reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
]
