from django.contrib import admin
from library.models import Reader, Author, Book


@admin.register(Reader)
class AdminReader(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'phone_number', 'active_books')


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    fields = ('title', 'total_page', 'author', 'total_instances')


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
