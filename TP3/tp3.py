import re

def process_text(text):
    soma = 0
    on = True

    for match in re.findall(r'(on|off|=|\d+)', text, flags=re.IGNORECASE):
        if match.isdigit():
            if on:
                soma += int(match)
        elif match.lower() == 'on':
            on = True
        elif match.lower() == 'off':
            on = False
        elif match == '=':
            print(f'Soma = {soma}')

def main():
    texto_exemplo = "oN 100 10120 oFF = on 192912 aijsjia 99u812ijxaiphsu8 = off askoasoi on 1020192 jasjaj09s off = asiajs ahshaisl askoaosk on 1020192 jasjaj09s off = asiajs ahshaislon = a0129090pxoai a90x890as09dczoxi =  off"
    process_text(texto_exemplo)

if __name__ == "__main__":
    main()
