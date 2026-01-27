from django.urls import path
from .views import (
    CountryListView, CountryDetailView,
    CityListView, CityDetailView,
    ServiceListView, ServiceDetailView,
    ApartmentListView, ApartmentDetailView,
    ApartmentImagesListView, ApartmentImagesDetailView,
    BookingListView, BookingDetailView,
    ReviewListView, ReviewDetailView,
    FavoriteListView, FavoriteDetailView,
    FavoriteItemListView, FavoriteItemDetailView,
    UserProfileListView, UserProfileDetailView
)
from .views import RegisterView, MyTokenObtainPairView

urlpatterns = [

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('countries/', CountryListView.as_view(), name='countries-list'),
    path('countries/<int:pk>/', CountryDetailView.as_view(), name='countries-detail'),

    path('users/', UserProfileListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserProfileDetailView.as_view(), name='users-detail'),

    path('cities/', CityListView.as_view(), name='cities-list'),
    path('cities/<int:pk>/', CityDetailView.as_view(), name='cities-detail'),

    path('services/', ServiceListView.as_view(), name='services-list'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='services-detail'),

    path('apartments/', ApartmentListView.as_view(), name='apartments-list'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartments-detail'),

    path('apartment-images/', ApartmentImagesListView.as_view(), name='apartment-images-list'),
    path('apartment-images/<int:pk>/', ApartmentImagesDetailView.as_view(), name='apartment-images-detail'),

    path('bookings/', BookingListView.as_view(), name='bookings-list'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='bookings-detail'),

    path('reviews/', ReviewListView.as_view(), name='reviews-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='reviews-detail'),

    path('favorites/', FavoriteListView.as_view(), name='favorites-list'),
    path('favorites/<int:pk>/', FavoriteDetailView.as_view(), name='favorites-detail'),

    path('favorite-items/', FavoriteItemListView.as_view(), name='favorite-items-list'),
    path('favorite-items/<int:pk>/', FavoriteItemDetailView.as_view(), name='favorite-items-detail'),
]
