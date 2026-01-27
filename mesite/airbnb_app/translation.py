from modeltranslation.translator import register, TranslationOptions
from .models import Country, City, Service, Apartment

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name',)

@register(Apartment)
class ApartmentTranslationOptions(TranslationOptions):
    fields = ('apartment_name', 'description',)
