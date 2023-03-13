"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from categories.api.router import router_category
from products.api.router import router_product
from users.api.router import router_user
from views.api.routers import router_view

schema_view = get_schema_view(
    openapi.Info(
        title="Zebrands API",
        default_version="v1",
        description="Zebrand API for manage Users 👦/👧 and products 🛏️🧳",
        contact=openapi.Contact(email="javieramayapat@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # documentation
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    # users
    path("api/v1/", include(router_user.urls)),
    path("api/v1/", include("users.api.router")),
    # categories
    path("api/v1/", include(router_category.urls)),
    # products
    path("api/v1/", include(router_product.urls)),
    # views
    path("api/v1/", include(router_view.urls)),
]
