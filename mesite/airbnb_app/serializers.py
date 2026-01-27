from rest_framework import serializers
from .models import (Country,UserProfile,City,Service,Apartment,
  ApartmentImages, Booking, Review,  Favorite, FavoriteItem)

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user_role']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']


class CountryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id','city_name']

class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id','service_name']

class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class ApartmentListSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()

    class Meta:
        model = Apartment
        fields = ['id', 'apartment_name', 'country']


class ApartmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'

class ApartmentListImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImages
        fields = ['id']

class ApartmentDetailImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImages
        fields = '__all__'


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','user','apartment']

class BookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','user','apartment']

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Favorite
        fields = ['id']

class FavoriteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Favorite
        fields = '__all__'

class FavoriteListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  FavoriteItem
        fields = ['id','favorite']

class FavoriteDetailItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  FavoriteItem
        fields = '__all__'



