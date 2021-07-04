from django.urls.resolvers import URLPattern
from django.urls import path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("nearest_dea/", views.nearest_dea, name="nearest_dea"),
    # path("listado/", views.listado, name ="listado"),
    path("suggestions/", views.suggestions, name="suggestions"),
    path("login/", views.login, name="login"),
    path("maps/", views.map, name = "map"),
    path("informationsent/", views.informationsent, name="informationsent")
]


# urlpatterns += staticfiles_urlpatterns()