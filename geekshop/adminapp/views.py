from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

from adminapp.forms import AdminShopUserRegisterForm, AdminShopUserChangeForm, AdminProductCategoryEditForm, AdminProductEditForm

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     object_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': 'admin panel/users',
#         'object_list': object_list,
#     }
#     return render(request, 'adminapp/users.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UsersListView(ListView):
    model = ShopUser
    # paginate_by = 2
    # template_name = 'adminapp/users.html'

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    # def get_context_data(self, *, object_list=None, **kwargs):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'admin panel/users'
        return context


# def user_create(request):
#     if request.method == 'POST':
#         form = AdminShopUserRegisterForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:index'))
#     else:
#         form = AdminShopUserRegisterForm()
#
#     context = {
#         'title': 'users/create',
#         'form': form,
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminShopUserCreateView(CreateView):
    model = ShopUser
    success_url = reverse_lazy('admin:index')
    form_class = AdminShopUserRegisterForm
    # template_name = 'adminapp/user_update.html'
    # fields = ('__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'users/create'
        return context

# def user_update(request, pk):
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         form = AdminShopUserChangeForm(request.POST, request.FILES, instance=edit_user)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:user_update',
#                                                 kwargs={
#                                                     'pk': edit_user.pk,
#                                                 }))
#     else:
#         form = AdminShopUserChangeForm(instance=edit_user)
#
#     content = {
#         'title': 'users/edit',
#         'form': form,
#     }
#
#     return render(request, 'adminapp/user_update.html', content)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminShopUserUpdateView(UpdateView):
    model = ShopUser
    success_url = reverse_lazy('admin:index')
    form_class = AdminShopUserChangeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'users/edit'
        return context

# def user_delete(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     # user.is_active = False
#     # user.save()
#     # return HttpResponseRedirect(reverse('admin:index'))
#     if request.method == 'POST':
#         # user.delete()
#         # вместо удаления лучше сделаем неактивным
#         user.is_active = False
#         user.save()
#         return HttpResponseRedirect(reverse('admin:index'))
#
#     context = {
#         'title': 'users/delete',
#         'user_to_delete': user,
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminShopUserDeleteView(DeleteView):
    model = ShopUser
    success_url = reverse_lazy('admin:index')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'users/delete'
        return context


# def user_activate(request, pk):
#     user = get_object_or_404(ShopUser, pk=pk)
#     if request.method == 'POST':
#         user.is_active = True
#         user.save()
#         return HttpResponseRedirect(reverse('admin:index'))
#
#     context = {
#         'title': 'users/activate',
#         'user_to_activate': user,
#     }
#
#     return render(request, 'adminapp/user_activate.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class AdminShopUserActivateView(DeleteView):
    model = ShopUser
    success_url = reverse_lazy('admin:index')
    template_name_suffix = '_confirm_activate'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'users/activate'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def categories(request):
#     # categories_list = ProductCategory.objects.all()
#     categories_list = ProductCategory.objects.order_by('-is_active', 'name')
#
#     context = {
#         'title': 'admin panel/categories',
#         'object_list': categories_list,
#     }
#
#     return render(request, 'adminapp/categories.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryListView(ListView):
    model = ProductCategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'admin panel/categories'
        return context


# def category_create(request):
#     if request.method == 'POST':
#         form = AdminProductCategoryEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         form = AdminProductCategoryEditForm()
#
#     context = {
#         'title': 'categories/create',
#         'form': form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('admin:categories')
    form_class = AdminProductCategoryEditForm
    # template_name = 'adminapp/category_update.html'
    # fields = ('__all__')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'categories/create'
        return context

# def category_update(request, pk):
#     edit_obj = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = AdminProductCategoryEditForm(request.POST, request.FILES, instance=edit_obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:category_update',
#                                                 kwargs={
#                                                     'pk': edit_obj.pk,
#                                                 }))
#     else:
#         form = AdminProductCategoryEditForm(instance=edit_obj)
#
#     context = {
#         'title': 'categories/edit',
#         'form': form,
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('admin:categories')
    form_class = AdminProductCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'categories/edit'
        return context

