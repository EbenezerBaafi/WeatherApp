from django.shortcuts import render
import requests
import os

# Create your views here.
def weather(request):
    data = {}
    if request.method == 'POST':
        city = request.POST.get('city', '').strip()
        if city:
            api_key = os.environ.get('OPENWEATHER_API_KEY', '9eeb671c6507280051b8eecd51c8abff')
            source = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
            try:
                resp = requests.get(source.format(city, api_key), timeout=5)
                resp.raise_for_status()
                payload = resp.json()

                # API returns cod as int or string; handle non-200 responses
                if str(payload.get('cod')) != '200':
                    data['error'] = payload.get('message', 'City not found')
                else:
                    data = {
                        'city': city,
                        'country_code': payload['sys'].get('country', ''),
                        'coordinate': f"{payload['coord'].get('lon', '')} {payload['coord'].get('lat', '')}",
                        'temp': round(payload['main'].get('temp', 0), 2),  # metric => Celsius
                        'humidity': payload['main'].get('humidity', ''),
                        'pressure': payload['main'].get('pressure', ''),
                    }
            except requests.RequestException:
                data['error'] = 'Network error. Please try again.'
            except Exception:
                data['error'] = 'Unexpected error. Please try again.'
        else:
            data['error'] = 'Please enter a city name.'

        return render(request, 'weather_app.html', data)

    # GET
    return render(request, 'weather_app.html', data)
