import django_tables2 as tables
from rango.models import Category

class CategoryTable(tables.Table):
    class Meta:
        model = Category
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}