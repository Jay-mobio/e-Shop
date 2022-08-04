# Generated by Django 4.0.6 on 2022-08-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_varified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/images/profile1.png', null=True, upload_to=''),
        ),
    ]
