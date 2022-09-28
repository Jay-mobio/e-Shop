"""MIXIN"""
from django.core.exceptions import PermissionDenied

class CheckCustomerGroup:
    """CHECK CUSTOMER GROUP"""
    def dispatch(self,request, *args, **kwargs):
        """DISPATCH"""
        if request.user.groups.filter(name="Product Owner").exists():
            raise PermissionDenied
        else:
            return super().dispatch(request,*args,**kwargs)
