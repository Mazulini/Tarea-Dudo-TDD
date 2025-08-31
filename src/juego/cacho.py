"""
Módulo que contiene la clase Cacho para el juego Dudo Chileno.
"""

from src.juego.dado import Dado, Pinta
from src.servicios.generador_aleatorio import GeneradorAleatorio


class Cacho:
    """
    Clase que representa un cacho (vaso de cuero) con dados del juego
    Dudo Chileno.
    """

    def __init__(self):
        """Inicializa un cacho con 5 dados y estado oculto."""
        self._dados = [Dado() for _ in range(5)]
        self._visible = False

    def get_dados(self):
        """
        Retorna una copia de los dados (para el propietario).

        Returns:
            list: Lista con copias de los dados
        """
        return self._dados.copy()

    def agitar(self):
        """
        Agita los dados regenerando sus valores usando el generador aleatorio.
        """
        for dado in self._dados:
            valor = GeneradorAleatorio.generar()
            # Actualizamos la pinta del dado con el nuevo valor
            dado._pinta = Pinta(valor)

    def is_visible(self):
        """
        Retorna si los dados están visibles o no.

        Returns:
            bool: True si los dados están visibles, False si están ocultos
        """
        return self._visible

    def mostrar_dados(self):
        """Hace visibles los dados."""
        self._visible = True

    def ocultar_dados(self):
        """Oculta los dados."""
        self._visible = False

    def get_dados_visibles(self):
        """
        Retorna los dados solo si están visibles (para otros jugadores).

        Returns:
            list: Lista con los dados si están visibles, lista vacía si
                  están ocultos
        """
        if self._visible:
            return self._dados.copy()
        else:
            return []
