import time
from graphics_lib import GraphicsLib

# Configuración de la pantalla
sck_pin = 14
mosi_pin = 13
cs_pin = 15
dc_pin = 2
rst_pin = 4
width = 320
height = 240

# Crear una instancia de la librería GraphicsLib
graphics = GraphicsLib(sck_pin, mosi_pin, cs_pin, dc_pin, rst_pin, width, height)

# Barra de progreso con graphics_lib
for i in range(101):
    graphics.draw_progress_bar(50, 150, 200, 20, i / 100, graphics.green)  # Actualiza el progreso
    time.sleep(0.1)
