"""GETTING PRODUCT SUBCATEGROIES"""
from django.views import View
from django.http import JsonResponse
from products.models import SubCategory

class ChooseSubCategory(View):
    """PRODUCT SUBCATEGORIES"""
    def get(self,id):
        """GETTING SUBCATEGORIES FORM RELATED CATEGORY"""
        sub_category = SubCategory.objects.filter(category__id = id).all()
        data = sub_category.values('id','name')
        return JsonResponse({'message':True,'data':list(data)}, status = 200)
