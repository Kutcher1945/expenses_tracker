from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'expenses', views.ExpenseViewSet)
router.register(r'profits', views.ProfitViewSet)
router.register(r'vendors', views.VendorViewSet)
router.register(r'payment-methods', views.PaymentMethodViewSet)
router.register(r'expense-reports', views.ExpenseReportViewSet)
router.register(r'profit-reports', views.ProfitReportViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'expense-category-subtypes', views.ExpenseCategorySubtypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
