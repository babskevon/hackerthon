from django.db import models

# Create your models here.


regions = [
    ('Central', "Central")
]
cities = [
    ("Banda", "Banda")
]
villages = [
    ("Lubawo", "Lubawo")
]
streets = [
    ("Luwum Street", "Luwum Street")
]
class Agent(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, choices=regions)
    city = models.CharField(max_length=255, choices=cities)
    village = models.CharField(max_length=255, choices=villages, null=True)
    street = models.CharField(max_length=255, choices=streets, null=True)
    contact = models.CharField(max_length=13)
    email = models.EmailField(null=True)

    def __str__(self) -> str:
        return self.name


# class Addres(models.Model):
#     region = models.CharField(max_length=255, choices=regions)
#     city = models.CharField(max_length=255, choices=cities)
#     village = models.CharField()


class ProductOwner(models.Model):
    name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    contact = models.CharField(max_length=13)
    status = models.BooleanField(default=False)


class Message(models.Model):
    owner = models.ForeignKey(ProductOwner, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class Pick(models.Model):
    # order_no = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, choices=regions)
    city = models.CharField(max_length=255, choices=cities)
    village = models.CharField(max_length=255, choices=villages, null=True)
    street = models.CharField(max_length=255, choices=streets)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)


