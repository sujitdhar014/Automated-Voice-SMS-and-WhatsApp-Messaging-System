
from django.contrib import admin
from django.urls import path
from whatsapp import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message', views.message),    
    # path('messagecom', views.messagecom, name='message_template'),
    path('hello', views.index, name='index'),
     path('send-message/',views.send_message, name='send_message'),
]
