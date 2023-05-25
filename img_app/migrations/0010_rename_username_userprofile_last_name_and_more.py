# Generated by Django 4.2.1 on 2023-05-24 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("img_app", "0009_alter_userprofile_birthday"),
    ]

    operations = [
        migrations.RenameField(
            model_name="userprofile",
            old_name="username",
            new_name="last_name",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="avatar",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="birthday",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="description",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.EmailField(blank=True, max_length=30),
        ),
        migrations.CreateModel(
            name="WorkerPorfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
                ("email", models.EmailField(blank=True, max_length=30)),
                ("inn", models.CharField(blank=True, max_length=30)),
                (
                    "city",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "Выберите город"),
                            ("Уссурийск", "Уссурийск"),
                            ("Владивосток", "Владивосток"),
                            ("Хабаровск", "Хабаровск"),
                            ("Краснодар", "Краснодар"),
                        ],
                        default="",
                        max_length=20,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]