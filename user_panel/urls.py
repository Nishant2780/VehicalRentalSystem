from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "user_panel"

urlpatterns = [
    
    path('home/', views.home, name='home'),

    path('Available_Vehical/', views.Available_Vehical, name='Available_Vehical'),
    path('type_wise_filter_in_userpanel/<int:id>', views.type_wise_filter_in_userpanel, name='type_wise_filter_in_userpanel'),
    
    
    path('Rent_Request/<int:id>/', views.Rent_Request, name='Rent_Request'),







   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)