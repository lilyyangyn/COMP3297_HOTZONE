# Generated by Django 3.1.2 on 2020-11-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20201129_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='category',
            field=models.CharField(choices=[('Residence', 'Residence'), ('Workplace', 'Workplace'), ('Visit', 'Visit')], max_length=12),
        ),
    ]
