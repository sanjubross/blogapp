# Generated by Django 3.2.4 on 2021-06-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(null=True, upload_to='public/blog/images'),
        ),
    ]