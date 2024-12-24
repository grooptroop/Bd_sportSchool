from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from requests import auth

from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from django.http import JsonResponse
from django.db import connection
from .forms import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def SGroupa(request):
    MGroupa = Groupa.objects.all()
    context = {
        'delete_Groupa': request.user.has_perm('main.delete_Receipt'),
        'add_Groupa': request.user.has_perm('main.add_Receipt'),
        'change_Groupa': request.user.has_perm('main.Receipt'),
        'MGroupa': MGroupa}
    return render(request, 'main/SGroupa.html',  context)

def Sbase(request):
    return render(request, 'main/base.html')

def STrenera(request):
    MTrenera = Trenera.objects.all()
    context = {
        'delete_Trenera': request.user.has_perm('main.delete_Receipt'),
        'add_Trenera': request.user.has_perm('main.add_Receipt'),
        'change_Trenera': request.user.has_perm('main.Receipt'),
        'MTrenera': MTrenera}
    return render(request, 'main/Trenera.html',  context)

def SSorevnovania(request):
    MSorevnovania = Sorevnovania.objects.all()
    context = {
        'delete_Sorevnovania': request.user.has_perm('main.delete_Receipt'),
        'add_Sorevnovania': request.user.has_perm('main.add_Receipt'),
        'change_Sorevnovania': request.user.has_perm('main.Receipt'),
        'MSorevnovania': MSorevnovania}
    return render(request, 'main/Sorevnovania.html',  context)

def SRoditel(request):
    MRoditel = Roditel.objects.all()
    context = {
        'delete_Roditel': request.user.has_perm('main.delete_Receipt'),
        'add_Roditel': request.user.has_perm('main.add_Receipt'),
        'change_Roditel': request.user.has_perm('main.Receipt'),
        'MRoditel': MRoditel}
    return render(request, 'main/Roditel.html',  context)

def SChildren(request):
    MChildren = Children.objects.all()
    context = {
        'delete_Children': request.user.has_perm('main.delete_Receipt'),
        'add_Children': request.user.has_perm('main.add_Receipt'),
        'change_Children': request.user.has_perm('main.Receipt'),
        'MChildren': MChildren}
    return render(request, 'main/Children.html',  context)

def Zapros(request):
    return render(request, 'main/Zapros.html')

def get_tables(request):
    # Получение всех таблиц в базе данных PostgreSQL
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT table_name FROM information_schema.tables "
            "WHERE table_schema = 'public'"
        )
        tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return JsonResponse(table_names, safe=False)


def get_table_data(request, table_name):
    # Получение данных из конкретной таблицы


    with connection.cursor() as cursor:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        rows = cursor.fetchall()
        column_names = [col[0] for col in cursor.description]

    data = [dict(zip(column_names, row)) for row in rows]
    return JsonResponse(data, safe=False)

def run_query(request, query_id):
    # if not request.user.groups.filter(name='Администраторы').exists():
    #     return JsonResponse({'error': 'Access Denied'}, status=403)

    predefined_queries = {
        1: "SELECT famili_tr, name_tr, last_name_tr FROM trenera INNER JOIN groupa ON trenera.id_trenera = groupa.trenera_id INNER JOIN children ON groupa.id_groupa = children.groupa_id WHERE (pol = 'Ж')",
        2: "SELECT * FROM children WHERE adress_ch LIKE '%г. Находка%';",
        3: "SELECT * FROM sorevnovania WHERE date_end = (SELECT MAX(date_end)FROM sorevnovania);",
        4: "SELECT * FROM children WHERE birthday = (SELECT MIN(birthday)FROM children WHERE pol = 'М');",
        5: "SELECT * FROM Groupa ORDER BY number_gr DESC;",
        6: "SELECT * FROM children WHERE birthday = (SELECT MIN(birthday)FROM children WHERE pol = 'Ж' AND ychastie = 'да');",
        7: "SELECT zvanie, famili_tr, vid_sporta FROM zvanie INNER JOIN trenera ON zvanie.ID_zvanie = trenera.zvanie_ID INNER JOIN Vid_sporta ON trenera.vid_sporta_ID = Vid_sporta.ID_vid_sporta",
        # Добавьте другие запросы
    }

    query = predefined_queries.get(query_id)
    if not query:
        return JsonResponse({'error': 'Invalid query ID'}, status=404)

    with connection.cursor() as cursor:
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    data = [dict(zip(column_names, row)) for row in rows]
    return JsonResponse(data, safe=False)

