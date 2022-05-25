from django.urls import path
from . import views

# urlpatterns = [
#     path('sports', views.news_view)
# ]

#przkanie argumentu do dynamicznego url:
urlpatterns = [
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view),
]

