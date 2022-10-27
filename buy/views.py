from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import permissions
# from .models import Order
from .serializers import OrderSerializer
from rest_framework.decorators import action


class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer


class UserOrderList(APIView):

    def get(self, request):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)

    @action(['DELETE'], detail=True)
    def delete_buy(self, request, pk):
        movie = self.get_object()
        user = request.user
        if not user.order.filter(movie=movie).exists():
            return Response('You Didn\'t Buy This!', status=400)
        user.order.filter(movie=movie).delete()
        return Response('Your Buy is Deleted!', status=204)
