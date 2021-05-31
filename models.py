from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ClientProduct(models.Model):
    product_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    product_code = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.product_name


class ClientName(models.Model):
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_product_id = models.ForeignKey(ClientProduct, null=True, blank=True ,on_delete=models.PROTECT)

    def __str__(self):
        return self.client_name


class Location(models.Model):
    location_name = models.CharField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.location_name
    

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255, null=True, blank=True,)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.username


class Status(models.Model):
    status_phase = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.status_phase



class OrderDetail(models.Model):
    client_name = models.ForeignKey(ClientName, on_delete=models.PROTECT)
    # client_product_name = models.ForeignKey(ClientProduct, to_field='product_name', on_delete=models.PROTECT)
    client_product_id = models.ForeignKey(ClientProduct, on_delete=models.PROTECT)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)
    build_location = models.ForeignKey(Location, on_delete=models.PROTECT, unique=True) # check unique in this if required and foreign key
    order_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    current_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    priority =  models.CharField(max_length=255, null=True, blank=True)
    status = models.ForeignKey(Status, null=True, blank=True, on_delete=models.PROTECT)
    file_preview = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.client_product_name



class Board(models.Model):
    client_name = models.ForeignKey(ClientName, on_delete=models.PROTECT, null=True, blank=True)
    product_code = models.ForeignKey(ClientProduct, on_delete=models.PROTECT, null=True, blank=True)
    punch_no = models.CharField(max_length=255, null=True, blank=True)
    size = models.CharField(max_length=255, null=True, blank=True)
    ups = models.CharField(max_length=255, null=True, blank=True)
    design = models.CharField(max_length=255, null=True, blank=True)
    tuck_in_flap = models.CharField(max_length=255, null=True, blank=True)
    collar_flap = models.CharField(max_length=255, null=True, blank=True)
    cam_pam = models.CharField(max_length=255, null=True, blank=True)
    plate_maker = models.CharField(max_length=255, null=True, blank=True)
    plate_maker_code = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        pass


class LogTable(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT)
    client_name = models.ForeignKey(ClientName, on_delete=models.PROTECT)
    client_product_id = models.ForeignKey(ClientProduct, on_delete=models.PROTECT)
    order_detail = models.ForeignKey(OrderDetail, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        pass


class CompletedOrder(models.Model):
    client_name = models.ForeignKey(ClientName, on_delete=models.PROTECT)
    client_product_id = models.ForeignKey(ClientProduct, on_delete=models.PROTECT)
    build_location = models.ForeignKey(Location, on_delete=models.PROTECT)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    date_completed = models.DateTimeField(auto_now_add=True, null=True)
    file_preview = models.CharField(max_length=255, null=True)

    def __str__(self):
        pass
