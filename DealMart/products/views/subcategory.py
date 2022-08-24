import json
from django.views import View
from django.shortcuts import render
from products.models import SubCategory
from django.http import JsonResponse
from django.core import serializers


class ChooseSubCategory(View):

    def get(self,request, id):
        sub_category = SubCategory.objects.filter(category__id = id).all()
        # sub_category = serializers.serialize('json', sub_category)
        data = sub_category.values('id','name')
        # print(sub_category_names,'----------------')
        # jason_dict = serializers.serialize('json', sub_category_names)
        # for i in sub_category:print(i)
        # print(sub_category)
        return JsonResponse({'message':True,'data':list(data)}, status = 200)