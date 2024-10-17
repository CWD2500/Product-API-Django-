from django.shortcuts import render , get_object_or_404
from .models import Product
from rest_framework.decorators  import api_view
from rest_framework.response  import Response
from .serializers  import ProductSerializer
from .fillter  import  ProductFillter
from rest_framework.pagination import PageNumberPagination
# Create your views here.



@api_view(['GET'])
def get_product(request):
	filters = ProductFillter(request.GET , queryset=Product.objects.all().order_by('id'))
	count  = filters.qs.count()
	resPage = 1
	paginations = PageNumberPagination()
	paginations.page_size = resPage
	# products  = Product.objects.all()
	queryset  =paginations.paginate_queryset(filters.qs , request)
	serializers = ProductSerializer(queryset , many=True)
	# serializers = ProductSerializer(filters.qs , many=True)
	print(serializers)
	return Response({"Products":serializers.data})
	

@api_view(['GET'])
def get_by_id_product(request,pk):
	products = get_object_or_404(Product , id=pk)
	serializers = ProductSerializer(products , many=False)
	# print(serializers)
	return Response({"Products":serializers.data})
 