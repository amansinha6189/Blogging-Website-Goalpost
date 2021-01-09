# Generated by Django 3.0.6 on 2020-07-11 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
            ],
        ),
    ]
