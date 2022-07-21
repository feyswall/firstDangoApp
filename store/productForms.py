from django import forms
from django.http import HttpResponse
from pkg_resources import require
from .models import Collection, Promotion


class createProductForm(forms.Form):

    queryset = Collection.objects.values_list('id', 'title')
    promoqueryset = Promotion.objects.values_list('id', 'discount')
    COLLECTIONS = list(queryset)
    PROMO = [('2', '1norder'), ('3', 'another')]

    tittle = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'some_class',
               'id': 'some_id'}))

    description = forms.CharField(max_length=1000, label='description', help_text='description'
        , widget=forms.CharField())
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


# 0624928766
