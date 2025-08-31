"""
Generador de números aleatorios para el juego Dudo.
"""

import random


class GeneradorAleatorio:
    
    @staticmethod
    def generar(min_val=1, max_val=6):
        """
        Genera un número aleatorio entre min_val y max_val.
        
        Args:
            min_val (int): Valor mínimo (por defecto 1)
            max_val (int): Valor máximo (por defecto 6)
            
        Returns:
            int: Número aleatorio generado
        """
        return random.randint(min_val, max_val)
