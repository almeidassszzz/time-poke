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
        i['imagem'] = dados['sprites']['other']['official-artwork']['front_default']

    equipe = time
        
    return render(request, 'time.html', {'equipe': equipe})



def lugia(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'lugia'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_lugia = response.json()

    context = {
        'imagem': dados_lugia['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_lugia['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_lugia['types']],
        'altura': f'{dados_lugia['height'] * 10}cm',
        'peso': f'{dados_lugia['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_lugia['stats']},
    }

    return render(request, 'lugia.html', context)



def charizard(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'charizard'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_charizard = response.json()

    context = {
        'imagem': dados_charizard['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_charizard['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_charizard['types']],
        'altura': f'{dados_charizard['height'] * 10}cm',
        'peso': f'{dados_charizard['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_charizard['stats']},
    }

    return render(request, 'charizard.html', context)

#mega do charizard
def mega_charizard(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    id = 10034
    url_completa = url + str(id)
    response = requests.get(url_completa)
    dados_mega_charizard = response.json()

    context = {
        'imagem': dados_mega_charizard['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_mega_charizard['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_mega_charizard['types']],
        'altura': f'{dados_mega_charizard['height'] * 10}cm',
        'peso': f'{dados_mega_charizard['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_mega_charizard['stats']},
    }

    return render(request, 'mega_charizard.html', context)



def rayquaza(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'rayquaza'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_rayquaza = response.json()

    context = {
        'imagem': dados_rayquaza['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_rayquaza['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_rayquaza['types']],
        'altura': f'{dados_rayquaza['height'] * 10}cm',
        'peso': f'{dados_rayquaza['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_rayquaza['stats']},
    }

    return render(request, 'rayquaza.html', context)

#mega do rayquaza
def mega_rayquaza(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    id = 10079
    url_completa = url + str(id)
    response = requests.get(url_completa)
    dados_mega_rayquaza = response.json()

    context = {
        'imagem': dados_mega_rayquaza['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_mega_rayquaza['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_mega_rayquaza['types']],
        'altura': f'{dados_mega_rayquaza['height'] * 10}cm',
        'peso': f'{dados_mega_rayquaza['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_mega_rayquaza['stats']},
    }

    return render(request, 'mega_rayquaza.html', context)



def torterra(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'torterra'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_torterra = response.json()

    context = {
        'imagem': dados_torterra['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_torterra['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_torterra['types']],
        'altura': f'{dados_torterra['height'] * 10}cm',
        'peso': f'{dados_torterra['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_torterra['stats']},
    }

    return render(request, 'torterra.html', context)



def suicune(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'suicune'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_suicune = response.json()

    context = {
        'imagem': dados_suicune['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_suicune['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_suicune['types']],
        'altura': f'{dados_suicune['height'] * 10}cm',
        'peso': f'{dados_suicune['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_suicune['stats']},
    }

    return render(request, 'suicune.html', context)



def mimikyu(request):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    nome = 'mimikyu-disguised'
    url_completa = url + nome
    response = requests.get(url_completa)
    dados_mimikyu = response.json()

    context = {
        'imagem': dados_mimikyu['sprites']['other']['official-artwork']['front_default'],
        'nome': dados_mimikyu['name'].capitalize(),
        'tipos': [i['type']['name'].upper() for i in dados_mimikyu['types']],
        'altura': f'{dados_mimikyu['height'] * 10}cm',
        'peso': f'{dados_mimikyu['weight'] / 10}kg',
        'status': {i['stat']['name'].replace('-', '_'): i['base_stat'] for i in dados_mimikyu['stats']},
    }

    return render(request, 'mimikyu.html', context)