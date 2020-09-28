import numpy as np

g = 9.81 #kg*m/s^2

class Barra(object):
    def __init__(self, ni, nj, R, t, E, ρ, σy):
        super(Barra, self).__init__()
        self.ni=ni
        self.nj=nj
        self.R=R
        self.t=t
        self.E=E
        self.ρ=ρ
        self.σy=σy
    
    def obtener_connectividad(self):
        """Implementar"""
        return 
    
    def calcular_area(self):
        """Implementar"""
        return 
    
    def calcular_largo(self, reticulado):
        """Implementar"""
        return 
    
    def calcular_peso(self, reticulado):
        """Implementar"""
        return 
        

    