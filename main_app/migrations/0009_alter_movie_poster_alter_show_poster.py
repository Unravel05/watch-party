# Generated by Django 5.0.4 on 2024-04-15 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_moviereview_date_alter_showreview_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.CharField(default='/vkcajIqORuKfd8uV2GYULlHut9o.jpg'),
        ),
        migrations.AlterField(
            model_name='show',
            name='poster',
            field=models.CharField(default='/mI2LuUls15AfFktdCYRNS4LGMfz.jpg'),
        ),
    ]