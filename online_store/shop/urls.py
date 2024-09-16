from tkinter.font import names

from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('user/', UserProfileViewSet.as_view({'get':'list','post':'create'}), name='userprofile_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}),
         name='userprofile_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('', ProductListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('product/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('photo/', ProductPhotosViewSet.as_view({'get': 'list', 'post': 'create'}), name='productphoto_list'),
    path('photo/<int:pk>/', ProductPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='productphoto_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='rating_detail'),

    path('review/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

]