@permission_required('main.add_Groupa', raise_exception=True)
def AddGroupa(request):
    error = ''
    if request.method == 'POST':
        form = AddGroupaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('SGroupa')
        else:
            error = 'Неправильное заполнение формы'
    form = AddGroupaForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddGroupa.html', data)
@permission_required('main.change_Groupa', raise_exception=True)
def edit_Groupa(request, id_groupa):
    member = get_object_or_404(Groupa, id_groupa=id_groupa)
    if request.method == "POST":
        form = UpdateGroupaForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('SGroupa')
    else:
        form = UpdateGroupaForm(instance=member)
    return render(request, 'main/AddGroupa.html', {'form': form})

@permission_required('main.delete_Groupa', raise_exception=True)
def Delete_Groupa(request, id_groupa):
    member = get_object_or_404(Groupa, id_groupa=id_groupa)
    if request.method == "POST":
        form = UpdateGroupaForm(request.POST, instance=member)
        Groupa.objects.filter(id_groupa = id_groupa).delete()
        return redirect('SGroupa')
    else:
        form = UpdateGroupaForm(instance=member)
    return render(request, 'main/DeleteGroupa.html', {'form': form})


@permission_required('main.add_Trenera', raise_exception=True)
def AddTrenera(request):
    error = ''
    if request.method == 'POST':
        form = AddTreneraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Trenera')
        else:
            error = 'Неправильное заполнение формы'
    form = AddTreneraForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddTrenera.html', data)

@permission_required('main.change_Trenera', raise_exception=True)
def edit_Trenera(request, id_trenera):
    member = get_object_or_404(Trenera, id_trenera=id_trenera)
    if request.method == "POST":
        form = UpdateTreneraForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('Trenera')
    else:
        form = UpdateTreneraForm(instance=member)
    return render(request, 'main/AddTrenera.html', {'form': form})

@permission_required('main.delete_Trenera', raise_exception=True)
def Delete_Trenera(request, id_trenera):
    member = get_object_or_404(Trenera, id_trenera=id_trenera)
    if request.method == "POST":
        form = UpdateTreneraForm(request.POST, instance=member)
        Trenera.objects.filter(id_trenera = id_trenera).delete()
        return redirect('Trenera')
    else:
        form = UpdateTreneraForm(instance=member)
    return render(request, 'main/DeleteTrenera.html', {'form': form})

@permission_required('main.add_Sorevnovania', raise_exception=True)
def AddSorevnovania(request):
    error = ''
    if request.method == 'POST':
        form = AddSorevnovaniaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Sorevnovania')
        else:
            error = 'Неправильное заполнение формы'
    form = AddSorevnovaniaForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddSorevnovania.html', data)

@permission_required('main.change_Sorevnovania', raise_exception=True)
def edit_Sorevnovania(request, id_sorevnovania):
    member = get_object_or_404(Sorevnovania, id_sorevnovania=id_sorevnovania)
    if request.method == "POST":
        form = UpdateSorevnovaniaForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('Sorevnovania')
    else:
        form = UpdateSorevnovaniaForm(instance=member)
    return render(request, 'main/AddSorevnovania.html', {'form': form})

@permission_required('main.delete_Sorevnovania', raise_exception=True)
def Delete_Sorevnovania(request, id_sorevnovania):
    member = get_object_or_404(Sorevnovania, id_sorevnovania=id_sorevnovania)
    if request.method == "POST":
        form = UpdateSorevnovaniaForm(request.POST, instance=member)
        Sorevnovania.objects.filter(id_sorevnovania = id_sorevnovania).delete()
        return redirect('Sorevnovania')
    else:
        form = UpdateSorevnovaniaForm(instance=member)
    return render(request, 'main/DeleteSorevnovania.html', {'form': form})


@permission_required('main.add_Roditel', raise_exception=True)
def AddRoditel(request):
    error = ''
    if request.method == 'POST':
        form = AddRoditelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Roditel')
        else:
            error = 'Неправильное заполнение формы'
    form = AddRoditelForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddRoditel.html', data)

@permission_required('main.change_Roditel', raise_exception=True)
def edit_Roditel(request, id_roditel):
    member = get_object_or_404(Roditel, id_roditel=id_roditel)
    if request.method == "POST":
        form = UpdateRoditelForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('Roditel')
    else:
        form = UpdateRoditelForm(instance=member)
    return render(request, 'main/AddRoditel.html', {'form': form})


