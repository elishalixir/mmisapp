from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import NewRegistration, MapForm, LoginForm, EnergyFuelForm, CementForm, EnvironmentAndHealthForm,\
    ASGMiningForm
from .models import MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement, EnvironmentAndHealth,\
    ASGMining
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request, 'mmis_app/welcome.html')


def sign_up(request):
    if request.method == 'POST':
        form = NewRegistration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #msg = 'Please Contact Admin for Sector Activation!' I need this msg to
            # display on first login
            return redirect('/welcome')
    else:
        form = NewRegistration()
        return render(request, 'registration/sign_up.html', {'form': form})

    return render(request, 'registration/login.html')


def login_view(request):
    form = LoginForm(request.POST)
    msg = ''
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_health:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_cement:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_asgm:
                login(request, user)
                return redirect('welcome')
            elif user is not None and user.is_EandF:
                login(request, user)
                return redirect('welcome')
            if user is not None and user.is_map:
                login(request, user)
                return redirect('welcome')

            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'registration/login.html', {'form': form, 'msg': msg})


@login_required(login_url='/login')
def welcome(request):
    return render(request, 'mmis_app/welcome.html')


# MercuryAddedProducts


# READ
@login_required(login_url='/login')
def map_read(request):
    context = {'map_read': MercuryAddedProducts.objects.all()}
    return render(request, 'mmis_app/map/map_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def map_create(request):
    if request.method == 'POST':
        form = MapForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/feedback')
            except:
                pass
    else:
        form = MapForm()
    return render(request, "mmis_app/map/map_create.html", {'form': form})


# EDIT
@login_required(login_url='/login')
def map_edit(request, id):
    map = MercuryAddedProducts.objects.get(id=id)
    return render(request, "mmis_app/map/map_edit.html", {'map': map})


@login_required(login_url='/login')
def map_update(request, id):
    map = MercuryAddedProducts.objects.get(id=id)
    form = MapForm(request.POST, instance=map)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/map_read')
        except:
            pass
    return render(request, "mmis_app/map/map_edit.html", {'form': form})


# DELETE
@login_required(login_url='/login')
def map_delete(request, id):
    map = MercuryAddedProducts.objects.get(id=id)
    map.delete()
    return redirect('/map_read')


# @login_required(login_url='/login')
def contact(request):
    pass


# @login_required(login_url='/login')
def feedback(request):
    return render(request, "mmis_app/feedback.html")


@login_required(login_url='/login')
def health(request):
    pass


@login_required(login_url='/login')
# @permission_required('ASGMElisha', raise_exception=True)
def Asgm(request):
    pass


@login_required(login_url='/login')
def cement_sector(request):
    pass


@login_required(login_url='/login')
def energy_fuel(request):
    pass


@login_required(login_url='/login')
def ecfp_read(request):
    context = {'ecfp_read': EnergyConsumptionAndFuelProduction.objects.all()}
    return render(request, 'mmis_app/energyfuel/ecfp_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def ecfp_create(request):
    if request.method == 'POST':
        form = EnergyFuelForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/feedback')
            except:
                pass
    else:
        form = EnergyFuelForm()
    return render(request, "mmis_app/energyfuel/ecfp_create.html", {'form': form})


# EDIT
@login_required(login_url='/login')
def ecfp_edit(request, id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(id=id)
    return render(request, "mmis_app/energyfuel/ecfp_edit.html", {'ecfp': ecfp})


@login_required(login_url='/login')
def ecfp_update(request, id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(id=id)
    form = EnergyFuelForm(request.POST, instance=ecfp)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/ecfp_read')
        except:
            pass
    return render(request, "mmis_app/energyfuel/ecfp_edit.html", {'form': form})


# DELETE
@login_required(login_url='/login')
def ecfp_delete(request, id):
    ecfp = EnergyConsumptionAndFuelProduction.objects.get(id=id)
    ecfp.delete()
    return redirect('/ecfp_read')


# cement
@login_required(login_url='/login')
def cem_read(request):
    context = {'cem_read': Cement.objects.all()}
    return render(request, 'mmis_app/cement/cem_read.html', context)


# CREATE/UPDATE
@login_required(login_url='/login')
def cem_create(request):
    if request.method == 'POST':
        form = CementForm(request.POST)
        if form.is_valid():
            try:
                temporal = form.save(commit=False)
                temporal.author = request.user
                temporal.save()
                return redirect('/feedback')
            except:
                pass
    else:
        form = CementForm()
    return render(request, "mmis_app/cement/cem_create.html", {'form': form})


# EDIT
@login_required(login_url='/login')
def cem_edit(request, id):
    cem = Cement.objects.get(id=id)
    return render(request, "mmis_app/cement/cem_edit.html", {'cem': cem})


@login_required(login_url='/login')
def cem_update(request, id):
    cem = Cement.objects.get(id=id)
    form = CementForm(request.POST, instance=cem)
    if form.is_valid():
        try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            print(form.errors)
            return redirect('/cem_read')
        except:
            pass
    return render(request, "mmis_app/cement/cem_edit.html", {'form': form})


# DELETE
@login_required(login_url='/login')
def cem_delete(request, id):
    cem = Cement.objects.get(id=id)
    cem.delete()
    return redirect('/cem_read')


# Environment and Health
# @login_required(login_url='/login')
def eAndH_read(request):
    context = {'eAndH_read': EnvironmentAndHealth.objects.all()}
    return render(request, 'mmis_app/envHealth/eAndH_read.html', context)


# CREATE/UPDATE
# @login_required(login_url='/login')
def eAndH_create(request):
    if request.method == 'POST':
        form = EnvironmentAndHealthForm(request.POST)
        if form.is_valid():
            # try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            return redirect('/feedback')
        # except:
        #     pass
    else:
        form = EnvironmentAndHealthForm()
    return render(request, "mmis_app/envHealth/eAndH_create.html", {'form': form})


# EDIT
# @login_required(login_url='/login')
def eAndH_edit(request, id):
    eAndH = EnvironmentAndHealth.objects.get(id=id)
    return render(request, "mmis_app/envHealth/eAndH_edit.html", {'eAndH': eAndH})


# @login_required(login_url='/login')
def eAndH_update(request, id):
    eAndH = EnvironmentAndHealth.objects.get(id=id)
    form = EnvironmentAndHealthForm(request.POST, instance=eAndH)
    if form.is_valid():
        temporal = form.save(commit=False)
        temporal.author = request.user
        temporal.save()
        print(form.errors)
        return redirect('/eAndH_read')
    # except:
    #     pass
    return render(request, "mmis_app/envHealth/eAndH_edit.html", {'form': form})


# DELETE
# @login_required(login_url='/login')
def eAndH_delete(request, id):
    eAndH = EnvironmentAndHealth.objects.get(id=id)
    eAndH.delete()
    return redirect('/eAndH_read')


# ASG MINING
# @login_required(login_url='/login')
def asgm_read(request):
    context = {'asgm_read': ASGMining.objects.all()}
    return render(request, 'mmis_app/mining/asgm_read.html', context)


# CREATE/UPDATE
# @login_required(login_url='/login')
def asgm_create(request):
    if request.method == 'POST':
        form = ASGMiningForm(request.POST)
        if form.is_valid():
            # try:
            temporal = form.save(commit=False)
            temporal.author = request.user
            temporal.save()
            return redirect('/asgm_read')
        # except:
        #     pass
    else:
        form = ASGMiningForm()
    return render(request, "mmis_app/mining/asgm_create.html", {'form': form})


# EDIT
# @login_required(login_url='/login')
def asgm_edit(request, id):
    asgm = ASGMining.objects.get(id=id)
    return render(request, "mmis_app/mining/asgm_edit.html", {'asgm': asgm})


# @login_required(login_url='/login')
def asgm_update(request, id):
    asgm = ASGMining.objects.get(id=id)
    form = ASGMiningForm(request.POST, instance=asgm)
    if form.is_valid():
        temporal = form.save(commit=False)
        temporal.author = request.user
        temporal.save()
        print(form.errors)
        return redirect('/asgm_read')
    # except:
    #     pass
    return render(request, "mmis_app/mining/asgm_edit.html", {'form': form})


# DELETE
# @login_required(login_url='/login')
def asgm_delete(request, id):
    asgm = ASGMining.objects.get(id=id)
    asgm.delete()
    return redirect('/asgm_read')
