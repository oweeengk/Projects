# Generated by Django 4.2.5 on 2024-01-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_stories_delete_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='category',
            field=models.CharField(choices=[('statements', 'Statements'), ('notices', 'Notices'), ('projects', 'Projects'), ('announcements', 'Announcements'), ('meetings', 'Meetings'), ('assessments', 'Assessments'), ('announcements', 'Announcements'), ('teambuilding', 'Teambuilding')], max_length=20),
        ),
    ]
