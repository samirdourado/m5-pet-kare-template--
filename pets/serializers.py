from rest_framework import serializers
from .models import SexPet
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from groups.models import Group


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=SexPet.choices,
        default=SexPet.NOT_INFORMED
    )
    group = GroupSerializer()    
    traits = TraitSerializer(many=True)
