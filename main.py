import collections

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

def discard_options(words_list, word):
    """
    Encuentra las palabras que contienen la letra para quitarlas de las opciones
    """
    new_list = []

    for letter in word: 
        for word_on_list in words_list:
            #Al encontrar una palabra con esa similitud, la elimina
            if letter in word_on_list:
                if word_on_list not in new_list:
                    new_list.append(word_on_list)

    #High order funcions
    #filter recibe una funcion anonima y un iterable
    options = list(filter(lambda x : x not in new_list, words_list))
    #options = [x for x in words_list if x not in new_list]
    print(options)
    #Ver Reduce
    opc = list(map(lambda x : x*2, words_list))
    print(opc)

def find_options(words_list, word, likely):
    """
    Encuentra las palabras que contienen la letra añadirlas
    """
    new_list = []

    for letter in word: 
        for word_on_list in words_list:
            #Al encontrar una palabra con esa similitud, la elimina
            if letter in word_on_list:
                if word_on_list not in new_list:
                    new_list.append(word_on_list)
    
    options = list(filter(lambda x : x in new_list, words_list))
    print(options)


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
    #words_list=['down', 'upon', 'else', 'love']
    #print(words_list)
    #Una vez terminado el ciclo de captura los intentos
    word = get_word('¿Cuál palabra has intentado?')
    if word in words_list:
        likely = get_num('Interta la similitud')
        if likely > 0:
            find_options(words_list, word, likely)
        else:
            #Descarta todas las opciones que contengan sus letras
            discard_options(words_list, word)
    else:
        print('Esa palabra no está agregada')


if __name__ == "__main__":
   run()
   #https://www.freecodecamp.org/news/if-name-main-python-example/