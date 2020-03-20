import requests
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def import_files(name):
    with open(name, 'rt') as f:
        text = f.read()
    
    return text
    
def lang_det(name):
    if name == 'FR.txt':
        to_lang = 'fr'
    elif name == 'ES.txt':
        to_lang = 'es'
    elif name == 'DE.txt':
        to_lang = 'de'
    else:
        print('Некорректный ввод')
        
    return to_lang

def translate_it(text, to_lang):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-ru'.format(to_lang)
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    data = ''.join(json_['text'])
    translate_1 = open('translate_'+ to_lang + '.txt', 'w', encoding= 'utf-8')

def main():
    command = input('Какой документ нужно перевести? e - ES.txt, f - FR.txt, d - DE.txt : ')
    if command == e:
        print('Выполняется обработка файла...')
        name = 'ES.txt'
        import_files(name)
        lang_det(name)
        translate_it(text, to_lang)
        print('Готово!')
    elif command == f:
        print('Выполняется обработка файла...')
        name = 'FR.txt'
        import_files(name)
        lang_det(name)
        translate_it(text, to_lang)
        print('Готово!')
    elif command == d:
        print('Выполняется обработка файла...')
        name = 'DE.txt'
        import_files(name)
        lang_det(name)
        translate_it(text, to_lang)
        print('Готово!')
    else:
        print('Некорректный ввод. Попробуйте еще раз')

main()
