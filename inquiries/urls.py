from django.urls import path
from .import views
# urls patterns

app_name = "inquiries"

urlpatterns = [
    path('inquiries_list', views.inquiries_list, name ='inquiries_list' ),
    path('inquiry_list/<int:pk>/', views.inquiry_list, name ='inquiry_list' ),
    path('categories_list', views.categories_list, name ='categories_list' ),
    path('category_list/s<int:pk>/', views.category_list, name ='category_list' ),
    path('syptoms_list', views.syptoms_list, name ='syptoms_list' ),
    path('syptom_list/s<int:pk>/', views.syptom_list, name ='syptom_list' ),
]