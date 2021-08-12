import argparse
import threading
import logging
import time
logger = logging.getLogger(__name__)
from django.db import connection
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
    help = "this is a command import TSE Padron developed in solvo training by Luis Diego Orias A."

    #Comando para procesar el archivo PADRON_COMPLETO.txt o MiPadron.txt

    #Ejecución del comando en windows:

    #python manage.py mycomand "C:\\Users\\USUARIO\\PycharmProjects\\ElectoralRegisterProject\\MyData\\PADRON_COMPLETO.txt"

    #La muestra extraida del padron utilizada fueron 898 lineas y se usarán en total 200 registros para el ejercicio.

    #python manage.py mycomand "C:\\Users\\Xinia Aguilar\\PycharmProjects\\ElectoralRegisterProject\\MyData\\MiPadron.txt" -t 200

    def clean_tables(self):
        """
        Delete all data on database if exists.
        """
        print("Deleting all registry data")
        with connection.cursor() as cursor:
            logger.debug("Execute 'TRUNCATE `padronelectoral_elector`' ")
            # Delete in raw for optimization
            cursor.execute('TRUNCATE `padronelectoral_elector`')

        # Using cascade aproach to delete other tables
        print('province'.objects.all().delete())

    def calculate_speed(self, func, message, *args):
        """
        Calculate the time spend by a function call

        :param func:  Function to call
        :param message: Message to print when time speed is available
        :param args:  Arguments to pass to functions
        """
        start = time.time()
        func(*args)
        end = time.time()
        print("Complete %s in " % message, end - start, " s")


    def add_arguments(self, parser):
        parser.add_argument("diselect", type=argparse.FileType('r', encoding='latin-1'))
        #parser.add_argument("padron", type=argparse.FileType('r', encoding='latin-1'))
        parser.add_argument("-t","--threads", type=int , dest='threads', default=1)

        parser.add_argument('--truncate',dest='truncate',default=200, type=int, help='Max number of elements inserted by statement', )

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

