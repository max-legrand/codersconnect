# Generated by Django 2.2.5 on 2020-02-04 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_auto_20200204_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('organization', models.ForeignKey(default=None, on_delete='CASCADE', to='users.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept_user', models.ForeignKey(default=None, on_delete='CASCADE', to='users.ExtendedUser')),
                ('post', models.ForeignKey(default=None, on_delete='CASCADE', to='posts.Postings')),
            ],
        ),
    ]