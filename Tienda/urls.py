
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from zapatillas.views import plantilla1, registrarse,signout,signin,create_task,create_zapatilla, task_detalle, listado, task_eliminar, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', plantilla1, name="task"),
    path('listado/', listado, name="listado"),
    path('Registro/', registrarse, name="registro"),
    path('create/task/', create_task, name='create_task'),
    path('create/<int:task_id>/', task_detalle, name='task_detalle'),
    path('create/<int:task_id>/delete/', task_eliminar, name='task_delete'),
    path('logout/', signout, name='logout'),
    path('signin/', signin, name='signin'),
    path('create/zapatilla/', create_zapatilla, name='create_zapatilla'),
    path('about/', about, name='about')



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)