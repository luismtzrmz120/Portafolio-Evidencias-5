import logging
import concurrent.futures
import time

def thread_function(name):
    logging.info("Thread %s; starting", name)
    time.sleep(2)
    logging.info("Thread %s; finishing", name)

if __name__ == "__main__":
    format = "%(asctimes: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S") 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(thread_function, range(5))
    logging.info("Main program finishing...")

  
"""
¿Qué es un ThreadPoolExecutor y para qué sirve? 

es una interfaz que ayuda a la ejecucion de varios procesos mediante hilos de los diferentes main 

¿Qué ventajas tiene usar un ThreadPoolExecutor sobre usar solamente la librería threading? 

con el ThreadPoolExecutor podemos inicar, cerrar, enviar, ejecutar y bloquear la terminación de las funciones de forma más eficiente o menos eficiente, lo cual lo hace más "completo" o "complejo" a diferencia del threading

Pega el resultado de la ejecución del programa

15;55;45; Main   : create and start thread 0.
15;55;45; Thread 0; starting
15;55;45; Main   : create and start thread 1.
15;55;45; Thread 1; starting
15;55;45; Main   : create and start thread 2.
15;55;45; Thread 2; starting
15;55;45; Main   : before joining thread 0.
15;55;47; Thread 0; finishing
15;55;47; Main   : thread 0 done.
15;55;47; Main   : before joining thread 1.
15;55;47; Thread 1; finishing
15;55;47; Main   : thread 1 done.
15;55;47; Main   : before joining thread 2.
15;55;47; Thread 2; finishing
15;55;47; Main   : thread 2 done.

Investiga y reporta. En computación, qué significa asíncronoy cómo se relaciona con nuestro tema de hoy? 

asíncrona es un método de intercambio de mensajes entre dos o más partes, en la que cada parte recibe y procesa el mensaje cuando sea conveniente o posible de realizar, en vez de hacerlo inmediatamente al recibirlo
La manera en que se relaciona es como lo podemos ver en nuestra consola, los hilos se despliegan de forma asincronica

"""

  
