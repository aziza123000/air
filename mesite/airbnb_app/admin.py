from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


class ApartmentImagesInline(admin.TabularInline):
    model = ApartmentImages
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    fk_name = 'apartment'
    extra = 1

class FavoriteItemInline(admin.TabularInline):
    model = FavoriteItem
    extra = 1

# Admin
@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    pass

@admin.register(City)
class CityAdmin(TranslationAdmin):
    pass

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    pass

@admin.register(Apartment)
class ApartmentAdmin(TranslationAdmin):
    inlines = [ApartmentImagesInline, ReviewInline]

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    inlines = [FavoriteItemInline]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'apartment', 'check_in', 'check_out', 'created_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_role', 'country')


