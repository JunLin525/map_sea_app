from django.urls import path

from .views import BookAPIView, BookAPIViews
from .views import BookDetailAPIVIEW, BookDetailAPIVIEWs
urlpatterns = [
    path('', BookAPIView.as_view(), name='book_list'),
    path('detail/<int:pk>', BookDetailAPIVIEW.as_view(), name='book_detail'),
    path('w/', BookAPIViews.as_view(), name="new-api"),
    path('w/<uuid:pk>', BookDetailAPIVIEWs.as_view(), name="new_api_detail")
]
