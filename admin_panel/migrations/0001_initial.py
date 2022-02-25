# Generated by Django 4.0.2 on 2022-02-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicalType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Name', models.CharField(max_length=50)),
                ('Type_Image', models.ImageField(upload_to='type_img')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
