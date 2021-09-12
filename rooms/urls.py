from django.urls import path
from . import views

app_name = "rooms"

urlpatterns = [
    path("list/",views.ListRoomsView.as_view()),
    path("<int:pk>/",views.SeeRoomView.as_view()),
    #path("<int:jhkim>/",views.SeeRoomView.as_view()),
    #pk 라는 키워드가 있기에 restapi 가 알아먹음
    #이거 고칠려면 listapiview,retreive api view  의 lookup_url_kwarg
]
