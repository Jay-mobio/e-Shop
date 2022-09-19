from django.core.exceptions import PermissionDenied

class CheckCustomerGroup:
    def dispatch(self,request, *args, **kwargs):
        if request.user.groups.filter(name="Product Owner").exists():
            raise PermissionDenied
        else:
            return super().dispatch(request,*args,**kwargs)