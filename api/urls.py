from django.urls import path, include
from .views import RegisterView, UserViewSet, JournalViewSet
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'journals', JournalViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]