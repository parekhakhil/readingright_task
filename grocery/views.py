from .forms import AddGraceryListForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    ListView,
    DetailView,
    DeleteView,
)
from .models import Grocery

# Create your views here.


def home(request):
    context = {"grocery_list": Grocery.objects.filter(user=request.user)}
    return render(request, template_name="grocery/home.html", context=context)


class GroceryListView(LoginRequiredMixin,ListView):

    login_url = '/login/'
    redirect_field_name = 'login'
    model = Grocery
    template_name = "grocery/home.html"
    context_object_name = "grocery_list"
    ordering = ["-created_at"]
    def get_queryset(self):
        date = self.request.GET.get('q',None)
        queryset = Grocery.objects.select_related(
            'user').filter(user=self.request.user)  # noqa
        if date:
            queryset = queryset.filter(date = date)
        return queryset

class GroceryDetailView(LoginRequiredMixin,DetailView):
    model = Grocery

class GroceryCreateView(LoginRequiredMixin, CreateView):
    model = Grocery
    success_url = '/'
    # fields = ['product', 'quantity','status','date']
    form_class = AddGraceryListForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GroceryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Grocery
    # fields = ['product', 'quantity','status','date']
    form_class = AddGraceryListForm
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        grocery_obj = self.get_object()
        if self.request.user == grocery_obj.user:
            return True
        return False

class GroceryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Grocery
    success_url = '/'

    def test_func(self):
        grocery_obj = self.get_object()
        if self.request.user == grocery_obj.user:
            return True
        return False
