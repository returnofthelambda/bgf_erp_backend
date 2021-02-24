from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContainerListAPIView.as_view(),
         name="container_list"),
    path('<int:id>/', views.ContainerRetrieveAPIView.as_view(),
         name="container_detail"),
    path('create/', views.ContainerCreateAPIView.as_view(),
         name="container_create"),
    path('update/<int:id>/', views.ContainerRetrieveUpdateAPIView.as_view(),
         name="container_update"),
    path('delete/<int:id>/', views.ContainerDestroyAPIView.as_view(),
         name="container_destroy"),
]
