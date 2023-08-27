import qrcode
from django.http import HttpResponse
from django.shortcuts import render
import wifi_qrcode_generator.generator

from django.conf import settings
from .form import *



# Create your views here.
def home(request):
    return render(request, 'qrCode/index.html')


def wifi(request):
    if request.method == 'POST':
        form  = wifiForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            hide = form.cleaned_data['hidden']
            password = form.cleaned_data['password']

            qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
                ssid=name, hidden=hide, authentication_type='WPA', password=password
            )
            # qr_code.print_ascii()
            img = qr_code.make_image()
            imgName = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)


            return render(request, 'qrCode/wifi-code.html', {'qrcode': imgName, 'form': form})
    else:
        form = wifiForm()

    return render(request, 'qrCode/wifi-code.html', {'form': form})

def link(request):
    if request.method == 'POST':
        form = linkForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['item']
            img = qrcode.make(item)
            imgName = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)

            return render(request, 'qrCode/link.html', {'qrcode': imgName, 'form': form})
    else:
        form = linkForm()

    return render(request, 'qrCode/link.html', {'form': form})

def telegram(request):
    if request.method == 'POST':
        form = telegramForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['item']
            img = qrcode.make(f"https://t.me/{item}")
            imgName = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)

            return render(request, 'qrCode/link.html', {'qrcode': imgName, 'form': form})
    else:
        form = telegramForm()

    return render(request, 'qrCode/link.html', {'form': form})

def instagram(request):
    if request.method == 'POST':
        form = instagramForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['item']
            img = qrcode.make(f"https://instagram.com/{item}")
            imgName = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)

            return render(request, 'qrCode/link.html', {'qrcode': imgName, 'form': form})
    else:
        form = instagramForm()

    return render(request, 'qrCode/link.html', {'form': form})

def twitter(request):
    if request.method == 'POST':
        form = twitterForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['item']
            img = qrcode.make(f"https://twitter.com/{item}")
            imgName = 'qr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)

            return render(request, 'qrCode/link.html', {'qrcode': imgName, 'form': form})
    else:
        form = twitterForm()

    return render(request, 'qrCode/link.html', {'form': form})

def facebook(request):
    if request.method == 'POST':
        form = facebookForm(request.POST)

        if form.is_valid():
            item = form.cleaned_data['item']
            img = qrcode.make(f"https://instagram.com/{item}")
            imgName = 'qrr' + '.png'
            img_path = str(settings.MEDIA_ROOT) + str(f'/{imgName}')
            img.save(img_path)

            return render(request, 'qrCode/link.html', {'qrcode': imgName, 'form': form})
    else:
        form = facebookForm()

    return render(request, 'qrCode/link.html', {'form': form})