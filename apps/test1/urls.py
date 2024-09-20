from django.urls import path
from .views import RegView,ItemView

urlpatterns = [
    path('regview/',RegView.as_view(),name='regview'),
    path('item/',ItemView.as_view(),name='item'),
    path('item/<int:id>/',ItemView.as_view(),name='item'),
    
]
