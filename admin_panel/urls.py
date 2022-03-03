from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = "admin_panel"

urlpatterns = [
    path('home/', views.home, name='home'),

    path('create_type/', views.create_type, name='create_type'),
    path('updatetype/<int:id>', views.updatetype, name="updatetype"),
    path('deletetype/<int:id>', views.deletetype, name="deletetype"),

    path('brand/', views.addbrand, name='addbrand'),    
    path('updatebrand/<int:id>', views.updatebrand, name="updatebrand"),
    path('deletebrand/<int:id>', views.deletebrand, name="deletebrand"),


    path('category/', views.category, name='category'),
    path('updatecategory/<int:id>', views.updatecategory, name="updatecategory"),
    path('deletecategory/<int:id>', views.deletecategory, name="deletecategory"),

    path('Vehical_Variant/', views.Vehical_Variant, name='Vehical_Variant'),
    path('Add_Vehical_Variant/', views.Add_Vehical_Variant, name='Add_Vehical_Variant'),
    path('updatevariant/<int:id>', views.updatevariant, name="updatevariant"),
    path('deletevariant/<int:id>', views.deletevariant, name="deletevariant"),

    path('vehical_Registration/', views.vehical_Registration, name='vehical_Registration'),
    path('Register_Vehical_List/', views.Register_Vehical_List, name='Register_Vehical_List'),
    path('update_Register_Vehical/<int:id>', views.update_Register_Vehical, name="update_Register_Vehical"),
    path('delete_Register_Vehical/<int:id>', views.delete_Register_Vehical, name="delete_Register_Vehical"),

    path('Users/', views.Users, name='Users'),

    path('owner_rq_List/', views.owner_rq_List, name='owner_rq_List'),
    path('Rent_Rq_List_admin/', views.Rent_Rq_List_admin, name='Rent_Rq_List_admin'),



   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)