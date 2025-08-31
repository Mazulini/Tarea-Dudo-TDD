"""
Tests para la clase Cacho del juego Dudo Chileno.
"""

import pytest
from unittest.mock import Mock, patch

from src.juego.cacho import Cacho
from src.juego.dado import Dado, Pinta


class TestCacho:
    """Tests para la clase Cacho."""
    
    def test_cacho_se_puede_crear(self):
        """Test que verifica que se puede crear una instancia de Cacho."""
        cacho = Cacho()
        assert cacho is not None
    
    def test_cacho_tiene_cinco_dados(self):
        """Test que verifica que un cacho contiene exactamente 5 dados."""
        cacho = Cacho()
        dados = cacho.get_dados()
        assert len(dados) == 5
        for dado in dados:
            assert isinstance(dado, Dado)
    
    @patch('src.servicios.generador_aleatorio.GeneradorAleatorio.generar')
    def test_cacho_agitar_cambia_dados_usando_generador(self, mock_generar):
        """Test que verifica que agitar usa el generador aleatorio para cambiar los dados."""
        # Configurar el mock para retornar valores específicos
        mock_generar.side_effect = [1, 3, 5, 2, 6]  # AS, TREN, QUINA, TONTO, SEXTO
        
        cacho = Cacho()
        cacho.agitar()
        
        # Verificar que el generador fue llamado 5 veces (una por cada dado)
        assert mock_generar.call_count == 5
        
        # Verificar que los dados tienen los valores esperados
        dados = cacho.get_dados()
        assert dados[0].show() == Pinta.AS
        assert dados[1].show() == Pinta.TREN
        assert dados[2].show() == Pinta.QUINA
        assert dados[3].show() == Pinta.TONTO
        assert dados[4].show() == Pinta.SEXTO
    
    def test_cacho_inicia_con_dados_ocultos(self):
        """Test que verifica que el cacho inicia con los dados ocultos."""
        cacho = Cacho()
        assert not cacho.is_visible()
    
    def test_cacho_mostrar_dados_cambia_visibilidad_a_true(self):
        """Test que verifica que mostrar_dados() hace visibles los dados."""
        cacho = Cacho()
        cacho.mostrar_dados()
        assert cacho.is_visible()
    
    def test_cacho_ocultar_dados_cambia_visibilidad_a_false(self):
        """Test que verifica que ocultar_dados() oculta los dados."""
        cacho = Cacho()
        cacho.mostrar_dados()  # Primero los mostramos
        cacho.ocultar_dados()
        assert not cacho.is_visible()
    
    def test_cacho_get_dados_visibles_retorna_dados_solo_si_es_visible(self):
        """Test que verifica que get_dados_visibles retorna dados solo si están visibles."""
        cacho = Cacho()
        
        # Cuando están ocultos, debería retornar lista vacía
        dados_ocultos = cacho.get_dados_visibles()
        assert dados_ocultos == []
        
        # Cuando están visibles, debería retornar los dados
        cacho.mostrar_dados()
        dados_visibles = cacho.get_dados_visibles()
        assert len(dados_visibles) == 5
        for dado in dados_visibles:
            assert isinstance(dado, Dado)
