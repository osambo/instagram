from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', LoginView.as_view(), name='login_url'),
    url(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    url(r'^newpost/$', views.new_post, name='new_post'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^updateprofile/', views.update_profile, name='update_profile'),
    url(r'^likes/(?P<id>\d+)',views.likes,name ='like'),
    url(r'^follow/(\d+)',views.follow,name="follow"),
    url(r'^search/', views.search_user, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)