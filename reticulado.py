import numpy as np

class Reticulado(object):
    """Define un reticulado"""
    def __init__(self):
        super(Reticulado, self).__init__()
        self.xyz = np.zeros((0,3), dtype=np.double)
        self.Nnodos = 0
        self.barras = []
        self.cargas = {}
        self.restricciones = {}
        
    def agregar_nodo(self, x, y, z=0):
        self.xyz.resize((self.Nnodos+1,3))
        self.xyz[self.Nnodos,:]=[x,y,z]
        self.Nnodos+=1
        return
    
    def agregar_barra(self, barra):
        """Implementar"""
        return
    
    def obtener_coordenada_nodal(self, n): 
        """Implementar"""
        return 
    
    def calcular_peso_total(self):
        """Implementar"""
        return 
    
    def obtener_nodos(self):
        """Implementar"""
        return 
    
    def obtener_barras(self):
        """Implementar"""
        return 
    
    def agregar_restriccion(self, nodo, gdl, valor=0.0):
        """Implementar"""
        return
    
    def agregar_fuerza(self, nodo, gdl, valor):
        """Implementar"""
        return
    
    def ensamblar_sistema(self):
        """Implementar"""
        return
    
    def resolver_sistema(self):
        """Implementar"""
        return
    
    def recuperar_fuerzas(self):
        """Implementar"""
        return
    def __str__(self):
        string = "nodos:\n"
        num_nodos = len(self.xyz)
        for i in range(num_nodos):
            string+=f"{i} : {self.obtener_coordenada_nodal(i)[0],self.obtener_coordenada_nodal(i)[1],self.obtener_coordenada_nodal(i)[2]}\n"
        string += "barras:\n"
        num_barras = len(self.barras)
        for i in range(num_barras):
            n_t1 = str(self.barras[i].ni)
            n_t2 = str(self.barras[i].nj)
            strtt = n_t1 + " " + n_t2
            string+=f'{i} : [{strtt}]\n'
            
        return string
    

