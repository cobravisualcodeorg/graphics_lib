# graphics_lib.py v.1
#cobravisualcode.org
#Descarga ILI9341 en  https://github.com/rdagger/micropython-ili9341

from machine import Pin, SPI
from ILI9341 import Display, color565
import time
import ustruct
import os


class GraphicsLib:
    def __init__(self, sck_pin, mosi_pin, cs_pin, dc_pin, rst_pin, width, height, backlight_pin=21):
        """
        Configura la pantalla TFT y el SPI para comunicarse con ella.
        """
        self.width = width  
        self.height = height  

        # Inicializa la comunicación SPI
        self.spi = SPI(1, baudrate=60000000, sck=Pin(sck_pin), mosi=Pin(mosi_pin))
        
        # Configura la pantalla TFT
        self.display = Display(self.spi, dc=Pin(dc_pin), cs=Pin(cs_pin), rst=Pin(rst_pin), width=self.width, height=self.height, rotation=180)

        # Configuración de la retroiluminación
        self.backlight = Pin(backlight_pin, Pin.OUT)
        self.backlight.on()  # Asegúrate de que la retroiluminación esté encendida al iniciar
        
        # Colores estándar
        self.white = color565(255, 255, 255)
        self.black = color565(0, 0, 0)
        self.red = color565(255, 0, 0)
        self.green = color565(0, 255, 0)
        self.blue = color565(0, 0, 255)
        self.yellow = color565(255, 255, 0)
        self.cyan = color565(0, 255, 255)
        self.magenta = color565(255, 0, 255)

        # Inicializar el estado de la pantalla
        self.clear_screen(self.black)
    
    
 
    
    
    
    
    
    
    
    
    def clear_screen(self, color):
        
        try:
            self.display.fill_rectangle(0, 0, self.width, self.height, color)
        except Exception as e:
            print(f"Error al limpiar la pantalla: {e}")

    def draw_text(self, x, y, text, color):
       
        try:
            self.display.draw_text8x8(x, y, text, color)
        except Exception as e:
            print(f"Error al dibujar texto: {e}")

    def draw_button(self, x, y, width, height, color, label, text_color=None):
        """ Dibuja un botón en la pantalla """
        try:
            if text_color is None:
                text_color = self.white

            # Dibuja el rectángulo del botón
            self.display.fill_rectangle(x, y, width, height, color)
            
            # Dibuja el texto del botón centrado
            text_x = x + (width // 2) - (len(label) * 8 // 2)
            text_y = y + (height // 2) - 8
            self.display.draw_text8x8(text_x, text_y, label, text_color)
        except Exception as e:
            print(f"Error al dibujar el botón: {e}")

    def draw_rectangle(self, x, y, width, height, color):
        """ Dibuja un rectángulo en las coordenadas especificadas """
        try:
            self.display.fill_rectangle(x, y, width, height, color)
        except Exception as e:
            print(f"Error al dibujar el rectángulo: {e}")

    def draw_line(self, x1, y1, x2, y2, color):
        """ Dibuja una línea entre dos puntos """
        try:
            self.display.draw_line(x1, y1, x2, y2, color)
        except Exception as e:
            print(f"Error al dibujar la línea: {e}")

    def update_screen(self):
        """ Actualiza la pantalla con los cambios realizados (si es necesario) """
        pass  # La pantalla se actualiza automáticamente con las funciones de dibujo.

    def enable_backlight(self):
        """ Enciende la retroiluminación """
        try:
            self.backlight.on()
        except Exception as e:
            print(f"Error al encender la retroiluminación: {e}")

    def disable_backlight(self):
        """ Apaga la retroiluminación """
        try:
            self.backlight.off()
        except Exception as e:
            print(f"Error al apagar la retroiluminación: {e}")

    def draw_image(self, x, y, image_data):
        """ Dibuja una imagen en la pantalla desde datos binarios """
        try:
            self.display.draw_image(x, y, image_data)
        except Exception as e:
            print(f"Error al dibujar la imagen: {e}")

    def draw_circle(self, x, y, radius, color):
        """ Dibuja un círculo """
        try:
            self.display.draw_circle(x, y, radius, color)
        except Exception as e:
            print(f"Error al dibujar el círculo: {e}")

    def draw_ellipse(self, x, y, a, b, color):
        """ Dibuja una elipse """
        try:
            self.display.draw_ellipse(x, y, a, b, color)
        except Exception as e:
            print(f"Error al dibujar la elipse: {e}")

    def get_screen_size(self):
        """ Devuelve el tamaño de la pantalla como una tupla (ancho, alto) """
        return (self.width, self.height)

    def draw_progress_bar(self, x, y, width, height, progress, color):
        """ Dibuja una barra de progreso """
        try:
            bar_width = int(width * progress)
            self.display.fill_rectangle(x, y, bar_width, height, color)
        except Exception as e:
            print(f"Error al dibujar la barra de progreso: {e}")
            
  
    
