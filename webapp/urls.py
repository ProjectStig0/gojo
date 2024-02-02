from django.urls import path
from .views import delete_brand
from . import views

urlpatterns = [
	path ('', views.home_page, name="homePage"),
	path('dash/', views.dashboard_page, name='dash'),
	path ('about/', views.about_page, name="aboutPage"),
	path ('index/', views.index, name="index"),
	path ('navbar/', views.navbar, name="navbar"),
	path ('footer/', views.footer, name="footer"),
	path ('login/', views.login_page, name="loginPage"),
	path ('brand/', views.brandform_Page, name="brandformPage"),
	path('add_brand/', views.add_brand, name='add_brand'),  # URL for adding a brand
	path('update/<int:brand_id>/', views.update_brand, name='update_brand'),  # URL for editing a brand
	path('delete/<int:brand_id>/', delete_brand, name='delete_brand'),  # URL for deleting a brand
	
]


