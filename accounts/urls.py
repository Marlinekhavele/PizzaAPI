from accounts.views import CustomerViewSet,StaffViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'staffs', StaffViewSet, basename='staff')
router.register(r'customers', CustomerViewSet, basename='customer')
urlpatterns = router.urls