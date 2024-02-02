from django.db import models

class Group(models.Model):
	name = models.CharField(max_length = 300, null = True)
	description = models.TextField(blank = True)
	datetime = models.DateTimeField(null = True)
	
	def __str__(self):
		return self.name

class Bag(models.Model):
	brandname = models.CharField(max_length = 300, null = True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	group = models.ManyToManyField(Group, related_name = 'bags')

	def __str__(self):
		return self.brandname

class ProductInventory(models.Model):
	bag = models.ForeignKey(Bag, on_delete = models.SET_NULL, null = True)
	productname = models.CharField(max_length = 300, null = True)
	description = models.TextField(blank = True)
	photo = models.ImageField(upload_to = 'albums/', blank = True)

	def __str__(self):
		return self.productname

class Brand(models.Model):
	model = models.CharField(max_length = 300, null = True)
	quality = models.CharField(max_length = 300, null = True)
	product = models.CharField(max_length = 300, null = True)
	description = models.TextField(blank = True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	photo = models.ImageField(upload_to = 'albums/', blank = True)

	def __str__(self):
		return self.model
		

