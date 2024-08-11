from rest_framework import serializers
from .models import CampDetails


class AddCampSerializers(serializers.ModelSerializer):
    class Meta:
        model = CampDetails
        fields = "__all__"