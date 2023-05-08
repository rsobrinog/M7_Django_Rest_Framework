from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer




"""
Decorators, Response i api_view extret de: https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
"""
@api_view(['GET'])
def getProducts(request):
    renderer_classes = [TemplateHTMLRenderer]

    list = [
        {'lista 1':'Mylist 1'},
        {'lista 2':'Mylist 2'},
        {'lista 3':'Mylist 3'},
        {'lista 4':'Mylist 5'}
    ]
    context = {'list': list}
    return Response(context, template_name='products.html', content_type='text/html')
