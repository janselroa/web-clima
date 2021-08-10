import requests

def clima(ciudad):
	try:
		api_key = 'e0eda8193a6a3795b8e4fe4b8594262f'
		params = {'APPID':api_key, 'q':ciudad,'units':'metric', 'lang':'es'}
		response = requests.get('https://api.openweathermap.org/data/2.5/weather',params=params)
		response_json = response.json()

		temp = response_json['main']['temp']
		description = response_json['weather'][0]['description']
		name = response_json['name']
		datos = [name,description,temp]
		return datos
	except:
		return ['Error']


def limpiar_str(string):
	caracteres = '<>/$#@%&!'
	for i in caracteres:
		string = string.replace(i,'')
	return string

