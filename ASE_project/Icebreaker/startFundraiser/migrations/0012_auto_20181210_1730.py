# Generated by Django 2.1.2 on 2018-12-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startFundraiser', '0011_reward_claimed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faqs',
            name='answer',
            field=models.TextField(default='Its for a good cause', max_length=200),
        ),
        migrations.AlterField(
            model_name='faqs',
            name='question',
            field=models.TextField(default='What are you raising funds for?', max_length=100),
        ),
    ]
