from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.
def weather(request):
    if request.method == 'POST':
        # Here you would typically handle the POST request data
        city = request.POST['city']
        source = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=impereial&appid=9eeb671c6507280051b8eecd51c8abff'
        list_of_data = requests.get(source.format(city)).json()

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            'temp': round((list_of_data['main']['temp'] - 32) * 5/9, 2),
            'humidity': str(list_of_data['main']['humidity']),
            'pressure': str(list_of_data['main']['pressure']),
        }
    else:
        data = {}
        return render(request, 'weather_app.html', data)