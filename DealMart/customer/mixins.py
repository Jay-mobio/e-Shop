from django.core.exceptions import PermissionDenied

class CheckCustomerGroup:
    def dispatch(self,request, *args, **kwargs):
        if request.user.groups.filter(name="Customer").exists():
            return True
        else:
            raise PermissionDenied