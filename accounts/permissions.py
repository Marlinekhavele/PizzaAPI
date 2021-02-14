class IsOwnerStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        staff = Staff.objects.get(pk=view.kwargs['staff'])
        return staff.owner == request.user
