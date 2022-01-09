from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
     
     page_size = 5
     '''
     page_size_query_param specifies how many items to be desplayed
     eg endpoint?count=3   only three items will be displayed
     '''
     page_size_query_param = 'count'
     '''
     max_size specificies the maximum amount of items that can be displayed
     '''
     max_page_size = 5
     page_query_param = 'p'