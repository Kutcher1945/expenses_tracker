from django.contrib import admin
from .models import Category, Expense, Vendor, PaymentMethod, ExpenseReport, Employee, ExpenseCategorySubtype

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount', 'category', 'date', 'created_by')
    list_filter = ('category', 'date')
    search_fields = ('description', 'created_by__username')

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact')
    search_fields = ('name', 'contact')

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(ExpenseReport)
class ExpenseReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_date', 'end_date')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'position')
    search_fields = ('user__username', 'department', 'position')

@admin.register(ExpenseCategorySubtype)
class ExpenseCategorySubtypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('name', 'category__name')
