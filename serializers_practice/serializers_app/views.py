from django.shortcuts import render
from .models import user_details
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from .serializer import arrange_data




@api_view(['GET'])
def get_all_records(request):
    query = user_details.objects.all()
    query = arrange_data(query, many=True)
    return Response(query.data)
    # query = query.values()
    # return Response(dict(data=query))

@api_view(['get', 'POST'])
def get_records_by_id(request, id):
    query= user_details.objects.get(user_id=id)
    query = arrange_data(query, many=False)
    return Response(query.data)

@api_view(['get','POST'])
def create_records(request):
    serialize = arrange_data(data=request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize)


@api_view(['GET','POST'])
def update_record(request, id):
    query = user_details.objects.get(user_id=id)
    serialize = arrange_data(instance=query, data = request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)