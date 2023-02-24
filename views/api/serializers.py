from rest_framework import serializers
from views.models import View


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = [
            'id',
            'viewed_at'
        ]