# def category_delete(request, pk):
#     item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         item.is_active = False
#         item.product_set.all().update(is_active=False)
#         item.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         item.product_set.all().update(is_active=True)
#
#     context = {
#         'title': 'categories/delete',
#         # 'category_to_delete': item,
#         'object': item,
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.product_set.all().update(is_active=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'categories/delete'
        return context

# def category_activate(request, pk):
#     item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         item.is_active = True
#         item.save()
#         return HttpResponseRedirect(reverse('admin:categories'))
#
#     context = {
#         'title': 'categories/activate',
#         # 'category_to_activate': item,
#         'object': item,
#     }
#
#     return render(request, 'adminapp/category_activate.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryActivateView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('admin:categories')
    template_name_suffix = '_confirm_activate'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'categories/activate'
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def products(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#     object_list = Product.objects.filter(category__pk=pk).order_by('-is_active', 'name')
#
#     context = {
#         'title': 'admin panel/product',
#         'category': category,
#         'object_list': object_list,
#     }
#
#     return render(request, 'adminapp/products.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductListView(ListView):
    model = Product
    paginate_by = 2

    def get_queryset(self):
        self.category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'admin panel/products'
        context['category'] = self.category
        return context


# def product_read(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#
#     context = {
#         'title': 'product/detail',
#         'object': product,
#     }
#
#     return render(request, 'adminapp/product_read.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product/detail'
        return context


# def product_create(request, pk):
#     category = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = AdminProductEditForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:products',
#                                                 kwargs={
#                                                     'pk': pk,
#                                                 }
#                                                 ))
#     else:
#         form = AdminProductEditForm(initial={'category': category})
#
#     context = {
#         'title': 'products/create',
#         'form': form,
#         'category': category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = AdminProductEditForm

    def get_form_kwargs(self):
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        kwargs = super(ProductCreateView, self).get_form_kwargs()
        kwargs.update({
            'initial': {'category': category}
        })
        return kwargs

    def get_queryset(self):
        category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product/create'
        return context


# def product_update(request, pk):
#     edit_obj = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = AdminProductEditForm(request.POST, request.FILES, instance=edit_obj)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('admin:product_update',
#                                                 kwargs={
#                                                     'pk': edit_obj.pk,
#                                                 }))
#     else:
#         form = AdminProductEditForm(instance=edit_obj)
#
#     context = {
#         'title': 'products/edit',
#         'form': form,
#         'category': edit_obj.category,
#     }
#
#     return render(request, 'adminapp/product_update.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    form_class = AdminProductEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'products/edit'
        return context


# def product_delete(request, pk):
#     item = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         item.is_active = False
#         item.save()
#         return HttpResponseRedirect(reverse('admin:products',
#                                             kwargs={
#                                                 'pk': item.category.pk,
#                                             }))
#     context = {
#         'title': 'products/delete',
#         # 'product_to_delete': item,
#         'object': item,
#     }
#
#     return render(request, 'adminapp/product_delete.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('admin:products',
                                                 kwargs={
                                                     'pk': self.object.category.pk,
                                                 }))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product/delete'
        return context


# def product_activate(request, pk):
#     item = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         item.is_active = True
#         item.save()
#         return HttpResponseRedirect(reverse('admin:products',
#                                             kwargs={
#                                                 'pk': item.category.pk,
#                                             }))
#     context = {
#         'title': 'products/activate',
#         # 'product_to_activate': item,
#         'object': item,
#     }
#
#     return render(request, 'adminapp/product_activate.html', context)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductActivateView(DeleteView):
    model = Product
    template_name_suffix = '_confirm_activate'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = True
        self.object.save()
        return HttpResponseRedirect(reverse_lazy('admin:products',
                                                 kwargs={
                                                     'pk': self.object.category.pk,
                                                 }))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product/activate'
        return context
