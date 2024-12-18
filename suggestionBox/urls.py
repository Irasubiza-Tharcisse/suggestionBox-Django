from django.urls import path

from . import views
urlpatterns=[
  path('',views.suggestion_view,name='suggestion'),
  path('success/',views.success_view,name='success'),
]