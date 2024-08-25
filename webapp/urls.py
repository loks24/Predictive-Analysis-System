from django.conf.urls import url
from webapp import views

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^Result/$',views.TagCodeView.as_view(),name="Tagcodeview"),
    url(r'^Report/$',views.ReportView.as_view(),name="ReportView"),
]