@permission_required('main.delete_Roditel', raise_exception=True)
def Delete_Roditel(request, id_roditel):
    member = get_object_or_404(Roditel, id_roditel=id_roditel)
    if request.method == "POST":
        form = UpdateRoditelForm(request.POST, instance=member)
        Roditel.objects.filter(id_roditel = id_roditel).delete()
        return redirect('Roditel')
    else:
        form = UpdateRoditelForm(instance=member)
    return render(request, 'main/DeleteRoditel.html', {'form': form})

@permission_required('main.add_Children', raise_exception=True)
def AddChildren(request):
    error = ''
    if request.method == 'POST':
        form = AddChildrenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Children')
        else:
            error = 'Неправильное заполнение формы'
    form = AddChildrenForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/AddChildren.html', data)

@permission_required('main.change_Children', raise_exception=True)
def edit_Children(request, id_children):
    member = get_object_or_404(Children, id_children=id_children)
    if request.method == "POST":
        form = UpdateChildrenForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('Children')
    else:
        form = UpdateChildrenForm(instance=member)
    return render(request, 'main/AddChildren.html', {'form': form})

@permission_required('main.delete_Children', raise_exception=True)
def Delete_Children(request, id_children):
    member = get_object_or_404(Children, id_children=id_children)
    if request.method == "POST":
        form = UpdateChildrenForm(request.POST, instance=member)
        Children.objects.filter(id_children = id_children).delete()
        return redirect('Children')
    else:
        form = UpdateChildrenForm(instance=member)
    return render(request, 'main/DeleteChildren.html', {'form': form})


def document(request):
    return render(request, 'main/Document.html')


def spravka(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="spravka.pdf"'

    people = Children.objects.raw("SELECT id_children, famili_ch, name_ch, last_name_ch, groupa_id FROM Children WHERE  id_children = '1'")
    for person in people:
        famili = str('Kirilovski   ')# из-за интерпритирования только английского языка сделаем костыль в виде заранее прописанных значений, пример реального применения в виде группы
        name = str('Anton    ')
        last_name = str('Fedorovich     ')
        groupa = str(person.groupa_id)
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    w, h = A4
    p.drawString(30, h - 90, "Certificate issued  " + famili + name + last_name)
    p.drawString(30, h - 140, 'It certifies the presence of the pupil in the sports school in the group numbered ' + groupa)
    p.drawString(30, h - 190, 'Principal Druzbin ')
    p.drawString(50, h - 240, 'Signature _______________')

    p.showPage()
    p.save()
    return response


def spisok_grup(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="spisok_grup.pdf"'

    people = Groupa.objects.raw("SELECT * FROM Groupa INNER JOIN trenera ON Groupa.trenera_id = trenera.id_trenera ")
    p = canvas.Canvas(response)
    w, h = A4
    y = 110
    #в данном примере мы продимонстрировали связи выведя тренеров, но фамилии написаны на русском из-за чего мы видем чёрные квадраты, чтобы показать что связи всё так есть оставили вид спорта не тронутым
    p.drawString(30, h - 90, "group list:")
    for person in people:
        p.drawString(30, h - (y+ 10), "The group " + str(person.number_gr) + "  includes athletes " + str(person.count_sportsmenov) )
        p.drawString(30, h - (y+ 25), "its full list is below (group number, sport, age, number of athletes, coach) ")
        p.drawString(50, h - (y + 45),str(person.id_groupa) +'       ' + str(person.number_gr) +'       '+ str(person.vid_sporta) + '      '+ str(person.vozrast)+'      '+ str(person.count_sportsmenov) + '      '+ str(person.famili_tr))
        y = y+ 90
    p.drawString(30, h - (y+20), 'Principal Druzbin ')
    p.drawString(50, h - (y+40), 'Signature _______________')
    p.showPage()
    p.save()
    return response

def sorevnovania(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sorevnovania.pdf"'

    people = Sorevnovania.objects.raw("SELECT * FROM Sorevnovania ")
    p = canvas.Canvas(response)
    w, h = A4
    y = 110
    p.drawString(30, h - (y - 40), 'Below are lists of competitions in the table listed (name, location, start date, end date)')
    for person in people:
        p.drawString(50, h - y,str(person.id_sorevnovania) +'       ' + str(person.name_so)  + '      '+ str(person.date_start)+'      '+ str(person.date_end) + '      ')
        y = y+20
    p.drawString(30, h - (y+20), 'Principal Druzbin ')
    p.drawString(50, h - (y+40), 'Signature _______________')
    p.showPage()
    p.save()
    return response


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main/SGroupa.html')
        else:
            messages.error(request, 'неподходящий логин')
    return render(request, 'main/login.html')


