from django.conf.urls import url,include
from django.contrib.auth.views import login,logout
from .views import view_home,HomeView,cont,register,view_poll,update_vote,status,give_poll
urlpatterns = [
	url(r'home/$',view_home),
	url(r'complaint/$',HomeView.as_view(),name='complaint'),
	url(r'login/$',login,{'template_name':'complaint/login.html'}),
	url(r'logout/$',logout,{'template_name':'complaint/logout.html'}),
	url(r'contact/$',cont,name='contact'),
	url(r'register/$',register,name='register'),
	url(r'add_poll/$',view_poll,name='add_poll'),
	url(r'add_poll_update/(?P<pk>\d+)/update$',update_vote,name='add_poll_update'),
	url(r'poll_status/$',status,name='poll_status'),
	url(r'give_poll/(?P<pk>\d+)/vote$',give_poll,name='give_poll_with_pk'),

	# url(r'add_poll/$',pollview.as_view(),name='add_poll'),

	#url(r'add_poll/$',choiceview.as_view(),name='add_poll'),
]
