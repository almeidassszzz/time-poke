from django.shortcuts import render
import requests
import json


def index(request):
    return render(request, 'index.html', {})


def time(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'

    time = [
        {'id': 249, 'nome': 'Lugia'},
        {'id': 6, 'nome': 'Charizard'},
        {'id': 384, 'nome': 'Rayquaza'},
        {'id': 389, 'nome': 'Torterra'},
        {'id': 245, 'nome': 'Suicune'},
        {'id': 778, 'nome': 'Mimikyu'},
    ]

    for i in time:
        url_completa = url + str(i['id'])
        dados = requests.get(url_completa).json()
        i['imagem'] = dados['sprites']['front_default']

    equipe = time
        
    return render(request, 'time.html', {'equipe': equipe})


def lugia(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'lugia'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_lugia = response.json()

    context = {
        'nome': dados_lugia['name'].capitalize(),
        'id': dados_lugia['id'],
        'tipos': [i['type']['name'] for i in dados_lugia['types']],
    }

    return render(request, 'lugia.html', context)


def charizard(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'charizard'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_charizard = response.json()

    context = {
        'nome': dados_charizard['name'].capitalize(),
        'id': dados_charizard['id'],
        'tipos': [i['type']['name'] for i in dados_charizard['types']],
    }

    return render(request, 'charizard.html', context)


def rayquaza(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'rayquaza'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_rayquaza = response.json()

    context = {
        'nome': dados_rayquaza['name'].capitalize(),
        'id': dados_rayquaza['id'],
        'tipos': [i['type']['name'] for i in dados_rayquaza['types']],
    }

    return render(request, 'rayquaza.html', context)


def torterra(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'torterra'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_torterra = response.json()

    context = {
        'nome': dados_torterra['name'].capitalize(),
        'id': dados_torterra['id'],
        'tipos': [i['type']['name'] for i in dados_torterra['types']],
    }

    return render(request, 'torterra.html', context)


def suicune(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'suicune'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_suicune = response.json()

    context = {
        'nome': dados_suicune['name'].capitalize(),
        'id': dados_suicune['id'],
        'tipos': [i['type']['name'] for i in dados_suicune['types']],
    }

    return render(request, 'suicune.html', context)


def mimikyu(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'mimikyu'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_mimikyu = response.json()

    context = {
        'nome': dados_mimikyu['name'].capitalize(),
        'id': dados_mimikyu['id'],
        'tipos': [i['type']['name'] for i in dados_mimikyu['types']],
    }

    return render(request, 'mimikyu.html', context)