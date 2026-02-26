# Primero, se define la función filtrar_vocales, recibe 2 parámetros de
# entrada: cadena y bandera.
# Siempre retorna 2 valores. En caso de éxito: 0 y el string filtrado.
# En caso de error: código de error respectivo y None.
def filtrar_vocales(cadena, bandera):

    # Verificar el tipo de variable con isinstance, compara con un string.
    if not isinstance(cadena, str):
        return -100, None
    # Verifica si cadena es un string vacio.
    if cadena == "":
        return -300, None
    # Bucle for que recorre cada elemento del string y lo compara con las
    # letras del abecedario.
    for c in cadena:
        if c not in "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            return -200, None
    # Verifica una lonigtud de str mayor a 30 con la función len.
    if len(cadena) > 30:
        return -400, None
    # Verificar el tipo de variable con isinstance, compara con un bool.
    if not isinstance(bandera, bool):
        return -500, None
    # Condición de bandera= True.
    # Bucle que recorre cadena y compara con las vocales del abcedario y
    # lo almacena en un str llamado vocales.
    if bandera:
        vocales = ""
        for c in cadena:
            if c in "aeiouAEIOU":
                vocales = vocales + c
        return 0, vocales  # retorna 0 de éxito y el str vocales.
    # Condición de bandera= False.
    # Bucle que recorre cadena y compara con las vocales del abcedario y
    # las que difieren las almacena en un str llamado consonantes.
    else:
        consonantes = ""
        for c in cadena:
            if c not in "aeiouAEIOU":
                consonantes = consonantes + c
        return 0, consonantes  # retorna 0 de éxito y el str consonantes.

# Primero, se define la función encontrar_extremos, recibe 1 parámetro de
# entrada: lista_numeros.
# Siempre retorna 3 valores. En caso de éxito: 0, valor máx y valor min.
# En caso de error: código de error respectivo, None, None.


def encontrar_extremos(lista_numeros):

    # Verificar el tipo de variable con isinstance, compara con una lista.
    if not isinstance(lista_numeros, list):
        return -600, None, None
    # Verifica una lonigtud de lista mayor a 15 con la función len.
    if len(lista_numeros) > 15:
        return -900, None, None
    # Verifica que la lista no esté vacía con la función len.
    if len(lista_numeros) == 0:
        return -800, None, None
    # Bucle que recorre lista_numeros y compara con isinstance si no es float
    # o int, se toma en cuenta que si es bool retorne error ya que python
    # lee True como 1 y False como 0.
    for unidad in lista_numeros:
        if not isinstance(unidad, (int, float)) or isinstance(unidad, bool):
            return -700, None, None
    valor_min_num = min(lista_numeros)  # función min: valor min de la lista
    valor_max_num = max(lista_numeros)  # función max: valor max de la lista
    return 0, valor_min_num, valor_max_num
    # retorna 0 de éxito y el valor max y min.
