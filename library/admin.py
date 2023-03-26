from django.contrib import admin
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html
from library.models import Reader, Author, Book


@admin.action(description='Изменение статуса на not_active')
def status_not_active(self, request, queryset: QuerySet):
    obj = queryset.update(status=Reader.Status.not_active)
    self.message_user(request, f'Статус активности {obj} позиций изменен на not_active')


@admin.action(description='Изменение статуса на is_active')
def status_is_active(self, request, queryset: QuerySet):
    obj = queryset.update(status=Reader.Status.is_active)
    self.message_user(request, f'Статус активности {obj} позиций изменен на is_active')


@admin.action(description='Изменение количества книг в библиотеке')
def book_total_instances(self, request, queryset: QuerySet):
    queryset.update(total_instances=0)
    self.message_user(request, 'Количество книг в библиотеке изменено на 0')


@admin.action(description='Удаление всех активных книг читателя')
def delete_active_books(self, request, queryset: QuerySet):
    for book in queryset:
        book.active_books.all().delete()
    self.message_user(request, 'У читателя нет активных книг')
    return redirect('.')


@admin.register(Reader)
class AdminReader(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'display_active_books', 'status')
    list_filter = ('status',)

    actions = [status_not_active, status_is_active, delete_active_books]

    def save_model(self, request, obj, form, change):
        if len(form.cleaned_data['active_books']) > 3:
            raise ValueError('Превышено максимальное число книг (3)')

        return super().save_model(request, obj, form, change)


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'total_page', 'author', 'total_instances', 'author_link')

    actions = [book_total_instances]

    def author_link(self, obj):
        link = reverse("admin:library_author_change", args=[obj.author.pk])

        return format_html(f'<a href="{link}">{obj.author}</a>')


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
