# Generated by Django 2.0.6 on 2018-07-02 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('studentreport', '0004_auto_20180629_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsdata',
            name='admission_year',
            field=models.CharField(choices=[('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039'), ('2040', '2040'), ('2041', '2041'), ('2042', '2042'), ('2043', '2043')], default=django.utils.timezone.now, help_text='Class Name', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentsdata',
            name='image',
            field=models.CharField(default='profile picture', help_text='Image', max_length=250),
            preserve_default=False,
        ),
    ]
