from rest_framework.throttling import UserRateThrottle


class ProductsRateThrottle(UserRateThrottle):
    scope = "product"

class CategoryRateThrottle(UserRateThrottle):
    scope = "category"

class SearchRateThrottle(UserRateThrottle):
    scope = "search"