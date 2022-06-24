from django.conf.urls import url
from .views import UploadCouponView


urlpatterns = [
    
    url('upload/', UploadCouponView.as_view(), name='myapp-upload')
    
     
]


