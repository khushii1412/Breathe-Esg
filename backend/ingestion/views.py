from django.db.models import Count
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DataSource, IngestionBatch, NormalizedActivity, Tenant
from .serializers import (
    DataSourceSerializer,
    IngestionBatchSerializer,
    NormalizedActivitySerializer,
    TenantSerializer,
)


class TenantListCreateView(generics.ListCreateAPIView):
    queryset = Tenant.objects.all().order_by("-created_at")
    serializer_class = TenantSerializer


class DataSourceListCreateView(generics.ListCreateAPIView):
    queryset = DataSource.objects.all().order_by("-created_at")
    serializer_class = DataSourceSerializer


class IngestionBatchListView(generics.ListAPIView):
    queryset = IngestionBatch.objects.all().order_by("-uploaded_at")
    serializer_class = IngestionBatchSerializer


class NormalizedActivityListView(generics.ListAPIView):
    queryset = NormalizedActivity.objects.all().order_by("-created_at")
    serializer_class = NormalizedActivitySerializer


class NormalizedActivityDetailView(generics.RetrieveAPIView):
    queryset = NormalizedActivity.objects.all()
    serializer_class = NormalizedActivitySerializer


@api_view(["GET"])
def dashboard_summary(request):
    total_batches = IngestionBatch.objects.count()
    total_activities = NormalizedActivity.objects.count()

    status_counts = (
        NormalizedActivity.objects.values("review_status")
        .annotate(count=Count("id"))
        .order_by("review_status")
    )

    source_counts = (
        NormalizedActivity.objects.values("source_type")
        .annotate(count=Count("id"))
        .order_by("source_type")
    )

    scope_counts = (
        NormalizedActivity.objects.values("scope")
        .annotate(count=Count("id"))
        .order_by("scope")
    )

    return Response(
        {
            "total_batches": total_batches,
            "total_activities": total_activities,
            "review_status_counts": list(status_counts),
            "source_counts": list(source_counts),
            "scope_counts": list(scope_counts),
        }
    )