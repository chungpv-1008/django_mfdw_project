from django.urls import path

from pages import views


urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.index, {"pagename": ""}, name="home"),
    path("contact", views.contact, name="contact"),
    path("<str:pagename>", views.index, name="index"),
]
