from rest_framework import viewsets
from .models import Category, Expense, Vendor, PaymentMethod, ExpenseReport, Employee, ExpenseCategorySubtype, Profit, ProfitReport
from .serializers import CategorySerializer, ExpenseSerializer, VendorSerializer, PaymentMethodSerializer, ExpenseReportSerializer, EmployeeSerializer, ExpenseCategorySubtypeSerializer, ProfitSerializer, ProfitReportSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ProfitViewSet(viewsets.ModelViewSet):
    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class ExpenseReportViewSet(viewsets.ModelViewSet):
    queryset = ExpenseReport.objects.all()
    serializer_class = ExpenseReportSerializer

class ProfitReportViewSet(viewsets.ModelViewSet):
    queryset = ProfitReport.objects.all()
    serializer_class = ProfitReportSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ExpenseCategorySubtypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategorySubtype.objects.all()
    serializer_class = ExpenseCategorySubtypeSerializer
