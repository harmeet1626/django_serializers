from django.shortcuts import render
from .models import user_details, address
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .serializer import User_details_serialiser, createUser, Address_serialiser, get_User_details_serialiser
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from serializers_app.paginations import SetPaginationPagesize,SetPaginationLimitOffset,SetPaginationCursor
from rest_framework import filters
from django.core.paginator import Paginator
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated ,BasePermission ,AllowAny,IsAdminUser



class PermissionByCondition(BasePermission):
    def has_permission(self, request, view):
        return True 
    



@api_view(['get', 'POST'])
def sendMail(request):
    try:
        subject = 'Subject of your email'
        message = 'This is the message body of your email.'
        from_email = 'harmeet_singh1@softprodigy.com'  # Sender's email address
        recipient_list = ['pratiksha_saluja@softprodigy.com']  # List of recipient email addresses
        send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        return Response("Email sent!!")
    except Exception as E:
        return Response(str(E))




# @api_view(['get','post'])
def homePage(request):
    return render(request,'homePage.html')

@api_view(['GET'])
def get_all_records(request):
    query = user_details.objects.all()
    query = User_details_serialiser(query, many=True)
    return Response(query.data)
    # query = query.values()
    # return Response(dict(data=query))

@api_view(['get', 'POST'])
def get_records_by_id(request, id):
    query= user_details.objects.get(user_id=id)
    query = User_details_serialiser(query)
    return Response(query.data)

# @api_view(['get','POST'])
# def create_records(request):
#     # serialize = User_details_serialiser(data=request.data)
#     queryset = users_detail_child.objects.all()

#     # serialize = User_details_serialiser(data=queryset, many=True)
#     # if serialize.is_valid():
#     #     # serialize.save()
#     #     return Response(serialize.data)
#     # else:
#     #     print(serialize.errors)
#     return Response(queryset.values())

@api_view(['get','POST'])
def create_records(request):
    serializer = User_details_serialiser(data= request.data)
    if serializer.is_valid():
        
        serializer.save()
    else:
        print(serializer.errors)
    return Response("worked")


@api_view(['GET','POST'])
def update_record(request, id):
    query = user_details.objects.get(user_id=id)
    serialize = User_details_serialiser(instance=query, data = request.data)
    if serialize.is_valid():
        serialize.save()
    return Response(serialize.data)
    


@api_view(['POST'])
def add_data(request):
    # query= users_detail_child.objects
    print(request.data)
    serializer = User_details_serialiser(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



class UserList(generics.ListAPIView):
    # permission_classes = PermissionByCondition
    queryset = user_details.objects.all()
    pagination_class = SetPaginationPagesize
    serializer_class= User_details_serialiser    
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset.values())        
        a = self.get_paginated_response(page)
        return Response(a)
        
    # def get_queryset(self):
    #     queryset=user_details.objects.all()
    #     return queryset

        # queryset = self.get_queryset()
        # print(queryset.data)
        # pagicreateUsernator = SetPaginationPagesize()
        # pagination_var = paginator.paginate_queryset(queryset, request)
        # serializer = User_details_serialiser(self.get_queryset, many=True)
        # res = {"total_data": len(self.get_queryset()), "data":serializer.data}
        # return Response(res)

    # def list(self, request):

    #     queryset = user_details.objects.all()
    #     # print(queryset.data)
    #     # paginator = SetPaginationPagesize()
    #     # pagination_var = paginator.paginate_queryset(queryset, request)
    #     pagination_class = LimitOffsetPagination
    #     serializer = User_details_serialiser(queryset, many=True)
    #     res = {"total_data": len(queryset), "data":serializer.data}
    #     return Response(res)        
        # limit = int(request.query_params.get('limit', 10))
        # offset = int(request.query_params.get('offset', 0))
        # username = request.query_params.get('username')
        # if username:
        #     queryset = queryset.filter(username__icontains = username)
        # serializer = User_details_serialiser(queryset[offset:offset+limit], many=True)
        # serializer = User_details_serialiser(queryset, many=True)
        # res = {"total_data": len(self.get_queryset()), "data":serializer.data}
    


class UserList_id( generics.DestroyAPIView, generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, user_id):
        queryset = user_details.objects.filter(user_id = user_id)
        if queryset:
            serializer_class = User_details_serialiser(queryset, many=True)
            return Response(serializer_class.data)
        else:
            return Response("No user found")
    
    def delete(self, request, user_id):
        queryset = user_details.objects.get(user_id = user_id)
        queryset.delete()
        return Response("User deleted successfully")


class AddUser(generics.ListAPIView):
# case of single serializer

    # serialised_class = createUser
    # def post (self, request, *args, **kwargs):
    #     try:
    #         serialised_class = createUser(data=request.data)
    #         if serialised_class.is_valid():
    #             serialised_class.save()
    #         else:
    #             print(serialised_class.errors)
    #         res = {"message":"user Created Successfully"}
    #         return Response(res)
        
    #     except Exception as E:
    #         print(str(E))
    #         return Response(str(E))

# case of multipal serializer
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            user_data = data.pop("user_details")
            user_address = data
            user_details_serializer_class = User_details_serialiser(data = user_data)
            user_address_serializer_class = Address_serialiser(data = user_address)
            if user_details_serializer_class.is_valid():            
                if user_address_serializer_class.is_valid():
                    user_details_obj = user_details.objects.create(**user_details_serializer_class.data)
                    address.objects.create(user_details=user_details_obj,**user_address_serializer_class.data)
                    return Response("user created")
                else:
                    print(user_address_serializer_class.errors)
            else:
                print(user_details_serializer_class.errors)
            return Response('Called')
        except Exception as E:
            return str(E)


    def get(self, request):
        try:
            queryset=user_details.objects.all()
            print(queryset)
            serialized = get_User_details_serialiser(queryset, many=True)
            print('after queryset')
            return Response(serialized.data)

        except Exception as E:
            return Response(str(E))
        

         

