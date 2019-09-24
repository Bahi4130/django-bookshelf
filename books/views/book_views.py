from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from books.filters import BookFilter
from books.forms import AddBookForm
from books.models import Book


class AddBookView(View):
    form_class = AddBookForm
    initial = {'key': 'value'}
    template_name = 'add_book.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                self.__save_to_db(form)
            except Exception as e:
                if settings.DEBUG == False:
                    return HttpResponse('Data could not be saved to DB.')
                raise Exception(e)

            return HttpResponseRedirect('/add-book/')

        return render(request, self.template_name, {'form': form})

    def __book_mapping_for_db(self, form):
        book = Book()
        book.isbn = form.cleaned_data['isbn']
        book.author = form.cleaned_data['author']
        book.title = form.cleaned_data['title']
        book.year = form.cleaned_data['year']
        book.description = form.cleaned_data['description']
        book.borrowed_by_who = form.cleaned_data['borrowed_by_who']
        book.borrowed_till = self.__map_borrowed_till(form.cleaned_data['borrowed_till'])
        book.is_borrowed = self.__map_is_borrowed(form.cleaned_data['borrowed_by_who'])

        return book

    def __map_borrowed_till(self, date):
        if date is not None:
            return date

        return ''

    def __save_to_db(self, form):
        book = self.__book_mapping_for_db(form)
        book.save()

    def __map_is_borrowed(self, borrowed_by_who):
        if borrowed_by_who is not None:
            return True

        return False


class BooksListView(ListView):

    def get(self, request):
        books_list = Book.objects.all()
        books_filter = BookFilter(request.GET, queryset=books_list)

        return render(request, 'index.html', {'filter': books_filter})







