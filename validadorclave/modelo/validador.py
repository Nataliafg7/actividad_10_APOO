from errores import *

class ReglaValidacion:
    def __init__(self, longitud_esperada): 
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        return len(clave) > self._longitud_esperada 


class ReglaValidacionGanimedes(ReglaValidacion):
    def _contiene_mayuscula(self, clave):
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave):
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave):
        return any(c.isdigit() for c in clave)

    def contiene_caracter_especial(self, clave):
        caracteres_especiales = ['@', '_', '#', '$', '%']
        return any(c in clave for c in caracteres_especiales)

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self._contiene_mayuscula(clave):
            raise NoTieneLetraMayusculaError()
        if not self._contiene_minuscula(clave):
            raise NoTieneLetraMinusculaError()
        if not self._contiene_numero(clave):
            raise NoTieneNumeroError()
        if not self.contiene_caracter_especial(clave):
            raise NoTieneCaracterEspecialError()
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        return 'calisto' in clave.lower()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        if not self.contiene_calisto(clave):
            raise NoTienePalabraSecretaError()
        return True


class Validador:
    def __init__(self, regla):
        self.regla = regla

    def es_valida(self, clave): # El método es_valida de la clase Validador debe retornar el resultado de invocar el método es_valida en el objeto regla que tiene como atributo.
        return self.regla.es_valida(clave)
    

#Los métodos _contiene_mayuscula, _contiene_minuscula y _contiene_numero de la clase ReglaValidacion
#implementan correspondientemente la lógica que verifica si una clave tiene una letra mayúscula, tiene 
#una letra minúscula y tiene un número. Para implementar dichos métodos puedes utilizar los métodos de la 
#clase str isupper(), islower() e isdigit()#


# Ej
def main():
    clave_ganimedes = "N@talia7*"
    clave_calisto = "CalistO7"

    validador_ganimedes = Validador(ReglaValidacionGanimedes(8))
    validador_calisto = Validador(ReglaValidacionCalisto(6))

    try:
        print("Validando clave con regla de Validación Ganímedes:")
        print(validador_ganimedes.es_valida(clave_ganimedes))
    except ValidadorError as e:
        print(f"Error: {e}")

    try:
        print("Validando clave con regla de Validación Calisto:")
        print(validador_calisto.es_valida(clave_calisto))
    except ValidadorError as e:
        print(f"Error: {e}")
main()