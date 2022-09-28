"""CHECK CART MIXIN"""
from django.core.exceptions import PermissionDenied
from customer.models import Cart

class CheckCart:
    """CART CHECKING"""
    def dispatch(self,request, *args, **kwargs):
        """DISATCH"""
        cart = Cart.objects.filter(created_by = request.user,is_active=True)
        if len(cart) > 0:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied
