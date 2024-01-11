# Import necessary modules from Django
from django.urls import path
from . import views

# Define urlpatterns for mapping URL patterns to views
urlpatterns = [
    # Public views
    path('', views.index, name='index'),  # Home page
    path('cart/', views.cart, name='cart'),  # Cart page
    path('menu/', views.menu, name='menu'),  # Menu page
    path('myorders/', views.my_orders, name='my_orders'),  # User's order history page
    path('profile/', views.profile, name='profile'),  # User profile page
    path('contact/', views.cont, name='contact'),
    path('class_surbhi/', views.surbhi, name='cbs'),
    path('news_event/', views.news, name='n&e'),
    path('about/', views.about, name='about'),
    path('food/search/', views.food_search, name='food_search'),

    # Admin dashboard views
    path('dashboard/admin/users/', views.users_admin, name='users_admin'),  # Admin: User management
    path('dashboard/admin/orders/', views.orders_admin, name='orders_admin'),  # Admin: Order management
    path('dashboard/admin/foods/', views.foods_admin, name='foods_admin'),  # Admin: Food management
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),  # Admin dashboard
    path('dashboard/admin/sales/', views.sales_admin, name='sales_admin'),  # Admin: Sales management

    # Admin views for adding and editing entities
    path('dashboard/admin/users/add_user/', views.add_user, name='add_user'),  # Admin: Add new user
    path('dashboard/admin/foods/add_food/', views.add_food, name='add_food'),  # Admin: Add new food
    path('dashboard/admin/sales/add_sales/', views.add_sales, name='add_sales'),  # Admin: Add new sale
    path('dashboard/admin/foods/editFood/<int:foodID>/', views.edit_food, name='edit_food'),  # Admin: Edit food details
    path('dashboard/admin/foods/foodDetails/<int:foodID>/', views.food_details, name='food_details'),  # Admin: View food details
    path('dashboard/admin/sales/editSale/<int:saleID>/', views.edit_sales, name='edit_sales'),  # Admin: Edit sale details

    # Admin actions on orders
    path('dashboard/admin/orders/confirm_order/<int:orderID>/', views.confirm_order, name='confirm_order'),  # Admin: Confirm order
    path('dashboard/admin/orders/confirm_delivery/<int:orderID>/', views.confirm_delivery, name='confirm_delivery'),  # Admin: Confirm delivery

    # User actions
    path('delete_item/<int:ID>/', views.delete_item, name='delete_item'),  # Delete item from cart
    path('add_deliveryBoy/<int:orderID>/', views.add_deliveryBoy, name='add_deliveryBoy'),  # Assign delivery boy to an order
    path('placeOrder/', views.placeOrder, name='placeOrder'),  # Place a new order
    path('addTocart/<int:foodID>/<int:userID>/', views.addTocart, name='addTocart'),  # Add item to the cart

    # Delivery boy dashboard
    path('dashboard/delivery_boy/', views.delivery_boy, name='delivery_boy'),  # Delivery boy dashboard
]
