from django.db import models
from django.contrib.auth.models import User

# Create your models here.

EMPTY_STRING = ""


def simple_char_field() -> models.CharField:
    return models.CharField(
        blank=True,
        default=EMPTY_STRING,
        max_length=128
    )


class State(models.Model):
    name = simple_char_field()
    big_desc = models.TextField(blank=True, default=EMPTY_STRING)
    short_desc = models.TextField(blank=True, default=EMPTY_STRING)
    to_do = models.TextField(blank=True, default=EMPTY_STRING)
    color = models.TextField(max_length=6)

    def __str__(self):
        return f"State {self.name}"


class TimeStampedModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Manager(models.Model):
    name = simple_char_field()

    def __str__(self):
        return self.name


class Person(TimeStampedModel):
    MALE = 'male'
    FEMALE = 'female'

    SEX_CHOICE = (
        ("M", MALE),
        ("F", FEMALE),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING
    )
    name = simple_char_field()
    request_link = simple_char_field()
    request_number = models.SmallIntegerField()
    status = simple_char_field()
    profile_image = models.ImageField(upload_to="static",blank=True, null=True)
    manager = models.ForeignKey(
        Manager,
        models.CASCADE,
    )
    is_game_technician = models.BooleanField(default=False)
    madness_level = models.SmallIntegerField(default=0)
    madness_level_near = models.SmallIntegerField(default=0)
    is_crazy = models.BooleanField(default=False)
    states = models.ManyToManyField(State, blank=True)
    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICE,
        default=MALE,
    )

    def __str__(self):
        return self.name


class Document(TimeStampedModel):
    # model_name = ""
    person = models.OneToOneField(
        Person,
        models.CASCADE,
        # related_name=model_name

    )

    class Meta:
        abstract = True


class Passport(Document):
    first_name = simple_char_field()
    last_name = simple_char_field()
    birthday = models.DateField(
        auto_now=True
    )
    passport_id = simple_char_field()
    address = simple_char_field()

    def __str__(self):
        return f"Passport {self.first_name}  {self.first_name} ({self.person.name})"


class DriversLicence(Document):
    license_id = models.CharField(max_length=10)
    parking_place = simple_char_field()

    def __str__(self):
        return f"DriversLicence {self.license_id}  ({self.person.name})"


class GunDocument(Document):
    number = simple_char_field()
    date = models.DateField()
    gun = simple_char_field()

    def __str__(self):
        return f"GunLicence{self.number}  ({self.person.name})"


class FingerPrint(Document):
    in_app = simple_char_field()
    in_base = simple_char_field()

    def __str__(self):
        return f"FingerPrint {self.in_base}  ({self.person.name})"


class Blood(Document):
    in_app = simple_char_field()
    in_base = simple_char_field()

    def __str__(self):
        return f"Blood {self.in_base}  ({self.person.name})"


class BankAccount(TimeStampedModel):
    bank_account_number = simple_char_field()
    balance = models.PositiveIntegerField(default=0)
    is_black = models.BooleanField(default=False)
    person = models.ForeignKey(
        Person,
        models.CASCADE,
        related_name="bankaccount"
    )


    def __str__(self):
        return f"BankAccount {self.bank_account_number}  ({self.person.name})"


class Friends(Document):
    friend1 = models.ForeignKey(Person, models.NOT_PROVIDED, null=True, related_name="person1")
    friend2 = models.ForeignKey(Person, models.NOT_PROVIDED, null=True, related_name="person2")
    friend3 = models.ForeignKey(Person, models.NOT_PROVIDED, null=True, related_name="person3")
    friend4 = models.ForeignKey(Person, models.NOT_PROVIDED, null=True, related_name="person4")
    friend5 = models.ForeignKey(Person, models.NOT_PROVIDED, null=True, related_name="person5")

    def __str__(self):
        return f"Friends {self.person.name}"
