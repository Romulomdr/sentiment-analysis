# Análise de Sentimentos 

O objetivo deste projeto é analisar se os usuários estão gostando ou não de uma determinada postagem, esse projeto foi feito usando python e a rede social escolhida foi o reddit devido sua API ser mais acessível, as bibliotecas que foram usadas serão mostradas e explicadas logo abaixo.

## 🚀 Começando

#### Abaixo segue as bibliotecas usadas juntamente com os links de suas respectivas documentações:

* [Praw](https://praw.readthedocs.io/en/stable/) - Uma biblioteca Python que permite interagir com a API do Reddit de forma fácil e intuitiva.
* [Pandas](https://pandas.pydata.org/docs/user_guide/index.html) - Uma biblioteca de manipulação de dados que fornece estruturas de dados rápidas, flexíveis e expressivas, como DataFrames.
* [NLTK](https://www.nltk.org/) - Biblioteca de toolkit para processamento de linguagem natural (NLP).
* [VaderSentiment](https://vadersentiment.readthedocs.io/en/latest/pages/code_and_example.html) - Um módulo para análise de sentimentos que usa o algoritmo VADER (Valence Aware Dictionary and Sentiment Reasoner).
* [MatPlotLib](https://matplotlib.org/stable/index.html) - Uma biblioteca de plotagem em 2D que fornece uma interface para criar gráficos e visualizações.
* [Seaborn](https://seaborn.pydata.org/) - Uma biblioteca de visualização de dados baseada em matplotlib que fornece uma interface de alto nível para criar gráficos estatísticos atraentes e informativos.

## 📋 Observações

Mesmo com o alto valor de resultados zeros (comentarios com emojis, simbolos, links, entre outros) podemos perceber com base no gráfico se os usuários estão gostando ou não de uma determinada postagem, resultados maiores que 0 estão felizes e menores que 0 não estão felizes
.
Segue abaixo um exemplo:

- [Postagem](https://www.reddit.com/r/cats/comments/1dz9kj4/found_this_baby_car_in_the_road_i_couldnt_leave/#lightbox), o resultado esperado nessa postagem é que além dos comentarios descartados que recebem nota 0,
  seja possivel ver que os cometarios positivos, sejam maiores que os comentarios negativos, abaixo segue uma foto da postagem e logo depois o gráfico após ter feito a análise dos comentários.

![PostagemCat](https://github.com/Romulomdr/sentiment-analysis/assets/106899605/cd913923-bc0d-4548-9a0b-e2dbf5f2240d)

- Resultados:
![Grafico resultado](https://github.com/Romulomdr/sentiment-analysis/assets/106899605/af5b6fff-f912-4f85-9dfd-8d9ecc0f014d)
  
## ✒️ Autor

* [**Romulo Matheus**](https://github.com/Romulomdr) - *Atualmente desenvolvedor Java back-end e suporte a ambientes Moodle* [<img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/romulo-dantasmdr/)

- 😁 Agradeço a todos pela atenção.
