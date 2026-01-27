from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    country_images = models.ImageField(upload_to='country_images')
    country_name = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.country_name

class UserProfile(AbstractUser):
    user_name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(70)],
                                           null=True,blank=True)
    user_images = models.ImageField(upload_to='user_images',null=True,blank=True)
    phone_number = PhoneNumberField(null=True,blank=True)
    register_date = models.DateTimeField(auto_now_add=True)
    RoleChoices = (
    ('client','client'),
    ('owner','owner')
    )
    user_role = models.CharField(max_length=20,choices=RoleChoices)
    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return  f'{self.first_name},{self.last_name}'


class City (models.Model):
    country =  models.ForeignKey(Country,on_delete=models.CASCADE)
    city_images = models.ImageField(upload_to='city_images')
    city_name = models.CharField(max_length=100)

    def __str__(self):
         return self.city_name


class Service(models.Model):
    service_image = models.ImageField(upload_to='service_images')
    service_name = models.CharField(max_length=30)

    def __str__(self):
        return self.service_name


class Apartment  (models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='apartments')
    apartment_name = models.CharField(max_length=30)
    street = models.CharField(max_length=100)
    postal_code = models.PositiveSmallIntegerField(verbose_name='почтовый индекс')
    apartment_stars = models.PositiveSmallIntegerField(choices=[(i,str(i))for i in range(1,6)])
    description = models.TextField()
    apartment_service = models.ManyToManyField(Service)

    def __str__(self):
        return self.apartment_name



class ApartmentImages(models.Model):
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE,related_name='images')
    apartment_image = models.ImageField(upload_to='aprt_images/')

    def __str__(self):
        return f'{self.apartment},{self.apartment_image}'


class Booking(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.apartment},{self.user}"



class Review(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment,on_delete=models.CASCADE,related_name='reviews')
    rating = models.PositiveSmallIntegerField( choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.user},{self.apartment}'


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class  FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite,on_delete=models.CASCADE)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite},{self.apartment}'


