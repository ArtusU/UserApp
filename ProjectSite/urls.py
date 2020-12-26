
from django.contrib import admin
from django.urls import path, include
from personal.views import home
from account.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('accounts/profile/', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
