from django.conf import settings # new
from django.http.response import JsonResponse,HttpResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.views.generic.base import TemplateView
import stripe
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'stripe_payment.html'
stripe.api_key = 'sk_test_51Mg4qcSHH6lTciJeaGNI4OHXueQleXieDaBKw4dQoPQWNBQMFOsplYfSTBVwdBStSJQLlFvFPphfFvIKUy3wAyyn008SW57vtP'

@api_view([ 'POST'])
def create_checkout_session(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                # {
                #    "price_data": {
                #             "currency": "INR",
                #             "unit_amount": 2000,  # Amount in cents (e.g., $20.00)
                #             "product_data": {
                #                 "name": "Donate a coffee",
                #                 "images": ["https://img.icons8.com/?size=512&id=4HBoNoTgzJzF&format=png"],
                #             },
                #         },
                #         "quantity": 1,
                # },
                {
                   "price_data": {
                            "currency": "INR",
                            "unit_amount": 3400*100,  # Amount in cents (e.g., $20.00)
                            "product_data": {
                                "name": "Donate a tea",
                                "images": ["https://img.icons8.com/?size=512&id=4HBoNoTgzJzF&format=png"],
                            },
                        },
                        "quantity": 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000' ,
            cancel_url='http://127.0.0.1:8000',
        )
        # return HttpResponse('intent created')
    except Exception as e:
        return HttpResponse(str(e))
    return redirect(checkout_session.url, code=303)
