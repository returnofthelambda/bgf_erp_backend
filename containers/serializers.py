from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Container


class ContainerListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Container
        fields = [
            'number',
            'pickup_date',
            'booking',
            'status',
            'absolute_url',
        ]

    def get_absolute_url(self, obj):
        return reverse('container_detail', args=(obj.pk,))


class ContainerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = [
            'id',
            'number',
            'pickup_date',
            'load_date',
            'departure_date',
            'steamship',
            'booking',
            'railyard',
            'size',
            'status',
        ]
