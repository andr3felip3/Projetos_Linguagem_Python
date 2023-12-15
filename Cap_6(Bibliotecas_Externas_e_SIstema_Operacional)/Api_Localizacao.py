# Geocoder: � uma api do google que pode ser utilizada por meio do maps para encontrar a localiza��o de um ponto

from pygeocoder import Geocoder #necess�rio importar a classe Geocoder

endereco = '1222, Lins de vasconcelos, S�o Paulo, SP' # endere�o da FIAP

print(Geocoder('AIzaSyAIY0coggbhzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).coordinates) # retorna as coordenadas

# sintaxe do geocoder: Geocoder('chave').geocode('endereco').constantes

## a chave: � uma ferramenta de acesso definido pelo site da google cloud
### endere�oe: � uma string contendo n�,rua,cidade,Estado


#------ N�o deu certo esse script pois n�o consegui a chave de acesso, nem instalar direito o geocoder ---#

from pygeocoder import Geocoder
endereco = 'Avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0coggbhzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco)
print(resultado)

                 ##---- Metodos geocode ----##
# geocode(endereco): retorna o ender�o de acordo com a base de dados do geocode
# geocode(endereco).state(): retorna o estado
# geocode(endereco).country(): retorna o pais
# geocode(endereco).cordinates(): retorna as coordenadas
# reverse_geocode(lat,long): retorna o endere�o por meio da lat e long