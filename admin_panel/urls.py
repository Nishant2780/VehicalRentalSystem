from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "admin_panel"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create_type/', views.create_type, name='create_type'),
    path('brand/', views.addbrand, name='addbrand'),
    
    path('updatebrand/<int:id>', views.updatebrand, name="updatebrand"),
    path('deletebrand/<int:id>', views.deletebrand, name="deletebrand"),


    path('category/', views.category, name='category'),
    path('updatecategory/<int:id>', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:id>', views.deletecategory, name="deletecategory"),




    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)