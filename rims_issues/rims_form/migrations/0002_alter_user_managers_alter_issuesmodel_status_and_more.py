# Generated by Django 4.0.1 on 2022-06-22 21:22

from django.db import migrations, models
import rims_form.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('rims_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', rims_form.models.CustomManager()),
            ],
        ),
        migrations.AlterField(
            model_name='issuesmodel',
            name='status',
            field=models.CharField(choices=[('NEW', 'New'), ('RESOLVED', 'Resolved')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
