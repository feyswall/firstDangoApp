from django import forms
from django.http import HttpResponse
from pkg_resources import require
from .models import Collection, Promotion


class createProductForm(forms.Form):

    queryset = Collection.objects.values_list('id', 'title')
    promoqueryset = Promotion.objects.values_list('id', 'discount')
    COLLECTIONS = list(queryset)
    PROMO = [('2', '1norder'), ('3', 'another')]

    tittle = forms.CharField(max_length=255)

    description = forms.CharField(widget=forms.Textarea())
    
    inventory = forms.IntegerField()
    
    last_update = forms.DateField(
        widget=forms.SelectDateWidget(years=range(1500, 3000)))
    
    promotion = forms.ChoiceField(
        label="promotions",
        widget=forms.RadioSelect,
        choices=PROMO)

    collection = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=COLLECTIONS,
    )

    price = forms.IntegerField()


# 0624928766

# fields to Learn are:
# > input field
# > radio
# > checkbox
# > text field
# > multiple selection
# > selection