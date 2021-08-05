from django.forms import ModelForm
from .models import user
from .models import product
from .models import login
from .models import order
class wishlist(ModelForm):
    class Meta:
        model = user
        fields = '__all__'