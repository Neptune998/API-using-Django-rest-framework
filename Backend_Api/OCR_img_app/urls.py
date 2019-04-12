from django.urls import path

from OCR_img_app.views import ImageView

app_name = 'OCR_img_app'
urlpatterns = [
       path('image/', ImageView.as_view(), name='image'),

]
