from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views  # Встроенные представления Django




# menedjer password - tir9482ieif
#admin password - 7272\
urlpatterns = [

    path('', views.Sbase, name='Home'),
    path('main/SGroupa.html', views.SGroupa, name='SGroupa'),
    path('main/Trenera.html', views.STrenera, name='Trenera'),
    path('main/Sorevnovania.html', views.SSorevnovania, name='Sorevnovania'),
    path('main/Roditel.html', views.SRoditel, name='Roditel'),
    path('main/Children.html', views.SChildren, name='Children'),
    path('main/Zapros.html', views.Zapros, name='Zapros'),


    path('api/tables/', views.get_tables, name='get_tables'),  # API для списка таблиц
    path('api/tables/<str:table_name>/', views.get_table_data, name='get_table_data'),  # API для данных таблицы
    path('api/query/<int:query_id>/', views.run_query, name='run_query'),  # API для выполнения запросов

    path('AddGroupa/', views.AddGroupa, name='AddGroupa'),
    path('AddTrenera/', views.AddTrenera, name='AddTrenera'),
    path('AddSorevnovania/', views.AddSorevnovania, name='AddSorevnovania'),
    path('AddRoditel/', views.AddRoditel, name='AddRoditel'),
    path('AddChildren/', views.AddChildren, name='AddChildren'),


    path('<int:id_groupa>/UpdateGroupa', views.edit_Groupa, name='UpdateGroupa'),
    path('<int:id_trenera>/UpdateTrenera', views.edit_Trenera, name='UpdateTrenera'),
    path('<int:id_sorevnovania>/UpdateSorevnovania', views.edit_Sorevnovania, name='UpdateSorevnovania'),
    path('<int:id_roditel>/UpdateRoditel', views.edit_Roditel, name='UpdateRoditel'),
    path('<int:id_children>/UpdateChildren', views.edit_Children, name='UpdateChildren'),



    path('<int:id_groupa>/DeleteGroupa', views.Delete_Groupa, name='DeleteGroupa'),
    path('<int:id_trenera>/DeleteTrenera', views.Delete_Trenera, name='DeleteTrenera'),
    path('<int:id_sorevnovania>/DeleteSorevnovania', views.Delete_Sorevnovania, name='DeleteSorevnovania'),
    path('<int:id_roditel>/DeleteRoditel', views.Delete_Roditel, name='DeleteRoditel'),
    path('<int:id_children>/DeleteChildren', views.Delete_Children, name='DeleteChildren'),


    path('main/Document', views.document, name='Document'),
    path('spravka', views.spravka, name='spravka'),
    path('spisok_grup', views.spisok_grup, name='spisok_grup'),
    path('sorevnovania', views.sorevnovania, name='sorevnovania'),


    path('login/', views.login, name='login'),
    path('/accounts/', include('django.contrib.auth.urls')),

]
