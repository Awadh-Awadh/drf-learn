from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
     '''
     page size gives the amount of items to be displayed
     
     '''
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

     '''
     page query helps in accessing the page
     e.g p=1 ---> access page
     '''
     page_query_param = 'p'