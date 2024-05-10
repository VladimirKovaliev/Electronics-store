from django.contrib import admin

from products.models import Producer, Supplier, Product, Supply


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_filter = ('city',)
    list_per_page = 10


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city')
    list_filter = ('city',)
    list_per_page = 10


@admin.register(Product)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('title', 'provider', 'model')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('product', 'producer', 'provider', 'debt')
    actions = ['nullify_debt']

    def nullify_debt(self, request, queryset):
        for item in queryset:
            item.debt = 0
            item.save()
        self.message_user(request, f'Задолженность перед поставщиком в выбранных поставках обнулена.')

    nullify_debt.short_description = 'Обнулить задолженность'