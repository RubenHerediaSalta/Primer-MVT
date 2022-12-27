from django.urls import path

from family.views import list_family, add_familiar

urlpatterns = [
    path('list-family/', list_family),
    path('add-family/', add_familiar),

]