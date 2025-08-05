from .models import User, Product, CartItem, Wishlist, Order, OrderItem
from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permisssions import IsCustomer, IsManager
from rest_framework.decorators import action
from django.db.models import Sum, Count
from rest_framework.response import Response

# REGISTER VIEW
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# PRODUCT VIEW
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrive'] :
            return [AllowAny()]
        return [IsAuthenticated(), IsManager()]

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated, IsManager])
    def sales_report(self, request):
        report = Product.objects.order_by('-times_bought')
        data = [
            {'name': p.name, 'times_bought': p.times_bought, 'category': p.category}
            for p in report
        ]
        return Response(data)

# CART VIEW
class CartView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsCustomer]
    serializer_class = CartSerializer

    def get_queryset(self):
        return CartItem.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

# WISHLIST VIEW
class WishlistView(viewsets.ModelViewSet):
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Wishlist.objects.filter(user = self.request.user)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

# ORDER VIEW
class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_queryset(self):
        return Order.objects.filter(user = self.request.user)

    def perform_create(self, serializers):
        cart_items = CartItem.objects.filter(user=self.request.user)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty.")

        total = sum(item.product.price * item.quantity for item in cart_items)
        order = serializers.save(user=self.request.user, total_price=total)

        order_items = []
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                product=cart_item.product,
                quantity=cart_item.quantity
            )
            order_items.append(order_item)


            cart_item.product.stock -= cart_item.quantity
            cart_item.product.times_bought += cart_item.quantity
            cart_item.product.save()

        order.items.set(order_items)

        cart_items.delete()
