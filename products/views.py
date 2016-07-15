from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# Create your views here.

from .models import Product

class ProductListView(ListView):
	model = Product
	queryset = Product.objects.all().active()

	def get_context_data(self,*args,**kwargs):
		context = super(ProductListView, self).get_context_data(*args,**kwargs)
		context["now"] = timezone.now()
		return context

class ProductDetailView(DetailView):
	model = Product
	#template_name = "product.html"



def product_detail_view_func(request,id):
	
	product_instance = get_object_or_404(Product,id=id)
	try:
		product_instance = get_object_or_404(id=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404
	product_instance = Product.objects.get(id=id)
	template = "products/product_detail.html"
	context = {
	"object":product_instance
	}
	return render(request,template,context) 