
class CovidDataServices:
    def get_countries_data(countries):
        pass

    def get_countries_historic_data(countries,start_date,end_date):
        pass
      


# Clase Adaptador que adapta los datos de la aplicación al formato CSV requerido por la librería de graficación de terceros
class Adaptador(CovidDataServices):

    def transformar_a_csv(datos_json):
    # Código para transformar los datos de JSON a CSV
        pass

# Librería de graficación de terceros que requiere datos en formato CSV
class CSVPlotter(Adaptador):
    def plot_data(csv_data):
        return image

    
class app: 
    def __init__():
        pass
        



