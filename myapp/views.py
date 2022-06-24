from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from myapp.models import Coupon
from myapp.serializers import SaveCouponSerializer, CouponUploadSerializer
from rest_framework import status

class UploadCouponView(generics.CreateAPIView):
    serializer_class = CouponUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coupons = serializer.validated_data['Coupons']
        reader = pd.read_csv(coupons)
        for _, row in reader.iterrows():
            new_coupon = Coupon(
                       code= row["code"],
                       description= row['description'],
                       amount= row["amount"],
                       amount_type= row["amount_type"]
                       )
            new_coupon.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)