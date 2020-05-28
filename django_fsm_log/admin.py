from django.contrib.contenttypes.admin import GenericTabularInline
from django.db.models import F

from .models import StateLog


__all__ = ('StateLogInline',)


class StateLogInline(GenericTabularInline):
    model = StateLog
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    fields = (
        'get_source_state_display',
        'get_state_display',
        'by',
        'description',
        'timestamp',
        'transition',
    )

    def get_readonly_fields(self, request, obj=None):
        return self.fields

    def get_queryset(self, request):
        return super(StateLogInline, self).get_queryset(
            request
        ).prefetch_related('content_object').order_by(F('timestamp').desc())
