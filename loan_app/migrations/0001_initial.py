# Generated by Django 4.2.1 on 2023-09-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LoanApplication",
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
                ("applicant_name", models.CharField(max_length=100)),
                ("business_name", models.CharField(max_length=100)),
                (
                    "requested_loan_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("has_profit_last_12_months", models.BooleanField()),
                (
                    "average_asset_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("pre_assessment", models.IntegerField(default=20)),
            ],
        )
    ]
