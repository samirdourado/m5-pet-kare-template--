from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView, Request, Response, status
from .models import Pet
from django.forms.models import model_to_dict
from .serializers import PetSerializer
from groups.models import Group
from traits.models import Trait
from rest_framework.pagination import PageNumberPagination


class PetView(APIView, PageNumberPagination):

    def get(self, request: Request) -> Response:
        pets = Pet.objects.all()
        result_page = self.paginate_queryset(pets, request)

        serializer = PetSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)

    def post(self, request: Request) -> Response:

        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validated_group_data = serializer.validated_data.pop("group")
        validated_trait_data = serializer.validated_data.pop("traits")
        trait_list = []

        try:
            group_objects = Group.objects.get(scientific_name=validated_group_data["scientific_name"])
        except Group.DoesNotExist:
            group_objects = Group.objects.create(**validated_group_data)

        pet = Pet.objects.create(**serializer.validated_data, group=group_objects)

        for trait_name in validated_trait_data:
            group_traits = Trait.objects.filter(name__iexact=trait_name["name"]).first()

            if not group_traits:
                group_traits = Trait.objects.create(**trait_name)

            trait_list.append(group_traits)

        pet.traits.set(trait_list)

        serializer = PetSerializer(pet)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
