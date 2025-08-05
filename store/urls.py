from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProductView, CartView, WishlistView, OrderView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', ProductView , basename='products')
router.register('cart', CartView , basename='cart')
router.register('wishlist', WishlistView , basename='wishlist')
router.register('orders', OrderView , basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    # AUTH
    # LOGIN
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # TO REFRESH THE TOKEN
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # REGISTER
    path('register/', RegisterView.as_view(), name='register')
]
