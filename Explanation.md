# explanations

## apps engine modular installed

[module_engine/views.py](https://github.com/ridwaanhall/django-dev-test/blob/bb13c4fc0ab70d0098cb4e653fd267951b60a08c/module_engine/views.py)

- install
- upgrade
- uninstall

## apps example module

### if installed, it can accessed product page

```python
def check_module_installed():
    """Check if this module is installed and enabled"""
    try:
        module = ModuleRegistry.objects.get(name='product_module')
        return module.installed and module.enabled
    except ModuleRegistry.DoesNotExist:
        return False
```

### class product

```python
class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=50, unique=True) # UUID
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- name
- barcode
- price
- stock

### role

| Username | Role    | Password  |
|----------|---------|-----------|
| admin    | Manager | admin     |
| user     | User    | Project123|

- manager CRUD
- user CRU
- public R

### valitadtion

- if D, are u sure to delete? then if yes delete, else cancel

## if uninstall project module, the product page cant be access

- uninstall

## every changes can handle with upgrade button

## ERD FLowChart
