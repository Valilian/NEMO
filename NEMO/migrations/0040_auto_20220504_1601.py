# Generated by Django 3.2.12 on 2022-05-04 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0039_version_4_1_0'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpagechoice',
            name='hide_from_staff',
            field=models.BooleanField(default=False, help_text='Hides this choice from normal users, staff and technicians. When checked, only facility managers and super-users can see the choice'),
        ),
        migrations.AlterField(
            model_name='landingpagechoice',
            name='hide_from_users',
            field=models.BooleanField(default=False, help_text='Hides this choice from normal users. When checked, only staff, technicians, facility managers and super-users can see the choice'),
        ),
    ]
