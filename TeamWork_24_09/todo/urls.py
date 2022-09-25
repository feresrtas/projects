

from django.urls import path, include
from .views import TodoMVS , CategoryListCreate , CategoryUpdateDelete
from rest_framework import routers

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register("todos",TodoMVS)

urlpatterns = [
    path('list',CategoryListCreate.as_view()),
    path('list/<int:id>',CategoryUpdateDelete.as_view())
]
urlpatterns +=router.urls