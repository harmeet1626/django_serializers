from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from .models import user_details


class arrange_data(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ['user_id','username', 'first_name', 'last_name', 'gender', 'password','status']
        # fields = '__all__'

    # def is_valid(self, *, raise_exception=False):
    #     return super().is_valid(raise_exception=raise_exception)
    

    # def validate(self, data):
    #         print("outside")    
    #         if data['status']!="active":
    #             print("inside ")
    #             raise serializers.ValidationError('User not active')    
    #         return data
	

   
