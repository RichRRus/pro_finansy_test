from django.urls import include, path
from rest_framework import routers

from poll import views

router = routers.DefaultRouter()
router.register('', views.PollViewSet)

urlpatterns = [
    path('polls/', include(router.urls)),
]
