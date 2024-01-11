# Import necessary modules from Django
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Define the Customer model
class Customer(models.Model):
    # Define constants for customer status
    pending = 'Pending'
    verified = 'Verified'
    
    STATUS = (
        (pending, pending),
        (verified, verified),
    )

    # Define fields for the Customer model
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length=10)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name

# Define the Staff model
class Staff(models.Model):
    # Define constants for staff roles
    admin = 'Admin'
    deliveryboy = 'Delivery Boy'
    chef = 'Chef'

    ROLES = (
        (admin, admin),
        (chef, chef),
        (deliveryboy, deliveryboy),
    )

    # Define fields for the Staff model
    staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length=10)
    email = User.email
    salary = models.IntegerField()
    role = models.CharField(max_length=30, choices=ROLES)

    def __str__(self):
        return self.staff_id.first_name + " " + self.staff_id.last_name

# Define the Order model
class Order(models.Model):
    # Define constants for order status
    pending = 'Pending'
    completed = 'Completed'

    STATUS = (
        (pending, pending),
        (completed, completed),
    )

    # Define constants for payment methods
    cod = 'Cash On Delivery'
    card = 'Card Payment'
    upi = 'UPI Payment'

    PAYMENT = (
        (cod, cod),
        (card, card),
        (upi, upi),
    )

    # Define constants for order type
    pickup = 'PickUp'
    delivery = 'Delivery'

    TYPE = (
        (pickup, pickup),
        (delivery, delivery),
    )

    # Define fields for the Order model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_timestamp = models.CharField(max_length=100, blank=True)
    delivery_timestamp = models.CharField(max_length=100, blank=True)
    payment_status = models.CharField(max_length=100, choices=STATUS)
    delivery_status = models.CharField(max_length=100, choices=STATUS)
    if_cancelled = models.BooleanField(default=False)
    total_amount = models.IntegerField()
    payment_method = models.CharField(max_length=100, choices=PAYMENT)
    location = models.CharField(max_length=200, blank=True, null=True)
    delivery_boy = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True, blank=True)

    # Define methods to confirm order and delivery
    def confirmOrder(self):
        self.order_timestamp = timezone.localtime().__str__()[:19]
        self.payment_status = self.completed
        self.save()

    def confirmDelivery(self):
        self.delivery_timestamp = timezone.localtime().__str__()[:19]
        self.delivery_status = self.completed
        self.save()

    def __str__(self):
        return self.customer.__str__()

# Define the Food model
class Food(models.Model):
    # Define constants for food course and status
    INDIAN = 'Indian Food'
    SOUTH = 'South Food'
    GUJARATI = 'Gujarati Food'
    PUNJABI = 'Punjabi Food'
    FAST = 'Fast Food'

    COURSE_CHOICES = (
        (INDIAN, 'Indian Food'),
        (SOUTH, 'South Food'),
        (GUJARATI, 'Gujarati Food'),
        (PUNJABI, 'Punjabi Food'),
        (FAST, 'Fast Food'),
    )

    DISABLED = 'Disabled'
    ENABLED = 'Enabled'

    STATUS_CHOICES = (
        (DISABLED, 'Disabled'),
        (ENABLED, 'Enabled'),
    )

    # Define fields for the Food model
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES, default=INDIAN)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ENABLED)
    content_description = models.TextField()
    base_price = models.FloatField()
    sale_price = models.FloatField(default=base_price)
    discount = models.DecimalField(default=0, decimal_places=2, max_digits=5)
    image = models.FileField(blank=True, null=True)
    num_order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Define the Comment model
class Comment(models.Model):
    # Define fields for the Comment model
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)

# Define the Data model
class Data(models.Model):
    # Define fields for the Data model
    date = models.DateField()
    sales = models.IntegerField()
    expenses = models.IntegerField()

# Define the OrderContent model
class OrderContent(models.Model):
    # Define fields for the OrderContent model
    quantity = models.IntegerField(default=1)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

# Define the Cart model
class Cart(models.Model):
    # Define fields for the Cart model
    quantity = models.IntegerField(default=1)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Define the DeliveryBoy model
class DeliveryBoy(models.Model):
    # Define fields for the DeliveryBoy model
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_boy = models.ForeignKey(Staff, on_delete=models.CASCADE)
