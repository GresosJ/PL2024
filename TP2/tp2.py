import re

# Exemplo
markdown_input = """
# Título
Este é um **exemplo** de conversor de *Markdown* para HTML.

## Lista Numerada
1. Item 1
2. Item 2
3. Item 3

## Links e Imagens
Veja mais em [GitHub](https://github.com).
![Logo](https://example.com/logo.png)
"""

def mdHTML(text_md):
    # Cabeçalhos
    text_md = re.sub(r'^(#+)\s+(.*)$', title, text_md, flags=re.MULTILINE)

    # Bold
    text_md = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text_md)

    # Itálico
    text_md = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text_md)

    # Lista numerada
    text_md = numberedList(text_md)

    # Link
    text_md = re.sub(r'\[([^]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text_md)

    # Imagem
    text_md = re.sub(r'!\[([^]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', text_md)

    return text_md

def title(text):
    level = len(text.group(1))
    return f'<h{level}>{text.group(2)}</h{level}>'
    

def numberedList(text):
    numbered_list_exp = re.compile(r'^\d+\.\s(.*)')
    in_numbered_list = False

    processed_lines = []

    for line in text.splitlines():
        subs = numbered_list_exp.subn(r'<li>\1</li>', line)

        if in_numbered_list:
            # Sair do "modo lista numerada"
            if subs[1] == 0:
                in_numbered_list = False
                processed_lines.append('</ol>')
            else:
                line = "    " + subs[0]
        else:
            # Entrar no "modo lista numerada"
            if subs[1] != 0:
                in_numbered_list = True
                processed_lines.append('<ol>')
                line = "    " + subs[0]

        processed_lines.append(line)

    return '\n'.join(processed_lines)

def main():
    print(mdHTML(markdown_input))
    pass
if __name__ == '__main__':
    main()