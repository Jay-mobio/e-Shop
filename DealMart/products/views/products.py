from products.models import Category,SubCategory
from products.forms import AddProductForm
from django.views.generic import FormView
from django.shortcuts import render,redirect
from products.models import Products
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AddProduct(FormView):
    template_name = "products/add_product.html" 
    form_class = AddProductForm
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name,{'form':form})



    def post(self,request):
        # import pdb;pdb.set_trace()
        # print(request.FILES)
        form  = AddProductForm(request.POST,request.FILES)
        
        # print(images)


        if form.is_valid(): 
            images = request.FILES['image']
            if images == None:
                images="static/images/default.jpg"
            name = request.POST.get('name')
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            sub_category_name = request.POST.get('sub_category')
            sub_category = SubCategory.objects.get(name=sub_category_name)
            price = request.POST.get('price')
            discription  = request.POST.get('discription')
            created_by = request.user
            Products.objects.create(name=name,category=category,price=price,discription=discription,created_by=created_by,sub_category=sub_category,image=images)
            return redirect('products:dashboard')
        return render(request,self.template_name,{'form':form})

    # def get(self,request):
    #     # import pdb;pdb.set_trace()
    #     # print(request.FILES)
    #     form  = AddProductForm(request.POST,request.FILES)
    #     return render(request,self.template_name,{'form':form})        
        

# class ProductImage(FormView):
