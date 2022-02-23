from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "accounts"

urlpatterns = [
    path('login/', views.login_page, name='login_page'),

    path('user_signup/', views.user_signup, name='user_signup'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('owner_signup/', views.owner_signup, name='owner_signup'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)