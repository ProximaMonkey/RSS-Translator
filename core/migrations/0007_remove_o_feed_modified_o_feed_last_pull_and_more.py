# Generated by Django 5.0.2 on 2024-02-26 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_o_feed_update_frequency"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="o_feed",
            name="modified",
        ),
        migrations.AddField(
            model_name="o_feed",
            name="last_pull",
            field=models.DateTimeField(
                blank=True,
                default=None,
                editable=False,
                help_text="Last time the feed was pulled",
                null=True,
                verbose_name="Last Pull(UTC)",
            ),
        ),
        migrations.AddField(
            model_name="o_feed",
            name="last_updated",
            field=models.DateTimeField(
                blank=True,
                default=None,
                editable=False,
                help_text="Last updated from the original feed",
                null=True,
                verbose_name="Last Updated(UTC)",
            ),
        ),
        migrations.AlterField(
            model_name="o_feed",
            name="etag",
            field=models.CharField(default="", editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name="o_feed",
            name="sid",
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="o_feed",
            name="size",
            field=models.IntegerField(default=0, editable=False, verbose_name="Size"),
        ),
        migrations.AlterField(
            model_name="o_feed",
            name="valid",
            field=models.BooleanField(editable=False, null=True, verbose_name="Valid"),
        ),
        migrations.AlterField(
            model_name="t_feed",
            name="modified",
            field=models.DateTimeField(
                blank=True,
                editable=False,
                help_text="Last time the feed was translated",
                null=True,
                verbose_name="Last Modified",
            ),
        ),
        migrations.AlterField(
            model_name="t_feed",
            name="size",
            field=models.IntegerField(default=0, editable=False, verbose_name="Size"),
        ),
        migrations.AlterField(
            model_name="t_feed",
            name="status",
            field=models.BooleanField(
                editable=False, null=True, verbose_name="Translation Status"
            ),
        ),
    ]
