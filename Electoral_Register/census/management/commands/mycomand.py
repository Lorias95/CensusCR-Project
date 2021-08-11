import argparse
import threading
from django.core.management.base import BaseCommand

def procesar_archivos(options, numthread, contador, max_contador, resultado):
    #print(numthread, options['diselec'].read())

    lineas = []
    for linea in options['diselec']:
        lineas.append(linea)
        contador += 1
        if contador == max_contador:
            print(numthread, "-- Procesando %d elementos (%d, %d)"% (len(lineas), contador, max_contador))
            return
    resultado.append(True)
    if lineas:
        print(numthread, "-- Procesando %d elementos (%d, %d)"% (len(lineas), contador, max_contador))
    return


class Command(BaseCommand):
    help = "this is a command import tse padron developed in solvo training by Luis Diego Orias A."

    #Comando para procesar el archivo PADRON.txt o MiPadron.txt

    #python manage.py mycomand "C:\\Users\\USUARIO\\PycharmProjects\\ElectoralRegisterProject\\MyData\\PADRON_COMPLETO.txt"

    #Muestra del Padron Utilizada en total 200 registros para el ejercicio.

    #python manage.py mycomand "C:\\Users\\Xinia Aguilar\\PycharmProjects\\ElectoralRegisterProject\\MyData\\MiPadron.txt" -t 200

    def add_arguments(self, parser):
        parser.add_argument("diselect", type=argparse.FileType('r', encoding='latin-1'))
        #parser.add_argument("padron", type=argparse.FileType('r', encoding='latin-1'))
        parser.add_argument("-t","--threads", type=int , dest='threads', default=1)

    def handle(self, *args, **options):
        #print(args, options)

        print(type(options["diselect"].readlines()))
        return
        #with open('C:\\Users\\Xinia Aguilar\\PycharmProjects\\ElectoralRegisterProject\\MiPadron.txt', 'r', encoding='latin-1') as arch:
         #   print(arch.read())
    max_thread = 3
    resultado = []

    while len(resultado) == max_thread and not all(resultado):
        list_threads = []
        for x in range(max_thread):
            t = threading.Thread(target=procesar_archivos, args=('options',x, 100*x, 100*(x+1), resultado))
            list_threads.append(t)
            t.start()

        for x in list_threads:
            x.join()

