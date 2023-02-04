from django.contrib import admin

from zapatillas.models import Project, Zapatillas, Entrega, Task


admin.site.register(Project)
admin.site.register(Zapatillas)
admin.site.register(Entrega)
admin.site.register(Task)
