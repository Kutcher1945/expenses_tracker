from rest_framework import serializers
from .models import Category, Expense, Vendor, PaymentMethod, ExpenseReport, Employee, ExpenseCategorySubtype, Profit, ProfitReport

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Expense
        fields = '__all__'

class ProfitSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Profit
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'

class ExpenseReportSerializer(serializers.ModelSerializer):
    expenses = ExpenseSerializer(many=True)

    class Meta:
        model = ExpenseReport
        fields = '__all__'

class ProfitReportSerializer(serializers.ModelSerializer):
    profits = ProfitSerializer(many=True)

    class Meta:
        model = ExpenseReport
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ExpenseCategorySubtypeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ExpenseCategorySubtype
        fields = '__all__'
