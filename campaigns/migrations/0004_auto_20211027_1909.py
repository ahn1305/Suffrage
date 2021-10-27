# Generated by Django 3.2.8 on 2021-10-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0003_auto_20211027_1904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_check',
            name='organization_name',
        ),
        migrations.AddField(
            model_name='user_check',
            name='org_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user_check',
            name='usr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]