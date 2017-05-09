import requests
from bs4 import BeautifulSoup
import urllib.request


def run():
	for i in range(1, 6):
		# hacemos la solicitud de un comic
		response = requests.get('https://xkcd.com/{}'.format(i))
		
		# parseamos el contenido de la respuesta, usando un parser html
		soup = BeautifulSoup(response.content, 'html.parser')
		
		# obtenemos el container de la imagen del comic
		image_container = soup.find(id = 'comic')

		# encontramos el tag de la imagen y accedemos a su atributo src
		image_url = image_container.find('img')['src']

		# obtenemos el nombre de la imagen, dividiendo su url por sus diagonales
		# y obteniendo la referencia a su ultima diagonal
		image_name = image_url.split('/')[-1]

		print('Descargando la imagen {}'.format(image_name))

		# guardamos la imagen usando su url y su nombre original
		urllib.request.urlretrieve('https:{}'.format(image_url), image_name)


if __name__ == '__main__':
	run()