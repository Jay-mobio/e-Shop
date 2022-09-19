from django.views import View
from products.models import SubCategory
from django.http import JsonResponse


class ChooseSubCategory(View):

    def get(self,request, id):
        sub_category = SubCategory.objects.filter(category__id = id).all()
        data = sub_category.values('id','name')
        return JsonResponse({'message':True,'data':list(data)}, status = 200)