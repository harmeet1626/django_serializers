from rest_framework.pagination import CursorPagination ,PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from django.http import JsonResponse

class SetPaginationPagesize(PageNumberPagination):
    page_size=5
    page_query_param = 'page'
    page_size_query_param = 'size'
    max_page_size = 20
    last_page_strings = [("last_page")]


    def get_paginated_response(self, data):
        response = Response(data)
        response['count'] = self.page.paginator.count
        response['next'] = self.get_next_link()
        response['previous'] = self.get_previous_link()
        return {"data":data,"status":200,"count":self.page.paginator.count, "next_link":self.get_next_link(),"previous":self.get_previous_link()}





# class SetPaginationPagesize(PageNumberPagination):
#     page_size = 2
#     page_query_param = 'page'
#     last_page_strings = [("last_page")]

#     page_size_query_param ='size'
#     max_page_size = 10


    

class SetPaginationLimitOffset(LimitOffsetPagination):
    default_limit = 3
    limit_query_param = 'limit'
    max_limit = 10


class SetPaginationCursor(CursorPagination):
    page_size = 3
    cursor_query_param = 'c'
    ordering = 'name'

    