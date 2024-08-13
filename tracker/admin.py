from django.contrib import admin
from tracker.models import *

admin.site.site_header = "Expense Tracker"
admin.site.site_title = "Expense Tracker"
admin.site.site_url = "Expense Tracker"


@admin.action(description="Mark selected stories as Credit")
def make_credit(modeladmin, request, queryset):
    queryset.update(status="CREDIT")

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        "amount",
        "expense_type",
        "description",
        "created_at",
        "display_value",
    ]


    actions = ['Make_Credit']

    def display_value(self, obj):
        if obj.amount > 0:
            return "Positive"
        else:
            return "Negative"


    search_fields = ["expense_type", "description"]
    list_filter = ["expense_type"]
    ordering = ["-expense_type"]


admin.site.register(CurrentBalance)
admin.site.register(TrackingHistory, TrackingHistoryAdmin)
# Register your models here.
