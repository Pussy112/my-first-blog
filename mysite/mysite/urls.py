from django.contrib import admin
from django.urls import path, include
"""ddd"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
