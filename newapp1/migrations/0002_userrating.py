# Generated by Django 3.1.5 on 2021-08-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.IntegerField()),
            ],
        ),
    ]
