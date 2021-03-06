# Generated by Django 4.0.1 on 2022-01-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_submission_code_alter_constraint_given_constraint_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='language_used',
            field=models.CharField(choices=[('Java', 'Java'), ('C++', 'C++'), ('C', 'C'), ('Python', 'Python'), ('JavaScript', 'JavaScript')], help_text='Programming language used to submit the problem', max_length=200),
        ),
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Wrong Answer', 'Wrong Answer'), ('Runtime Error', 'Runtime Error'), ('Time Limit Exceeded', 'Time Limit Exceeded'), ('Compilation Error', 'Compilation Error'), ('Memory Limit Exceeded', 'Memory Limit Exceeded')], help_text='If the submission is accepted or not', max_length=100),
        ),
    ]
