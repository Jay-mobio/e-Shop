from django.core.exceptions import PermissionDenied
from customer.models import Cart

class CheckCart:
    def dispatch(self,request, *args, **kwargs):
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        if len(cart) > 0:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied