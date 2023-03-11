from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_registration, name='student_registration'),
    path('detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
