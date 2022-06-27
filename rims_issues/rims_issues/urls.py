from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from rims_form.views import SignupView, UnauthorizedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rims_form.urls', namespace='rims_form')),
    path('login/', LoginView.as_view(), name='login'),
    path('unauthorized/', UnauthorizedView.as_view(), name='unauthorized'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
