import requests
from bs4 import BeautifulSoup
import Funciones_Scrapper
import re

page = requests.get("https://www.normacomics.com/guardianes-de-la-noche-11.html")
soup= BeautifulSoup(page.content,'html.parser')


#print(soup.encode("utf-8"))

result=soup.select_one('span[class="price"][id*="product-price-"]')

precioActual_texto=result.text.split()
precioActual_texto=precioActual_texto[0]
precioActual_texto_Limpio1 = precioActual_texto.replace('€', '')
precioActual_texto_Limpio2 = precioActual_texto_Limpio1.replace('\n','')
precioActual_texto_Limpio3 = precioActual_texto_Limpio2.replace(',','.')

precioActual=float(precioActual_texto.replace(",","."))
print('Analizando los datos...')


#Establecemos el precio deseado
precioDeseado = 7
global HayOferta
#Calcula el precio
print ("\nEl precio máximo deseado para este producto es de "+ str(precioDeseado)+"€\n")

global hayOferta
#Calcula el precio
import Funciones_Scrapper
hayOferta = Funciones_Scrapper.Oferta_Precio_Deseado(precioActual,precioDeseado)

if(hayOferta):
    print("Tenemos OFERTA! - Avisamos al usuario!")
    #avisar por telegram
    import Aviso_Telegram
    Aviso_Telegram
else:
    print("No hay oferta.")

#2089233941:AAFA_md4pvCXgVCB68wkhiOBLc4POIlcDPA
#735937105




