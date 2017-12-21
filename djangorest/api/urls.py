from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateTransactionView, DetailsTransactionView, CreateBlockView, DetailsBlockView, AddBlockView, MineBlockView, UserView, UserDetailsView


urlpatterns = {
	url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^transactions/$', CreateTransactionView.as_view(), name='create'),
	url(r'^transactions/(?P<pk>[0-9]+)/$', DetailsTransactionView.as_view(), name='details'),
	url(r'^blocks/$', CreateBlockView.as_view(), name='create'),
	url(r'^blocks/(?P<pk>[0-9]+)/$', DetailsBlockView.as_view(), name='details'),
	url(r'^blocks/add/(?P<num_of_blocks_to_add>[0-9]+)/$', AddBlockView.as_view(), name='block_add'),
	url(r'^blocks/mine/$', MineBlockView.as_view(), name='block_mine'),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
	url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)