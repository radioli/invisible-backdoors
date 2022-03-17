#unicode 
#U+202A
#U+202B 
#U+202D 
#U+202E 
#U+2066 
#U+2067 
#U+2068 
#U+202C 
#U+2069
import re
import sys
list_of_signs=['\u202A', '\u202B', '\u202D', '\u202E', '\u2066', '\u2067', '\u2068', '\u202C', '\u2069']
def search_for_signs(signs:list, input_data:str)->None:
    for sign in list_of_signs:
        for match in re.finditer(sign, input_data):
            unicode_display = sign.encode('raw_unicode_escape')
            print(f'Found {unicode_display}, at index {match.start()}')
    pass
def load_file(file_name:str):
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
        return content
def main():
    args = sys.argv[1:]
    input_data = load_file(str(args[0]))
    search_for_signs(list_of_signs, input_data)

if __name__ == '__main__':
    main()
