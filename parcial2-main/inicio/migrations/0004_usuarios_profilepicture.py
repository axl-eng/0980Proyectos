# Generated by Django 5.0.2 on 2024-04-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_usuarios_age_usuarios_dpi_usuarios_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='profilePicture',
            field=models.ImageField(default='image.jpg', upload_to='Imagenes_Fid'),
        ),
    ]
