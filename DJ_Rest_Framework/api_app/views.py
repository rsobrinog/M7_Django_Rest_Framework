from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


"""
Decorators, Response i api_view extret de: https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
"""
@api_view(['GET'])
def getProducts(request):

    list = [
        {'lista 1':'Mylist 1'},
        {'lista 2':'Mylist 2'},
        {'lista 3':'Mylist 3'},
        {'lista 4':'Mylist 5'}
    ]

    return Response(list)
