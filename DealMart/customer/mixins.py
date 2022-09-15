from django.core.exceptions import PermissionDenied

class CheckCustomerGroup:
    def dispatch(self,request, *args, **kwargs):
        if request.user.groups.filter(name="Customer").exists():
            return super().dispatch(request,*args,**kwargs)
        else:
            raise PermissionDenied