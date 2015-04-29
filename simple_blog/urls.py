from django.conf.urls import include, url
from django.contrib import admin
from blogapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'simple_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createBlog, name='addblog'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}),
]
