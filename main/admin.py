from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# from .admin_models import *
from django.contrib.auth.admin import UserAdmin

# admin.site.register(User, UserAdmin)
# Register your models here.s
# @admin.register(OrderType)
# class OrderTypeAdmin(admin.ModelAdmin):
#     pass


@admin.register(State)
class  StateAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class ManagerProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Passport)
class PassportErrorAdmin(admin.ModelAdmin):
    pass


@admin.register(DriversLicence)
class DriversLicenceAdmin(admin.ModelAdmin):
    pass


@admin.register(FingerPrint)
class FingerPrintAdmin(admin.ModelAdmin):
    pass


@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    pass


@admin.register(Blood)
class BloodAdmin(admin.ModelAdmin):
    pass


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    pass
