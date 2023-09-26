
from django.contrib import admin
from django.urls import path
from serializers_app.views import get_all_records,get_records_by_id,create_records, update_record
from serializers_app.views import UserList, UserList_id, add_data, AddUser,sendMail, homePage
from stripe_payment.views import create_checkout_session, HomePageView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rayzorpay_payment.views import paymenthandler, homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('get_all_records/', get_all_records),
    # path('get_records_by_id/<int:id>/', get_records_by_id),
    # path('create_records/', create_records),
    # path('update_record/<int:id>/', update_record),
    # path('users/', UserList.as_view()),
    # path('users/<user_id>/', UserList_id.as_view()),
    # path('addUser/', AddUser.as_view()),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('sendMail/', sendMail, name='send_mail' ),
    # path('homePage/', homePage, name='homePage' )
    path('', HomePageView.as_view(), name='home'),
    # path('payment/', stripe_config, name='payment' ),
    path('create-checkout-session/', create_checkout_session),
    path('home/', homepage, name='index'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    

]
