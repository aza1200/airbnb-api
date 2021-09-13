from rest_framework import viewsets
from .models import Room
from .serializers import BigRoomSerializer

class RoomViewset(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer

    # view set 은 빠르지만 안쓸거임
    # 왜냐하면 viewset 이 하고있는 모든것들을 어떻게 하는지 알아보자
    # 제대로 배워보장
    # cbv ,fbv

