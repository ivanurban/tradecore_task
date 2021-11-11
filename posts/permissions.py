from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        #Read only allowed 
        if request.method in permissions.SAFE_METHODS:
            return True


        # write permission to author only
        return obj.author ==request.user