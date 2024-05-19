from django.contrib import admin
from .models import About
from .models import ServiceIntro
from .models import Services
from .models import Clients
from .models import QuickFacts
from .models import WhoWeAre
from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(About, ImportExportModelAdmin)
admin.site.register(ServiceIntro, ImportExportModelAdmin)
admin.site.register(Services, ImportExportModelAdmin)
admin.site.register(Clients, ImportExportModelAdmin)
admin.site.register(QuickFacts, ImportExportModelAdmin)
admin.site.register(WhoWeAre, ImportExportModelAdmin)

