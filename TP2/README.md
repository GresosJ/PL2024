# TPC 2 - Converter Markdown para HTML
## Autor
 - A88000;
 - Gerson Henrique de Araújo Júnior;

## Enunciado


Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:
 - Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
   - In: 
     ```markdown
      #Exemplo
     ```
   - Out:
     ```html 
     <h1>Exemplo</h1>
     ```
 - Bold: pedaços de texto entre "**":
   - In:
     ```markdown 
     Este é um **exemplo** ...
     ```
   - Out: 
     ```html
     Este é um <b>exemplo</b> ...
     ```
 - Itálico: pedaços de texto entre "*":
   - In: 
     ```markdown
     Este é um *exemplo* ...
     ```
   - Out: 
     ```html
     Este é um <i>exemplo</i> ...
     ```
 - Lista numerada:
   - In:
     ```markdown
     1. Primeiro item
     2. Segundo item
     3. Terceiro item
     ```
   - Out:
     ```html
     <ol>
        <li>Primeiro item</li>
        <li>Segundo item</li>
        <li>Terceiro item</li>
     </ol>
     ```
 - Link: [texto](endereço URL)
   - In: 
     ```markdown
     Como pode ser consultado em [página da UC](http://www.uc.pt)
     ```
   - Out: 
     ```html
     Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
     ```
 - Imagem: ![texto alternativo](path para a imagem)
   - In: 
     ```markdown
     Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
     ```
   - Out: 
     ```html
     Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
     ```

### Resolução
Então para criar este conversor, foram utilizadas expressões regulares (Regex) para leitura e substituição dos elementos textuais.

Foi implementada uma função adicional chamada "title" que realiza a numeração dos cabeçalhos, verificando e contando o número de "#" após a palavra-chave. Na conversão de todos os elementos, exceto a Lista Numerada, foram empregadas expressões regulares, conforme mencionado anteriormente.

Mas no cas da Lista Numerada, foi utilizadaa uma abordagem diferente, onde a função "numbered_list" verifica se a linha começa com um número seguido de um ponto, e se sim, adiciona a tag "< li>" ao início da linha e a tag "</ li>" ao final da linha. No final, a função "numbered_list" adiciona as tags "< ol>" e "</ ol>" ao início e ao final da lista, respetivamente.