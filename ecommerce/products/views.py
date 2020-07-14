from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *


# Create your views here.


class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = 'product_list_view.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = 'product_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # context['abc'] = 123
        print(context)
        return context

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     instance = Product.objects.get_by_id(pk)
    #     print(instance)
    #     if instance is None:
    #         raise Http404("Product Doesn't exist")
    #     return instance

    def get_queryset(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(pk=pk)
    # except Product.DoesNotExist:
    #     raise Http404('Product Does not Exist')

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, 'product_detail_view.html', context)


class ProductFeaturedListView(ListView):
    template_name = 'product_list_view.html'

    def get_queryset(self):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.features()
    template_name = 'featured_detail.html'

    # def get_queryset(self):
    #     request = self.request
    #     return Product.objects.all().featured()


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail_view.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not Found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('Hmmm')
        return instance
