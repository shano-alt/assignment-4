from django.shortcuts import render
from .models import Book, Category

def home(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category', '')

    books = Book.objects.all()
    categories = Category.objects.all()

    # 🔍 Filter by search text
    if search_query:
        books = books.filter(title__icontains=search_query) | books.filter(author__name__icontains=search_query)

    # 🏷️ Filter by category
    if category_id:
        books = books.filter(categories__id=category_id)

    context = {
        'books': books.distinct(),
        'categories': categories,
        'search_query': search_query,
        'selected_category': category_id,
    }
    return render(request, 'library/home.html', context)
