from django.core.exceptions import PermissionDenied

class CheckProductOwnerGroup:
    def dispatch(self,request, *args, **kwargs):
        if request.user.groups.filter(name="Product Owner").exists():
            return True
        else:
            raise PermissionDenied