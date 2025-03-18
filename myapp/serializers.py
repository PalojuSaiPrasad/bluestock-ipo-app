from rest_framework import serializers
from .models import IPO
from datetime import date


class IPOSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPO
        fields = '__all__'  # Adjust fields as necessary


def validate_Company_name(self, value):
    if not value.strip():
        raise serializers.ValidationError("Comapany name cannot be empty ")
    return value


def validate_price(value):
    if value <= 0:
        raise serializers.ValidationError("Price must be a positive number")
    return value


def validate_date(self, data):

    open_date = data.get("open_date")
    close_date = data.get("close_date")

    if self.instance is None and open_date and open_date < date.today():
        raise serializers.ValidationError("open date cannot be in the past")

    if open_date and close_date and close_date < open_date:
        raise serializers.ValidationError("Close date must be after open date")
    return date
