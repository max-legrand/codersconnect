# Generated by Django 3.0.3 on 2020-04-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_connection_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='postings',
            name='image',
            field=models.ImageField(default='placeholder.png', upload_to='images/posts'),
        ),
    ]
