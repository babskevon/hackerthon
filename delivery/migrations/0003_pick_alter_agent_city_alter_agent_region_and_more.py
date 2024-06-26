# Generated by Django 4.1 on 2024-05-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=255, null=True)),
                ('region', models.CharField(choices=[('Central', 'Central')], max_length=255)),
                ('city', models.CharField(choices=[('Banda', 'Banda')], max_length=255)),
                ('village', models.CharField(choices=[('Lubawo', 'Lubawo')], max_length=255, null=True)),
                ('street', models.CharField(choices=[('Luwum Street', 'Luwum Street')], max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='agent',
            name='city',
            field=models.CharField(choices=[('Banda', 'Banda')], max_length=255),
        ),
        migrations.AlterField(
            model_name='agent',
            name='region',
            field=models.CharField(choices=[('Central', 'Central')], max_length=255),
        ),
        migrations.AlterField(
            model_name='agent',
            name='street',
            field=models.CharField(choices=[('Luwum Street', 'Luwum Street')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='village',
            field=models.CharField(choices=[('Lubawo', 'Lubawo')], max_length=255, null=True),
        ),
    ]
