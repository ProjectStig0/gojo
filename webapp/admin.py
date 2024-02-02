from django.contrib import admin

# Register your models here.
from .models import Bag
from .models import ProductInventory
from .models import Group
from .models import Brand

admin.site.register(Bag)
admin.site.register(ProductInventory)
admin.site.register(Group)
admin.site.register(Brand)

