"""girlcue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from usersapp import views as user_views
from django.contrib import admin
from django.conf.urls import url


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', include('girlapp.urls')),

    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='usersapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersapp/logout.html'), name='logout'),

    # Password Reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='usersapp/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='usersapp/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='usersapp/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),


    path('update-profile/', user_views.profile_update, name='update-profile'),
    path('user_profile/', user_views.user_profile, name='user-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

