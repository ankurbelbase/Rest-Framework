# Rest-Framework
small example of restframe work


Installation

Install using pip, including any optional packages you want...

pip install djangorestframework

Add 'rest_framework' to your INSTALLED_APPS setting.

INSTALLED_APPS = (
    ...
    'rest_framework',
)


In urls.py add

from rest_framework import routers
from restapiapp import views

router = routers.DefaultRouter()
router.register(r'event', views.EventApiView)


urlpatterns = [
    ...
    url(r'^', include(router.urls))
    
]

and you're ready to go....
