# Generated by Django 4.2.7 on 2023-11-29 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('AppPro', '0009_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group'),
        ),
    ]
