from django.conf import settings
from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="facilities")
    facility_code = models.CharField(max_length=100)
    facility_name = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ("tenant", "facility_code")

    def __str__(self):
        return f"{self.facility_code} - {self.facility_name}"


class DataSource(models.Model):
    SOURCE_TYPES = [
        ("SAP", "SAP"),
        ("UTILITY", "Utility Electricity"),
        ("TRAVEL", "Corporate Travel"),
    ]

    INGESTION_METHODS = [
        ("CSV_UPLOAD", "CSV Upload"),
        ("API_PULL", "API Pull"),
        ("MANUAL", "Manual Entry"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="data_sources")
    source_type = models.CharField(max_length=50, choices=SOURCE_TYPES)
    name = models.CharField(max_length=255)
    ingestion_method = models.CharField(max_length=50, choices=INGESTION_METHODS, default="CSV_UPLOAD")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.name}"


class IngestionBatch(models.Model):
    STATUS_CHOICES = [
        ("UPLOADED", "Uploaded"),
        ("PROCESSING", "Processing"),
        ("COMPLETED", "Completed"),
        ("FAILED", "Failed"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="ingestion_batches")
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, related_name="batches")
    original_filename = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="UPLOADED")
    total_rows = models.PositiveIntegerField(default=0)
    normalized_rows = models.PositiveIntegerField(default=0)
    failed_rows = models.PositiveIntegerField(default=0)
    suspicious_rows = models.PositiveIntegerField(default=0)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.original_filename} ({self.status})"


class RawRecord(models.Model):
    batch = models.ForeignKey(IngestionBatch, on_delete=models.CASCADE, related_name="raw_records")
    row_number = models.PositiveIntegerField()
    raw_payload = models.JSONField()
    parse_status = models.CharField(max_length=50, default="PARSED")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Batch {self.batch_id} Row {self.row_number}"


class NormalizedActivity(models.Model):
    SCOPE_CHOICES = [
        ("SCOPE_1", "Scope 1"),
        ("SCOPE_2", "Scope 2"),
        ("SCOPE_3", "Scope 3"),
    ]

    REVIEW_STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("LOCKED", "Locked for Audit"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="activities")
    raw_record = models.OneToOneField(RawRecord, on_delete=models.CASCADE, related_name="normalized_activity")

    source_type = models.CharField(max_length=50)
    activity_type = models.CharField(max_length=255)
    scope = models.CharField(max_length=50, choices=SCOPE_CHOICES)

    original_quantity = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    original_unit = models.CharField(max_length=50, blank=True)
    normalized_quantity = models.DecimalField(max_digits=18, decimal_places=4, null=True, blank=True)
    normalized_unit = models.CharField(max_length=50, blank=True)

    activity_date = models.DateField(null=True, blank=True)
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)

    facility_code = models.CharField(max_length=100, blank=True)
    vendor_or_supplier = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=10, blank=True)

    source_row_reference = models.CharField(max_length=255, blank=True)
    review_status = models.CharField(max_length=50, choices=REVIEW_STATUS_CHOICES, default="PENDING")
    locked_for_audit = models.BooleanField(default=False)

    approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    approved_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} - {self.activity_type}"


class ValidationIssue(models.Model):
    SEVERITY_CHOICES = [
        ("ERROR", "Error"),
        ("WARNING", "Warning"),
    ]

    activity = models.ForeignKey(NormalizedActivity, on_delete=models.CASCADE, related_name="issues")
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    issue_code = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.severity}: {self.issue_code}"


class AuditLog(models.Model):
    activity = models.ForeignKey(NormalizedActivity, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.CharField(max_length=100)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    old_value = models.JSONField(null=True, blank=True)
    new_value = models.JSONField(null=True, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} on Activity {self.activity_id}"