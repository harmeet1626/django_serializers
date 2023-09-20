from rest_framework.response import Response
from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from .models import user_details, address


class User_details_serialiser(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ['username', 'first_name', 'last_name', 'gender', 'password','status']
        # fields = '__all__'


class Address_serialiser(serializers.ModelSerializer):
    class Meta:
        model= address
        fields = ['city', 'State', 'PIN_code']


class get_User_details_serialiser(serializers.ModelSerializer):
    user_details_child = Address_serialiser()
    class Meta:
        model = user_details
        fields = ['username', 'first_name', 'last_name', 'gender', 'password','status', 'user_details_child']



class createUser(serializers.ModelSerializer):
    user_details = User_details_serialiser()

    class Meta:
        model =address
        fields = ['user_details','city', 'State', 'PIN_code', 'user_details']
        

    def create(self, validated_data):
        
        user_table_data = validated_data.pop("user_details")
        address_table_data = validated_data
        user_details_object = user_details.objects.create(**user_table_data)
        address.objects.create(user_details=user_details_object,**address_table_data)       
        return validated_data
    
    # def get_status_details(self, obj):
    #     user_data = address.objects.filter(id =1)
    #     data = {}
    #     print('111111111111111')
    #     data["city"] = obj.city
    #     data["State"] = obj.State
    #     data["PIN_Code"] = obj.PIN_Code
    #     print(data)
    #     return data
    #     # return user_data



# class User_details_serialiser(serializers.ModelSerializer):
#     user_details_child = User_details_serialiser()
#     class Meta:
#         model=users_detail_child
#         fields = ['name','email', 'age','user_details_child']

#     def create(self, validated_data):
#         print("7678623846823", validated_data)
#         child_details = validated_data.pop('user_details_child')
#         print(1111111,validated_data)
#         user_details_obj= user_details.objects.create(**validated_data)
#         print(2222222222222)
#         users_detail_child_data = users_detail_child.objects.create(user_details=user_details_obj, **child_details)
#         return("success!")


# class User_details_serialiser(serializers.ModelSerializer):
#     class Meta:
#         model=users_detail_child
#         fields = '__all__'

    # def is_valid(self, *, raise_exception=False):
    #     return super().is_valid(raise_exception=raise_exception)
    

    # def validate(self, data):
    #         print("outside")    
    #         if data['status']!="active":
    #             print("inside ")
    #             raise serializers.ValidationError('User not active')    
    #         return data


class profile:
     pass

   
