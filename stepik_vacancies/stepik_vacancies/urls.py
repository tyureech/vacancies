"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from vacancies import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name='home'),
    path('vacancies/', views.VacanciesAll.as_view(), name='vacancies'),
    path('vacancies/<int:id>/', views.Vacancy.as_view(), name='vacancy'),
    path('vacancies/cat/<str:direction>/', views.VacanciesDirection.as_view(), name='vacancies_direction'),
    path('companies/<int:id>', views.Company.as_view(), name='company'),
    path('vacancies/<int:id>/send', views.SendVacancy.as_view(), name='send'),
    path('', include('authentication.urls')),
    path('', include('my_company.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = views.custom_handler404
handler500 = views.custom_handler500
