from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
# from .views import BusinessCreateView
from . import views

urlpatterns = [
    path('',  views.index, name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^hood/',views.neighbourhood,name='neighbourhood'),
    # url(r'^user/',views.user,name='user'),
    url(r'^business/',views.business,name='business'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/',views.post,name='post'),
    url(r'^neighborhood/',views.neighbourhoods,name='neighbourhood')
    # path('business/new/',BusinessCreateView.as_view(), name = 'business-create'),
    # path('business/',views.business_list,name='business'),


    # url(r'^api/projects/$', views.ProjectsList.as_view()),
    # url(r'^api/profile/$', views.ProfileList.as_view()),

]