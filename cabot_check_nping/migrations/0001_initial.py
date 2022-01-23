# Generated by Django 3.2.11 on 2022-01-23 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cabotapp", "0002_auto_20220122_2317"),
    ]

    operations = [
        migrations.CreateModel(
            name="NPINGStatusCheck",
            fields=[
                (
                    "statuscheck_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cabotapp.statuscheck",
                    ),
                ),
                (
                    "host",
                    models.TextField(
                        help_text="Host to check.", verbose_name="Target host(s)"
                    ),
                ),
                (
                    "nping_cmd_line_switches",
                    models.TextField(
                        help_text="Enter switches as they vould be entered on the command line.",
                        verbose_name="NPing command line switches",
                    ),
                ),
                (
                    "count",
                    models.PositiveIntegerField(
                        default=1, help_text="Number of packet to send."
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("cabotapp.statuscheck",),
        ),
    ]
