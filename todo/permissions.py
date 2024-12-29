from rest_framework import permissions

class IsTodoOwnerorIsAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #if(request.user.id == obj.user.id):
            #return True
        if request.user.is_superuser == True:
            return True
        else:
            return False