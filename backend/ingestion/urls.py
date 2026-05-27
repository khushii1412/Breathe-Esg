from django.urls import path

from . import views

urlpatterns = [
    path("tenants/", views.TenantListCreateView.as_view(), name="tenant-list-create"),
    path("data-sources/", views.DataSourceListCreateView.as_view(), name="data-source-list-create"),
    path("batches/", views.IngestionBatchListView.as_view(), name="batch-list"),
    path("activities/", views.NormalizedActivityListView.as_view(), name="activity-list"),
    path("activities/<int:pk>/", views.NormalizedActivityDetailView.as_view(), name="activity-detail"),
    path("dashboard/summary/", views.dashboard_summary, name="dashboard-summary"),
]