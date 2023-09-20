"""
URL configuration for serializers_practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from serializers_app.views import get_all_records,get_records_by_id,create_records, update_record
from serializers_app.views import UserList, UserList_id, add_data, AddUser

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get_all_records/', get_all_records),
    # path('get_records_by_id/<int:id>/', get_records_by_id),
    # path('create_records/', create_records),
    # path('update_record/<int:id>/', update_record),
    path('users/', UserList.as_view()),
    path('users/<user_id>/', UserList_id.as_view()),
    path('addUser/', AddUser.as_view())

]
