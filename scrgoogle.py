import urllib
from requests_html  import HTMLSession


def get_source(url):
    session = HTMLSession()
    response = session.get(url)
    return response


def parse_results(response):

    css_identifier_resultado = ".tF2Cxc"
    css_identifier_titulo = "h3"
    css_identifier_enlace = ".yuRUbf a"
    css_identifier_texto = ".IsZvec"

    results = response.html.find(css_identifier_resultado)

    output = []

    for result in results:
        item = {
            'titulo':result.find(css_identifier_titulo, first=True).text,
            'enlace':result.find(css_identifier_enlace, first=True).attrs['href'],
            'texto':result.find(css_identifier_texto, first=True).text
        }

        output.append(item)
    
    return output
    



def google_search(query):
    
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com.ar/search?q="+query+"&num=100")

    return parse_results(response)


texto_a_buscar = input("Que desea buscar? ").lower()

resultado_final = google_search(texto_a_buscar)

contador = 0
for resultado in resultado_final:
    contador += 1
    print("---Resultado # ",contador)

    print(resultado.get('titulo'),resultado.get('enlace'))
    print(resultado.get('texto'))
    print("------------------------------------")