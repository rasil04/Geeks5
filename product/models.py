from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    @property
    def products_count(self):
        return self.products.count()

    @property
    def products_list(self):
        return [product.title for product in self.products.all()]

    def str(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    price = models.FloatField(default=0)
    category = models.ManyToManyField('Category', related_name='products')
    tags = models.ManyToManyField('Tag', blank=True)

    @property
    def rating(self):
        stars = [review.start for review in self.reviews.all()]
        return round(sum(stars) / len(stars), 2)

    @property
    def category_name(self):
        name_category = [category.name for category in self.category.all()]
        return name_category

    def str(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, '*' * i) for i in range(1, 6))
    product = models.ForeignKey('Product', on_delete=models.CASCADE,
                                related_name='reviews', null=True)
    stars = models.IntegerField(choices=CHOICES, null=True)
    text = models.TextField(blank=True, null=True)

    @property
    def product_title(self):
        return self.product.title

    def str(self):
        return self.text


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name