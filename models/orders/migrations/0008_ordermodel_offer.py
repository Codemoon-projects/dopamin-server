# Generated by Django 4.2.11 on 2024-11-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_person_ordermodel_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='offer',
            field=models.IntegerField(default=0, verbose_name='درصد تخفیف'),
        ),
    ]
