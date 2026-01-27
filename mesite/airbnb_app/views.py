from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .permissions import IsOwnerOrReadOnly, IsAdminUser
from .models import (
    Country, UserProfile, City, Service,
    Apartment, ApartmentImages, Booking,
    Review, Favorite, FavoriteItem
)
from .serializers import (
    CountryListSerializer, CountryDetailSerializer,
    UserProfileListSerializer, UserProfileDetailSerializer,
    CityListSerializer, CityDetailSerializer,
    ServiceListSerializer, ServiceDetailSerializer,
    ApartmentListSerializer, ApartmentDetailSerializer,
    ApartmentListImagesSerializer, ApartmentDetailImagesSerializer,
    BookingListSerializer, BookingDetailSerializer,
    ReviewListSerializer, ReviewDetailSerializer,
    FavoriteListSerializer, FavoriteDetailSerializer,
    FavoriteListItemSerializer, FavoriteDetailItemSerializer
)

User = get_user_model()

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAdminUser]

class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer
    permission_classes = [IsAdminUser]

class UserProfileListView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user_role', 'country']
    search_fields = ['username', 'first_name', 'last_name']
    ordering_fields = ['age', 'register_date']
    permission_classes = [IsAdminUser]

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CityListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country']
    search_fields = ['city_name']
    ordering_fields = ['city_name']
    permission_classes = [IsAdminUser]

class CityDetailView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
    permission_classes = [IsAdminUser]

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['service_name']
    ordering_fields = ['service_name']
    permission_classes = [IsAdminUser]

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceDetailSerializer
    permission_classes = [IsAdminUser]

class ApartmentListView(generics.ListAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country', 'city', 'apartment_stars']
    search_fields = ['apartment_name', 'street']
    ordering_fields = ['apartment_stars', 'postal_code']
    permission_classes = [IsOwnerOrReadOnly]

class ApartmentDetailView(generics.RetrieveAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ApartmentImagesListView(generics.ListAPIView):
    queryset = ApartmentImages.objects.all()
    serializer_class = ApartmentListImagesSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ApartmentImagesDetailView(generics.RetrieveAPIView):
    queryset = ApartmentImages.objects.all()
    serializer_class = ApartmentDetailImagesSerializer
    permission_classes = [IsOwnerOrReadOnly]

class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'apartment']
    ordering_fields = ['check_in', 'check_out', 'created_add']
    permission_classes = [IsOwnerOrReadOnly]

class BookingDetailView(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['user', 'apartment', 'rating']
    search_fields = ['text']
    ordering_fields = ['rating']
    permission_classes = [IsOwnerOrReadOnly]

class ReviewDetailView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteListSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FavoriteDetailView(generics.RetrieveAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FavoriteItemListView(generics.ListAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteListItemSerializer
    permission_classes = [IsOwnerOrReadOnly]

class FavoriteItemDetailView(generics.RetrieveAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteDetailItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
