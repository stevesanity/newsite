from django.conf.urls import patterns, include, url
from django.contrib import admin

from showdata.views import *

urlpatterns = patterns('',
    # fhir-app url
    (r'^fhir-app/launch.html$',test_smart),
    (r'^fhir-app/$',main_dashboard),
    (r'^fhir-app/maindashboard.html$',main_dashboard),
    (r'^fhir-app/frontpage.html$',front_page),
    (r'^fhir-app/login.html$',log_in_verifying),
    (r'^fhir-app/account.html$',account_edit),
    (r'^fhir-app/introriskpredicton.html$',intro_risk_prediction),
    (r'^fhir-app/introhealthalert.html$',intro_health_alert),
    # normal url
    (r'^$', front_page ),
    (r'^frontpage.html$', front_page ),
    (r'^login.html$',log_in_verifying),
    (r'^account.html$',account_edit),
    (r'^maindashboard.html$',main_dashboard),
    (r'^introriskpredicton.html$',intro_risk_prediction),
    (r'^introhealthalert.html$',intro_health_alert),
    # test url
    (r'^showdata/$',show_data),
    (r'^add(\d+)/$',add_data),
)
