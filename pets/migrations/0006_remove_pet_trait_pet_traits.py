# Generated by Django 4.2 on 2023-04-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traits', '0003_remove_trait_traits'),
        ('pets', '0005_pet_trait'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='trait',
        ),
        migrations.AddField(
            model_name='pet',
            name='traits',
            field=models.ManyToManyField(related_name='pets', to='traits.trait'),
        ),
    ]
