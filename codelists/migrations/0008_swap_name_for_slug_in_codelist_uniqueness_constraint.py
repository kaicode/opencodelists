# Generated by Django 3.1 on 2020-08-27 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("opencodelists", "0002_auto_20200424_1017"),
        ("codelists", "0007_auto_20200722_1438"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="codelist", unique_together={("project", "name", "slug")},
        ),
    ]
