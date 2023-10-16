from django.contrib import admin
from django.urls import path
from asosiy.views import (greeting, homepage, all_books, ayol_muallif_kitoblari,
                          kitob, all_authors, selected_author, selected_book, all_books_2, record,
                          alive_authors, top_three_books, top_three_authors, the_last_three_record,
                          alive_author_books, the_same_genre_books, the_oldest_authors, books_less_ten,
                          selected_record, graduated_student, delete_book)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', greeting),
    path('', homepage),
    path('all_books_1/', all_books),
    path('woman_authors/', ayol_muallif_kitoblari),
    path('kitoblar/<int:son>/', kitob),
    path('all_authors', all_authors),
    path('selected_author/<int:son>/', selected_author),
    path('all_books/', all_books_2),
    path('selected_book/<int:son>', selected_book),
    path('record', record),
    path('alive_authors', alive_authors),
    path('top_three_books', top_three_books),
    path('top_three_authors', top_three_authors),
    path('the_last_three_record', the_last_three_record),
    path('alive_author_books', alive_author_books),
    path('the_same_genre_books', the_same_genre_books),
    path('the_oldest_authors', the_oldest_authors),
    path('books_less_ten', books_less_ten),
    path('selected_record/<int:id>', selected_record),
    path('graduated_student', graduated_student),
    path('delete_book/<int:son>/', delete_book),

]