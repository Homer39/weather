from django.shortcuts import render
import requests


def weather(request):
    api = '357c40dd0278fa6dbeeb1dfab10d3303'
    city = "Paris"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api}'

    response = requests.get(url).json()
#    print(response)
    data = {
            'temp': response['main']['temp'],
            'humidity': response['main']['humidity'],
            'wind': response['wind']['speed'],
            'deg': response['wind']['deg']
            }
    context = {'data': data}
    return render(request, 'weather/main.html', context)