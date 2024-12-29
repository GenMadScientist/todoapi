from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination

class CustomPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 5
    page_size_query_param = "page_size"

class CustomLimitPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 5

class CursorPagePagination(CursorPagination):
    page_size = 3
    ordering = "-title"