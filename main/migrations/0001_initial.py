# Generated by Django 3.1.1 on 2020-09-05 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=128)),
                ('big_desc', models.TextField(blank=True, default='')),
                ('short_desc', models.TextField(blank=True, default='')),
                ('to_do', models.TextField(blank=True, default='')),
                ('color', models.TextField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, default='', max_length=128)),
                ('request_link', models.CharField(blank=True, default='', max_length=128)),
                ('request_number', models.SmallIntegerField()),
                ('status', models.CharField(blank=True, default='', max_length=128)),
                ('is_game_technician', models.BooleanField(default=False)),
                ('madness_level', models.SmallIntegerField(default=0)),
                ('madness_level_near', models.SmallIntegerField(default=0)),
                ('is_crazy', models.BooleanField(default=False)),
                ('sex', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='male', max_length=1)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.manager')),
                ('states', models.ManyToManyField(blank=True, to='main.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Passport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(blank=True, default='', max_length=128)),
                ('last_name', models.CharField(blank=True, default='', max_length=128)),
                ('birthday', models.DateField(auto_now=True)),
                ('passport_id', models.CharField(blank=True, default='', max_length=128)),
                ('address', models.CharField(blank=True, default='', max_length=128)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GunDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(blank=True, default='', max_length=128)),
                ('date', models.DateField()),
                ('gun', models.CharField(blank=True, default='', max_length=128)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('friend1', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='person1', to='main.person')),
                ('friend2', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='person2', to='main.person')),
                ('friend3', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='person3', to='main.person')),
                ('friend4', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='person4', to='main.person')),
                ('friend5', models.ForeignKey(null=True, on_delete=django.db.models.fields.NOT_PROVIDED, related_name='person5', to='main.person')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FingerPrint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_app', models.CharField(blank=True, default='', max_length=128)),
                ('in_base', models.CharField(blank=True, default='', max_length=128)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DriversLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('license_id', models.CharField(max_length=10)),
                ('parking_place', models.CharField(blank=True, default='', max_length=128)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_app', models.CharField(blank=True, default='', max_length=128)),
                ('in_base', models.CharField(blank=True, default='', max_length=128)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bank_account_number', models.CharField(blank=True, default='', max_length=128)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('is_black', models.BooleanField(default=False)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
