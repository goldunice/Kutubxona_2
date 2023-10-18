from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


def greeting(request):
    return HttpResponse("Hello World")


def homepage(request):
    return render(request, "home.html")


def ayol_muallif_kitoblari(request):
    content = {
        "kitoblar": Kitob.objects.filter(muallif__jins='Ayol')
    }
    return render(request, "mashq_uchun/ayol_kitoblari.html", content)


def all_books(request):
    if request.method == 'POST':
        a = request.POST.get("ism")
        b = request.POST.get("kitob_s")
        c = request.POST.get("kurs")
        Muallif.objects.create(ism=a, kitob_soni=b, kurs=c)
        return redirect('/all_authors/')

    content = {
        "kitoblar": Kitob.objects.all()
    }
    return render(request, "kitoblar.html", content)


def kitob(request, son):
    content = {
        "book": Kitob.objects.get(id=son)
    }
    return render(request, 'mashq_uchun/kitob.html', content)


def all_authors(request):
    if request.method == 'POST':
        Muallif.objects.create(
            ism = request.POST.get("ism"),
            jins = request.POST.get("jins"),
            kitoblar_soni = request.POST.get("k_soni"),
            tirik = request.POST.get("tirik") == "on",
            tugilgan_sana = request.POST.get("t_sana"),
        )
        return redirect("/all_authors/")
    word = request.GET.get("search_word")
    result = Muallif.objects.all()
    if word:
        result = result.filter(ism__contains=word)
    content = {
        "all_authors": result
    }
    return render(request, 'mashq_uchun/all_authors.html', content)


def selected_author(request, son):
    content = {
        "selected_author": Muallif.objects.get(id=son)
    }
    return render(request, 'mashq_uchun/selected_author.html', content)


def all_books_2(request):
    soz = request.GET.get("kalit")
    natija = Kitob.objects.all()
    if soz:
        natija = natija.filter(nom__contains=soz) or natija.filter(muallif__ism__contains=soz)

    content = {
        "all_books_2": natija
    }
    return render(request, 'mashq_uchun/all_books.html', content)


def selected_book(request, son):
    content = {
        "selected_book": Kitob.objects.get(id=son)
    }
    return render(request, 'mashq_uchun/selected_book.html', content)


def record(request):
    word = request.GET.get("search_word")
    result = Record.objects.all()
    if word:
        result = result.filter(talaba__ism=word)
    content = {
        "record": result
    }
    return render(request, 'mashq_uchun/record.html', content)


def alive_authors(request):
    content = {
        "alive_authors": Muallif.objects.filter(tirik=True)
    }
    return render(request, 'mashq_uchun/alive_authors.html', content)


def top_three_books(request):
    content = {
        "top_three_books": Kitob.objects.order_by("-sahifa")[0:3]
    }
    return render(request, 'mashq_uchun/top_three_books.html', content)


def top_three_authors(request):
    content = {
        "top_three_authors": Muallif.objects.order_by("-kitoblar_soni")[0:3]
    }
    return render(request, 'mashq_uchun/top_three_authors.html', content)


def the_last_three_record(request):
    content = {
        "the_last_three_record": Record.objects.order_by("-olingan_sana")[0:3]
    }
    return render(request, 'mashq_uchun/the_last_three_record.html', content)


def alive_author_books(request):
    content = {
        "alive_author_books": Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'mashq_uchun/alive_author_books.html', content)


def the_same_genre_books(request):
    content = {
        "the_same_genre_books": Kitob.objects.filter(janr__contains="Badiiy")
    }
    return render(request, 'mashq_uchun/the_same_genre_books.html', content)


def the_oldest_authors(request):
    content = {
        "the_oldest_authors": Muallif.objects.order_by("tugilgan_sana")[0:3]
    }
    return render(request, 'mashq_uchun/the_oldest_authors.html', content)


def books_less_ten(request):
    authors = Muallif.objects.filter(kitoblar_soni__lt=10)
    books = Kitob.objects.filter(muallif__id__in=authors.values("id"))
    context = {'authors': authors, "books": books}
    return render(request, 'mashq_uchun/books_less_ten.html', context)


def selected_record(request, id):
    content = {
        "selected_record": Record.objects.get(id=id)
    }
    return render(request, 'mashq_uchun/selected_record.html', content)


def graduated_student(request):
    content = {
        "graduated_student": Record.objects.filter(talaba__kurs=4)
    }
    return render(request, 'mashq_uchun/graduated_student.html', content)


def delete_book(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/all_books/")


def delete_author(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/all_authors/")


def delete_record(request, son):
    Record.objects.get(id=son).delete()
    return redirect("/record/")


def talabalar(request):
    if request.method == 'POST':
        a = request.POST.get("ism")
        b = request.POST.get("kitob_soni")
        c = request.POST.get("kurs")
        Talaba(ism=a, kitob_soni=b, kurs=c).save()

        return redirect('/talabalar/')

    content = {
        "talabalar": Talaba.objects.all()
    }
    return render(request, "mashq_uchun/talabalar.html", content)
