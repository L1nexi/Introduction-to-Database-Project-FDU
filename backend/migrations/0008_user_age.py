# Generated by Django 5.0.6 on 2024-06-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_artist_follower_user_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0, help_text='Enter an age'),
        ),
    ]