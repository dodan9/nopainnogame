# Generated by Django 3.1.5 on 2021-08-03 06:31

from django.db import migrations, models
import django.db.models.deletion
import rental.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0005_auto_20210726_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceValues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('values', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(db_index=True, max_length=20)),
                ('type_id', models.IntegerField(choices=[(1, '1: speed'), (2, '2: simple'), (3, '3: competition'), (4, '4: explorer')])),
            ],
        ),
        migrations.CreateModel(
            name='RentalGame',
            fields=[
                ('game_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('game_name', models.CharField(max_length=40)),
                ('game_image', models.ImageField(blank=True, upload_to='static/game/')),
                ('release_date', models.DateField()),
                ('game_stock', models.IntegerField()),
                ('game_rfee', models.IntegerField()),
                ('game_description', models.TextField(max_length=500)),
                ('device_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='rental.devicevalues')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='rental.genre')),
            ],
            options={
                'ordering': ['-device_value', '-genre'],
            },
        ),
        migrations.CreateModel(
            name='RentalDevice',
            fields=[
                ('device_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('device_name', models.CharField(max_length=40)),
                ('device_pub', models.DateField()),
                ('platform', models.CharField(choices=[('PS', 'PlayStaion'), ('ND', 'Nintendo')], max_length=2)),
                ('device_image', models.ImageField(blank=True, upload_to='static/device/')),
                ('device_color', models.CharField(max_length=20)),
                ('device_state', models.CharField(choices=[('매우좋음', '매우좋음'), ('좋음', '좋음'), ('보통', '보통')], max_length=10)),
                ('device_rfee', models.IntegerField()),
                ('device_check', models.IntegerField(choices=[(0, '대여가능'), (1, '대여중')], default=0)),
                ('device_description', models.TextField(max_length=500)),
                ('device_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='rental.devicevalues')),
            ],
            options={
                'ordering': ['-device_value'],
            },
        ),
        migrations.CreateModel(
            name='GameRental',
            fields=[
                ('game_rental_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('gaddress', models.CharField(max_length=60)),
                ('grental_date', models.DateField(default=rental.models.get_drental_date, editable=False)),
                ('overdue', models.IntegerField(null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gRentals_id', to='rental.rentalgame')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gRentals_id', to='account.user')),
            ],
            options={
                'ordering': ['game_rental_id'],
            },
        ),
        migrations.CreateModel(
            name='DeviceReserve',
            fields=[
                ('device_reserve_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('device_reserve_date', models.DateField()),
                ('device_due_date', models.DateField()),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dReserve_id', to='rental.rentaldevice')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dReserve_id', to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='DeviceRental',
            fields=[
                ('device_rental_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('daddress', models.CharField(max_length=60)),
                ('drental_date', models.DateField(default=rental.models.get_drental_date, editable=False)),
                ('overdue', models.IntegerField(null=True)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dRentals_id', to='rental.rentaldevice')),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dRentals_id', to='account.user')),
            ],
            options={
                'ordering': ['device_rental_id'],
            },
        ),
    ]