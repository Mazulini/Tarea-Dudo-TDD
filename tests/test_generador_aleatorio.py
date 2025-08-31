"""
Tests para la clase GeneradorAleatorio del juego Dudo Chileno.
"""

from src.servicios.generador_aleatorio import GeneradorAleatorio


class TestGeneradorAleatorio:
    """Tests para la clase GeneradorAleatorio."""

    def test_generar_retorna_numero_en_rango_default(self):
        """Test que verifica que generar retorna un número entre 1 y 6."""
        numero = GeneradorAleatorio.generar()
        assert 1 <= numero <= 6

    def test_generar_retorna_numero_en_rango_personalizado(self):
        """Test que verifica que generar retorna un número en el rango
        especificado."""
        numero = GeneradorAleatorio.generar(min_val=10, max_val=20)
        assert 10 <= numero <= 20

    def test_generar_con_rango_unitario(self):
        """Test que verifica que generar funciona con un rango de un solo
        valor."""
        numero = GeneradorAleatorio.generar(min_val=5, max_val=5)
        assert numero == 5

    def test_generar_multiples_valores_estan_en_rango(self):
        """Test que verifica que múltiples generaciones están en el rango
        correcto."""
        for _ in range(100):
            numero = GeneradorAleatorio.generar()
            assert 1 <= numero <= 6
            assert isinstance(numero, int)