# Kita akan belajar API
import requests

# .get untuk mengakses urlnya
response = requests.get(url='http://api.open-notify.org/iss-now.json')
print(response)
# kita juga bisa menambahkan .status_code untuk lebih jelas
print(response.status_code)
#output : response 200

# ini isi datanya
data = response.json()
print(data)
print(data['iss_position']['latitude'])

# Jenis jenis response
# 1xx = hold on
# 2xx = success
# 3xx = pergi lu
# 4xx = masalah ada di programmer
# 5xx = masalah ada di server


# Coba praktik yuk
# API with parameter
my_lat = 106.981327
my_long = -6.235298
format = 'ISO 8601:1988'
time = ' Asia/Hong_Kong'
city = "bekasi city"

parameters = {
    'lat': my_lat,
    'lng': my_long,
    'formatted': format,
    'tzid': time
}

response = requests.get(url = 'https://api.sunrise-sunset.org/json', params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunset']
sunset = data['results']['sunset']
print(f'Sunset at {sunset} in {city}')
