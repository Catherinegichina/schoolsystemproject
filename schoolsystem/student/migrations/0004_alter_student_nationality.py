# Generated by Django 3.2.4 on 2021-08-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_admission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('k', 'Kenyan'), ('r', 'Rwandan'), ('u', 'Ugandan'), ('t', 'Tanzanian'), ('a', 'Algerian'), ('a', 'Angolan'), ('b', 'Burundian'), ('b', 'Burkinabe'), ('c', 'Cameroonian')], max_length=20),
        ),
    ]
