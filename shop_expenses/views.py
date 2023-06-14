from rest_framework import viewsets
from .models import Category, Expense, Vendor, PaymentMethod, ExpenseReport, Employee, ExpenseCategorySubtype
from .serializers import CategorySerializer, ExpenseSerializer, VendorSerializer, PaymentMethodSerializer, ExpenseReportSerializer, EmployeeSerializer, ExpenseCategorySubtypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class ExpenseReportViewSet(viewsets.ModelViewSet):
    queryset = ExpenseReport.objects.all()
    serializer_class = ExpenseReportSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ExpenseCategorySubtypeViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategorySubtype.objects.all()
    serializer_class = ExpenseCategorySubtypeSerializer
