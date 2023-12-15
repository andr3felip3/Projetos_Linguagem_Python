# Geocoder: é uma api do google que pode ser utilizada por meio do maps para encontrar a localização de um ponto

from pygeocoder import Geocoder #necessário importar a classe Geocoder

endereco = '1222, Lins de vasconcelos, São Paulo, SP' # endereço da FIAP

print(Geocoder('AIzaSyAIY0coggbhzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco).coordinates) # retorna as coordenadas

# sintaxe do geocoder: Geocoder('chave').geocode('endereco').constantes

## a chave: é uma ferramenta de acesso definido pelo site da google cloud
### endereçoe: é uma string contendo nº,rua,cidade,Estado


#------ Não deu certo esse script pois não consegui a chave de acesso, nem instalar direito o geocoder ---#

from pygeocoder import Geocoder
endereco = 'Avenida paulista, 100 Sao Paulo'
resultado = Geocoder('AIzaSyAIY0coggbhzTCe5rGF86FLUKXWKw2yPMM').geocode(endereco)
print(resultado)

                 ##---- Metodos geocode ----##
# geocode(endereco): retorna o enderço de acordo com a base de dados do geocode
# geocode(endereco).state(): retorna o estado
# geocode(endereco).country(): retorna o pais
# geocode(endereco).cordinates(): retorna as coordenadas
# reverse_geocode(lat,long): retorna o endereço por meio da lat e long