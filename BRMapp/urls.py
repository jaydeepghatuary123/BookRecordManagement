from django.urls import path
from BRMapp import views
from django.conf.urls import url

urlpatterns = [
    url('new-book',views.newBook),
    url('edit-book',views.editBook),
    url('view-books',views.viewBooks),
    url('search-book',views.searchBook),
    url('delete-book',views.delectBook),
    url(r'^add',views.add),
    url('search',views.search),
    url('edit',views.edit),
    url('login',views.userLogin),
    url('logout',views.userLogout),
]
