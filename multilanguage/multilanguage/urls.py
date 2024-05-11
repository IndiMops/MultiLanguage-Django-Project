from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("", views.MainPageViews.as_view(), name = "main_page"),
    path("", include("book_catalogue.urls"))
]

urlpatterns += i18n_patterns(
    path("", views.MainPageViews.as_view(), name="main_page"),
    path("", include("book_catalogue.urls"))
)
