from rest_framework import serializers

from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    data_inicio = serializers.DateTimeField(source='start_date')
    data_fim = serializers.DateTimeField(source='end_date')
    classificacao = serializers.IntegerField(source='classification')
    nota = serializers.IntegerField(source='rating', min_value=1, max_value=5)

    class Meta:
        model = Trip
        fields = ('id', 'data_inicio', 'data_fim', 'classificacao', 'nota')
