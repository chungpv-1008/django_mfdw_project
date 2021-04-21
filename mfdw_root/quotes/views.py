from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from quotes.models import Quote
from quotes.forms import QuoteForm
from pages.models import Page


class QuoteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("login")
    # model = Quote
    context_object_name = "all_quotes"

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

    # def get_context_data(self, **kwargs):
    #     context = super(QuoteList, self).get_context_data(**kwargs)
    #     context["page_list"] = Page.objects.all()
    #     return context


class QuoteView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("login")
    # model = Quote
    context_object_name = "quote"

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)
    # def get_context_data(self, **kwargs):
    #     context = super(QuoteView, self).get_context_data(**kwargs)
    #     context["page_list"] = Page.objects.all()
    #     return context

@login_required(login_url=reverse_lazy("login"))
def quote_req(request):
    submitted = False
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except Exception:
                pass
            quote.save()
            return HttpResponseRedirect("/quote/?submitted=True")
    else:
        form = QuoteForm()
        if submitted in request.GET:
            submitted = True
    context = {
        "form": form,
        "submitted": submitted,
        "page_list": Page.objects.all()
    }
    return render(request, "quotes/quote.html", context=context)


class Register(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("register-success")

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
