EXIT = 'exit'

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


    for passw in words_list:
        if not passw.__eq__(word):
            #Search coincidences
            passw_comparer = zip(passw, word)
            passw_char = [x for x, z in passw_comparer if x==z]
            
            coincidences = len(passw_char)
            if coincidences == likely:
                passw_posibilities.append({"password":passw, "coincidences":coincidences, "on_letter":passw_char})

    print(passw_posibilities)
    
    """
    filter recibe una funcion anonima y un iterable
    options = list(filter(lambda x : x not in words_list, words_list))
    options = [x for x in words_list if x not in new_list]
    opc = list(map(lambda x : x*2, words_list))
    Ver Reduce
    """


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
            #Antes de agregarla, revisa si la palabra ya wxiste en la lista
            if not data_input in words_list:
                words_list.append(data_input)     
            else:
                print(f'La palabra "{data_input}" ya ha sido agregada')


    #TODO datos de prueba
    words_list=['down', 'upon', 'here', 'stay', 'star', 'block', 'take', 'ride', 'there', ]
    print(words_list)
    #Una vez terminado el ciclo de captura los intentos
    word = get_word('¿Cuál palabra has intentado?')
    if word in words_list:
        likely = get_num('Interta la similitud \t')
        #Descarta todas las opciones que contengan sus letras
        discard_options(words_list, word, likely)
    else:
        print('Esa palabra no está agregada')


if __name__ == "__main__":
   run()
   #https://www.freecodecamp.org/news/if-name-main-python-example/