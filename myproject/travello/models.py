from django.db import models

# Create your models here.

class Destination:
    id : int
    name : str
    destination: str
    image: str
    desc: str
    price: int
