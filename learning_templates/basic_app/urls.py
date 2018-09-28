from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
# KEY THINGS THE NAME YOU MENTION

app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other')
]
