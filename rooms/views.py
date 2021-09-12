from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer,BigRoomSerializer

# @api_view(["GET"])
# def list_rooms(request):
#     rooms = Room.objects.all()
#     serialized_rooms = RoomSerializer(rooms,many = True)
#     return Response(data=serialized_rooms.data)

# class ListRoomsView(APIView):
#
#     def get(self,request):
#         rooms = Room.objects.all()
#         serializer = RoomSerializer(rooms,many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         pass

#오직 하나의 뷰만 페이지 사이즈를 바꾸고 싶을떄???
# 강의 1.4 참조
class ListRoomsView(ListAPIView):
    #많은 것을 커스터마이징할 필요가 없을때의 뷰
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
    #lookup_url_kwarg = "jhkim"