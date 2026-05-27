from django.contrib import admin

from .models import (
    AuditLog,
    DataSource,
    Facility,
    IngestionBatch,
    NormalizedActivity,
    RawRecord,
    Tenant,
    ValidationIssue,
)


admin.site.register(Tenant)
admin.site.register(Facility)
admin.site.register(DataSource)
admin.site.register(IngestionBatch)
admin.site.register(RawRecord)
admin.site.register(NormalizedActivity)
admin.site.register(ValidationIssue)
admin.site.register(AuditLog)