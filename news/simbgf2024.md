---
title: "The lab at the 2024 Symposium of Brazilian Geophysical Society"
date: 2024-10-17
author: Leonardo Uieda
---

{%- import "macros.html" as macros %}

Last week, me and lab member [Ellen Fernandes Marcos](../team/#fernandesellen)
attended the [10<sup>th</sup> Symposium of the Brazilian
Geophysical Society](https://sbgf.org.br/xsimposio/), held at the beautiful
Salvador in the state of Bahia, northeastern Brazil.

{{ macros.figure("../images/news/simbgf2024-venue.jpg", caption="View from the balcony of the conference venue. Couldn't ask for a better place to sit during the coffee breaks!", alt="View of a small beach with white sand, some palm trees on the left and a big hotel building on the right" ) }}

## Poster presentation

Ellen gave her first ever conference presentation about her work on
cross-validation applied to equivalent source methods for interpolating gravity
and magnetic data.
Her poster was well attended during the session and she handled the questions
perfectly, even when facing one of the top experts in equivalent sources in the
world. You can find abstract (in Portuguese) below.

{{ macros.figure("../images/news/simbgf2024-ellen.jpg", caption="Ellen and her poster during the first day of the event. The title of the presentation was (in Portuguese): Quantificação da qualidade da interpolação de dados de métodos potenciais por fontes equivalentes utilizando validação cruzada em blocos.", alt="A woman with curly hair smiling next to a poster with a bright box in the center showing the main question of the study and figures around it as supporting information" ) }}

### Abstract (in Portuguese)

Como parte do seu processamento, dados de gravimetria e magnetometria são
rotineiramente interpolados em malhas regulares a altitudes constantes.
O método das fontes equivalentes é ideal para realizar esse processamento por
levar em consideração a física do problema, como a altitude variável dos pontos
de observação e o fato dos dados representarem funções harmônicas. A qualidade
do resultado obtido varia de acordo com dois parâmetros: a profundidade das
fontes e o parâmetro de regularização. Ambos controlam o grau de suavidade da
solução e a capacidade do método de prever valores plausíveis onde existem
lacunas nos dados observados. Neste trabalho, utilizamos o método da validação
cruzada em blocos (Roberts et al. 2017; doi:10.1111/ecog.02881) para estimar
a capacidade das fontes equivalentes de prever dados onde existem lacunas nos
levantamentos. Na validação cruzada, os dados são divididos aleatoriamente em
dois subconjuntos, um para ajuste (treinamento) do modelo de fontes
equivalentes e outro para testar as previsões do modelo. Para dados de métodos
potenciais, a divisão aleatória dos dados resulta em um conjunto de dados para
teste que estão espacialmente próximos dos dados para treinamento. Isso provoca
a superestimação da qualidade do ajuste aos dados de teste, pois dados de
métodos potenciais são autocorrelacionados, ou seja, dados espacialmente
próximos tendem a ter valores semelhantes. A separação dos dados por blocos ao
invés de aleatoriamente foi introduzida para sanar esse problema. Porém, sua
viabilidade para a técnica de fontes equivalentes não foi explorada. Utilizamos
dados sintéticos e reais para avaliar o uso das metodologias "block k-fold"
e "leave-one-block-out" para estimar a qualidade da interpolação de dados
gravimétricos e magnetométricos por fontes equivalentes. Nossa avaliação inclui
um teste sistemático do efeito da variação do tamanho dos blocos na estimativa
da qualidade, tanto para levantamentos terrestres quanto aerolevatamentos. Para
conjuntos de dados grandes (> 10,000), testamos também a aplicação da validação
cruzada em uma parcela dos dados e a viabilidade da extrapolação dos resultados
para o resto do levantamento. Por fim, os resultados nos informam como
a utilização destes métodos impactam na produção de malhas que combinam
diversos levantamentos para grandes territórios, como Brasil, Antártica
e Austrália. As fontes equivalentes serão as de Soler & Uieda (2021;
doi:10.31223/X58G7C) e a validação cruzada por blocos será a implementação do
pacote Verde (Uieda, 2018; doi:10.21105/joss.00957).

## Sessions and social

The Symposium was great way to catch up with what the Brazilian geophysics
community has been up to in the past few years while I've been away.
It was great to walk around the poster hall and see all of the interesting
research being done by students from the several geophysics programmes from
across the country.
It was also great that I got to see old friends from grad school!

{{ macros.figure("../images/news/simbgf2024-friends.jpg", caption='Old friends from undergrad in São Paulo and grad school in Rio de Janeiro. From left to right: <a href="https://www.researchgate.net/profile/Flora-Solon">Flora F. Solon</a> (Professor at UFF), <a href="https://www.pinga-lab.org/people/oliveira-jr.html">Vanderlei C. Oliveira Jr.</a> (Researcher at Observatório Nacional), me, and <a href="https://www.linkedin.com/in/higo-oliveira-nunes-26897a46/?originalSubdomain=br">Higo O. Nunes</a> (Geophysicist at the Brazilian Geological Survey).', alt="A woman and three men smiling with people at a poster session in the background" ) }}

My favorite session by far was the discussion on the geophysics undergraduate
programmes, the challenges we face, and future perspectives.
I was particularly good because a good number of students were present and some
commented on their experience, needs, and difficulties.
Geophysics is struggling worldwide as enrollment dwindles
(see [this report from the UK](https://doi.org/10.1093/astrogeo/atae056) for
a quantitative example) and Brazil is not an exception.
But I'm optimistic that our public university systems will be able to sustain
our programmes into the future, particularly since they aren't as susceptible
to market forces like for-profit institutions abroad.
We have a long road ahead of us to get the word out about geophysics to
prospective students and to show that it's not all about oil and gas and
mining.

To me, **the most important thing we can do is hire good people at
universities** who are not only worried about how much grant money they can get
or how many papers they've published.
We need people who want to engage in outreach, who value education and strive
to improve, and who contribute to the diversity of our departments, including
a diversity of research themes outside of natural resource exploration.


