EXIT = 'exit'
TRIES = 3

def get_num(msj):
    num = ''
    while type(num) != type(0):
        try:
            num = int(input(msj))
        except TypeError:
            print(TypeError)
            num = ''
    return num

get_word = lambda msj='' : input(msj).lower().strip()

def discard_options(words_list, word, likely=0):
    """
    Recorre la palabra para comparar las letras en sus respectivas posiciones
    """
    passw_posibilities = []
    aux_list = []

    for passw in words_list:
        if not passw.__eq__(word):
            #Search coincidences
            passw_comparer = zip(passw, word)
            passw_char = [x for x, z in passw_comparer if x==z]
            
            coincidences = len(passw_char)
            if coincidences == likely:
                aux_list.append(passw)
                passw_posibilities.append({"password":passw, "coincidences":coincidences, "on_letter":passw_char})

    if len(aux_list) > 0:
        print(f'Estas son las posibles palabras con {likely} coincidencias')
        for item in passw_posibilities:
            print(f'Palabra: {item.get("password").capitalize()} en la letra {item.get("on_letter")}')
    else:
        print('No hay concidencias')
    
    words_list = aux_list
    return words_list


def run():
    print(f'\nEscribe todas las palabras que aparecen en pantalla \n\nEscribe "\\{EXIT.capitalize()}" cuando hayas terminado')
    words_list = []

    get_words_from_user = False
    while get_words_from_user:
        data_input = get_word()
        #Cuando sea el comando de salida, prepara a terminar la ejecución
        if (data_input.__eq__(f'\\{EXIT}')):
            get_words_from_user = False
        else:
            #Antes de agregarla, revisa si la palabra ya existe en la lista
            if not data_input in words_list:
                words_list.append(data_input)     
            else:
                print(f'La palabra "{data_input.capitalize()}" ya ha sido agregada')

    counter = 1
    
    while (len(words_list) > 1) and (counter < TRIES):
        word = get_word('¿Cuál palabra has intentado?')
        if word in words_list:
            likely = get_num('Inserta las similitudes \t')
            #Descarta todas las opciones que contengan sus letras
            words_list = discard_options(words_list, word, likely)
            counter += 1
        else:
            print('Esa palabra no está agregada')


if __name__ == "__main__":
   run()
   #https://www.freecodecamp.org/news/if-name-main-python-example/