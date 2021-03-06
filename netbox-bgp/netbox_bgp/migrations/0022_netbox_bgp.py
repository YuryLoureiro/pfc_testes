# Generated by Django 4.0.3 on 2022-05-12 07:42

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0057_created_datetimefield'),
        ('extras', '0073_journalentry_tags_custom_fields'),
        ('netbox_bgp', '0021_netbox32_support'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoutingPolicyRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('index', models.PositiveIntegerField()),
                ('action', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('match_ip_cond', models.JSONField(blank=True, null=True)),
                ('match_custom', models.JSONField(blank=True, null=True)),
                ('set_actions', models.JSONField(blank=True, null=True)),
                ('match_community', models.ManyToManyField(blank=True, related_name='+', to='netbox_bgp.community')),
                ('match_ip', models.ManyToManyField(blank=True, related_name='+', to='ipam.prefix')),
                ('routing_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rules', to='netbox_bgp.routingpolicy')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('routing_policy', 'index'),
                'unique_together': {('routing_policy', 'index')},
            },
        ),
    ]
