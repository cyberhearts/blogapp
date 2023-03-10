from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostPageView.as_view(), name='postPage'),
]
