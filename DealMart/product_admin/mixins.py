"""GROUP CHECK MIXIN"""
from django.core.exceptions import PermissionDenied

class CheckProductOwnerGroup:
    """CHECK PRODUCT OWNER GROUP OF USER"""
    def dispatch(self,request, *args, **kwargs):
        """DISPATCH"""
        if request.user.groups.filter(name="Product Owner").exists():
            return super().dispatch(request,*args,**kwargs)

        raise PermissionDenied
