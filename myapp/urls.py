#from django.conf.urls import url
#from .views import UploadCouponView

#urlpatterns = [
#    url('upload/', UploadCouponView.as_view(), name='myapp-upload')
    
     
#]

from .views import CSVUploadHandler
from django.urls import path

urlpatterns = [
    path('upload/',CSVUploadHandler.as_view(), name='myapp-upload')    
]