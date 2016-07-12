from django.test import TestCase, Client

# Create your tests here.
from Prestamo import Prestamo

#Creando casos de prueba
class CrearPrestamo (TestCase):
    def crear_prestamo(self):
        self.prestamo = Prestamo()

    def test_calcular_prestamo_1(self):
        response = Prestamo.valor_total(self, 2000,2)
        self.assertEqual(response,2080.8)

    def test_calcular_prestamo_1_1(self):
            response = Prestamo.valor_total(self, 2000,5)
            self.assertEqual(response,0)

    def test_calcular_prestamo_2(self):
        response = Prestamo.valor_total(self, 6000,5)
        self.assertEqual(response,6566.25)

    def test_calcular_prestamo_2_2(self):
        response = Prestamo.valor_total(self, 6000,8)
        self.assertEqual(response,0)

    def test_calcular_prestamo_3(self):
        response = Prestamo.valor_total(self, 15000,10)
        self.assertEqual(response,17940)

    def test_calcular_prestamo_3_3(self):
        response = Prestamo.valor_total(self, 15000,16)
        self.assertEqual(response,0)

    def test_calcular_prestamo_4(self):
        response = Prestamo.valor_total(self, 25000,5)
        self.assertEqual(response,0)

    # def test_lista_consultas(self):
    #     '''Metodo que prueba que la url /consultas/
    #     responda con estado 200
    #     '''
    #     respuesta = self.cliente.get('/consultas/')
    #     self.assertEqual(respuesta.status_code,200)
