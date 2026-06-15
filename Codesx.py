class Taxi:
    def __init__(self):
        self.lugares = 4
    
    def __add__(self, other) -> int:
        if isinstance(other, int) :
            self.lugares -= other
            return self.lugares - other
        elif isinstance(other, Taxi):
            self.lugares -= other.lugares
            return self.lugares - other.lugares
    
    def Vf_LugarVago(self, other):
        if isinstance(other, Taxi):
            if self.lugares >= other.lugares:
                return True
            else: return False
        elif isinstance(other, int):
            if self.lugares >= other:
                return True

quant_grupos = int(input())
grups = input().split()
sortedGroups = sorted(grups, reverse=True)
Taxis = [Taxi()]
indexTaxis = 0

for grupo_ in sortedGroups:
    grupo = int(grupo_)
    if grupo != 1: 
        if Taxis[indexTaxis].Vf_LugarVago(grupo):
            Taxis[indexTaxis] + grupo
        else:
            Taxis.append(Taxi())
            indexTaxis += 1
            if Taxis[indexTaxis].Vf_LugarVago(grupo):
                Taxis[indexTaxis] + grupo 
    elif grupo == 1:
        deu = False
        for taxi in Taxis:
            if taxi.Vf_LugarVago(grupo):
                taxi + grupo
                deu = True
                break
        if not deu:
            Taxis.append(Taxi())
            indexTaxis += 1
            if Taxis[indexTaxis].Vf_LugarVago(grupo):
                Taxis[indexTaxis] + grupo 
                
print(len(Taxis))