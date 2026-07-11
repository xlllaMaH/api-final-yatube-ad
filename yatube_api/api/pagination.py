"""Pagination api."""
from rest_framework.pagination import LimitOffsetPagination


class PostPagination(LimitOffsetPagination):
    """Pagination class for model Post."""

    default_limit = 10

    def paginate_queryset(self, queryset, request, view=None):
        """Use LimitOffsetPagination when limit/offset are present."""
        if (
            'limit' not in request.query_params
            and 'offset' not in request.query_params
        ):
            return None
        return super().paginate_queryset(queryset, request, view)
