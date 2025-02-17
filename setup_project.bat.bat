@echo off
REM Získání cesty, ve které je BAT soubor spuštěn
set PROJECT_ROOT=%~dp0

REM Vytvoření složek pro šablony a statické soubory
mkdir "%PROJECT_ROOT%templates"
mkdir "%PROJECT_ROOT%static"
mkdir "%PROJECT_ROOT%static\css"
mkdir "%PROJECT_ROOT%static\js"
mkdir "%PROJECT_ROOT%templates\WEBhodina11_2"

REM Vytvoření základních souborů
echo. > "%PROJECT_ROOT%templates\WEBhodina11_2\index.html"
echo. > "%PROJECT_ROOT%static\css\styles.css"
echo. > "%PROJECT_ROOT%static\js\script.js"

REM Vytvoření urls.py pro aplikaci
echo from django.urls import path > "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo from . import views >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo urlpatterns = [path('', views.index, name='index')] >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"

REM Aktualizace views.py
echo from django.shortcuts import render > "%PROJECT_ROOT%WEBhodina11_2\views.py"
echo. >> "%PROJECT_ROOT%WEBhodina11_2\views.py"
echo def index(request): >> "%PROJECT_ROOT%WEBhodina11_2\views.py"
echo     return render(request, 'WEBhodina11_2/index.html') >> "%PROJECT_ROOT%WEBhodina11_2\views.py"

REM Aktualizace hlavního urls.py
echo from django.contrib import admin > "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo from django.urls import include, path >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo. >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo urlpatterns = [ >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo     path('admin/', admin.site.urls), >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo     path('', include('WEBhodina11_2.urls')), >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"
echo ] >> "%PROJECT_ROOT%WEBhodina11_2\urls.py"

REM Aktualizace settings.py
echo import os >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo. >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo TEMPLATES = [ >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo     { >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo         'BACKEND': 'django.template.backends.django.DjangoTemplates', >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo         'DIRS': [os.path.join(BASE_DIR, 'templates')], >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo         'APP_DIRS': True, >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo         'OPTIONS': { >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo             'context_processors': [ >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo                 'django.template.context_processors.debug', >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo                 'django.template.context_processors.request', >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo                 'django.contrib.auth.context_processors.auth', >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo                 'django.contrib.messages.context_processors.messages', >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo             ], >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo         }, >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo     }, >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo ] >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo. >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo STATIC_URL = '/static/' >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"
echo STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] >> "%PROJECT_ROOT%WEBhodina11_2\settings.py"

REM Dokončení
echo Struktura projektu byla úspěšně nastavena!
pause