from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('login/', views.login_view, name='login_view'),
    path('welcome/', views.welcome, name='welcome'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),

    #Create - MAP
    path('map_create/', views.map_create, name='map_create'),
    #Read - MAP
    path('map_read/', views.map_read, name='map_read'),
    # Update - MAP
    path('map_edit/<int:id>', views.map_edit, name='map_edit'),
    #Update - MAP
    path('map_update/<int:id>', views.map_update, name='map_update'),
    #Delete - MAP
    path('map_delete/<int:id>', views.map_delete, name='map_delete'),

# Energy consumption and fuel production
    # Create - energyfuel
    path('ecfp_create/', views.ecfp_create, name='ecfp_create'),
    # Read - energyfuel
    path('ecfp_read/', views.ecfp_read, name='ecfp_read'),
    # Update - energyfuel
    path('ecfp_edit/<int:id>', views.ecfp_edit, name='ecfp_edit'),
    # Update - energyfuel
    path('ecfp_update/<int:id>', views.ecfp_update, name='ecfp_update'),
    # Delete - energyfuel
    path('ecfp_delete/<int:id>', views.ecfp_delete, name='ecfp_delete'),
    #cement
    # path('cement/', views.cement_sector, name='cement'),
    # Create - cement
    path('cem_create/', views.cem_create, name='cem_create'),
    # Read - cement
    path('cem_read/', views.cem_read, name='cem_read'),
    # Edit - cement
    path('cem_edit/<int:id>', views.cem_edit, name='cem_edit'),
    # Update - cement
    path('cem_update/<int:id>', views.cem_update, name='cem_update'),
    # Delete - cement
    path('cem_delete/<int:id>', views.cem_delete, name='cem_delete'),

    # Environment and Health
    # path('health/', views.health, name='health'),
    # Create - eAndH
    path('eAndH_create/', views.eAndH_create, name='eAndH_create'),
    # Read - eAndH
    path('eAndH_read/', views.eAndH_read, name='eAndH_read'),
    # Edit - cement
    path('eAndH_edit/<int:id>', views.eAndH_edit, name='eAndH_edit'),
    # Update - cement
    path('eAndH_update/<int:id>', views.eAndH_update, name='eAndH_update'),
    # Delete - cement
    path('eAndH_delete/<int:id>', views.eAndH_delete, name='eAndH_delete'),

    #ASG MINING
    # path('Asgm/', views.Asgm, name='Asgm'),
    # Create - asgm
    path('asgm_create/', views.asgm_create, name='asgm_create'),
    # Read - asgm
    path('asgm_read/', views.asgm_read, name='asgm_read'),
    # Edit - asgm
    path('asgm_edit/<int:id>', views.asgm_edit, name='asgm_edit'),
    # Update - asgm
    path('asgm_update/<int:id>', views.asgm_update, name='asgm_update'),
    # Delete - asgm
    path('asgm_delete/<int:id>', views.asgm_delete, name='asgm_delete'),


]
