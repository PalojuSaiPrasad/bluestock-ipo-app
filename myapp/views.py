
from myapp.models import IPO
from rest_framework import generics
from .serializers import IPOSerializer

# IPOViewList class is used to perform view operation


class IPOViewList(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer


# IPOCreate class is used to perform view operation

class IPOCreate(generics.CreateAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer


# IPOUpdate class is used to perform view operation

class IPOUpdate(generics.UpdateAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer


# IPODelete class is used to perform view operation

class IPODelete(generics.DestroyAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
