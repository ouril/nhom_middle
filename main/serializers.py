from rest_framework import serializers

from main.models import *


class StateSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = State
        fields = "__all__"




class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = "__all__"


class PassportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passport
        fields = "__all__"

class FingerPrintSerializer(serializers.ModelSerializer):

    class Meta:
        model = FingerPrint
        fields = "__all__"


class FriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friends
        fields = "__all__"

class DriverLicenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriversLicence
        fields = "__all__"

class GunLicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GunDocument
        fields = "__all__"


class BloodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blood
        fields = "__all__"

class BankaccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"

class PersonSerializer(serializers.ModelSerializer):
    passport = PassportSerializer()
    driverslicence = DriverLicenceSerializer()
    gundocument = GunLicenceSerializer()
    friends = FriendsSerializer()
    bankaccount = BankaccountSerializer(many=True)
    blood = BloodSerializer()

    class Meta:
        model = Person
        fields = "__all__"



