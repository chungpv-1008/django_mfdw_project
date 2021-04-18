from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from pages.models import Page
from pages.forms import ContactForm

def index(request, pagename):
    print("Page name", pagename)
    pagename = "/" + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        "title": pg.title,
        "content": pg.body_text,
        "last_updated": pg.update_date,
        "y": enumerate(range(4)),
        "page_list": Page.objects.all()
    }
    return render(request, "pages/page.html", context)


def contact(request):
    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            con = get_connection("django.core.mail.backends.console.EmailBackend")
            print("-------------------")
            send_mail(
                cd["subject"],
                cd["message"],
                cd["email"],
                ["chungcypher11111999@gmail.com"],
                connection=con
            )
            print("------------------")
            return HttpResponseRedirect("/contact?submitted=True")
    else:
        form = ContactForm()
        if "submitted" in request.GET:
            submitted = True

    context = {
        "form": form,
        "page_list": Page.objects.all(),
        "submitted": submitted
    }
    return render(request, "pages/contact.html", context)
