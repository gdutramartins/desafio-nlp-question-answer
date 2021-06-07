# Pós Graduação PUC/RJ - BI-Master - Maio de 2021

## Grupo de Desafios NLP - Tema: Question Similarity

Terceiro Desafio do Grupo de Desafios NLP. Promovido pelos professores Leonardo Mendoza e Cristian Muñoz Villalobos. O objetivo do desafio será construir um modelo para resolver o problema de question similarity publicado no Kaggle no link abaixo: https://www.kaggle.com/rtatman/questionanswer-dataset

O resultado esperado é fazer com que o modelo responda a perguntas por similaridade, ou seja, dada uma base de perguntas e respostas conhecidas (base de conhecimento), uma nova pergunta solicitada (existente ou não) será respondida com a resposta relacionada à pergunta da base com maior similaridade. 

&nbsp;   
---
## Solução Construida com apoio dos Mentores

  Temos dois problemas no mesmo desafio:  
  1. Descobrir o assunto da pergunta - A similiaridade deve ser realizada com as perguntas que estão no mesmo asssunto (*ArticleTitle*).  
  2. Encontrar a pergunta com maior similaridade - Dentre as perguntas que existem naquele contexto qual aquela que possui maior similaridade com a pergunta informada.   


### Parte 1 - Identificando o asssunto da pergunta  
  Para descobrir o assunto da pergunta utilizei um algoritmo que busca o match com as condições listadas abaixo na sua respectiva ordem:  
    &nbsp;&nbsp;a) Encontrar as entidades (NER) da pergunta - Após identificação separar os tokens das entidades encontradas e buscar dentro do array de strings que identificam o assunto.  
    O modelo Spacy utilizado foi *en_core_web_lg*. Entendo que essa parte poderia ter várias melhorias, poderiamos treinar um novo modelo Spacy ou Bert para melhor identificação das entidades.  
    &nbsp;  
    &nbsp;&nbsp;b) Encontrar Nomes (noun chunks) da pergunta - Após identificação separar os tokens dos nomes encontrados e buscar dentro do array de strings que identificam o assunto.
    O modelo Spacy utilizado foi *en_core_web_lg*.      
    &nbsp;  
    &nbsp;&nbsp;c) Lemmanization - Lemmanization nos tokens do assunto e da pergunta para busca de algum match.
    O modelo Spacy utilizado foi *en_core_web_lg*.      
    &nbsp;  
    &nbsp;&nbsp;d) Stemmer - Stemmer nos tokens do assunto e da pergunta para buscar algum match.
    Utilizado PorterStemmer da NLTK.      
    &nbsp;  
    &nbsp;&nbsp;e) Encontrar entidades (NER) nos arquivos texto (fonte) relacionados - Cada asssunto está relacionado com um ou mais arquivos texto, são a base de conhecimento para resposta da pergunta. Como última tentativa de fazer o match aplico NER nos arquivos e busco por algum match dos tokens das entidades encontradas na pergunta e nos arquivos.  
    &nbsp;  
    A reposta da busca por assunto pode retornar mais de uma opção e até encontrar assunto diferente do esperado, por esse motivo fizemos um teste com a base de perguntas. Foram considerados casso de sucesso quando encontra-se uma opção e ela está correta , quando a lista retornada contém a opção correta ou ao buscar a principal escolha na lista de opções priorizando a ordem do match é encontrado somente um assunto. 
    Deve-se considerar também que uma parte da base de perguntas utiliza referências implícitas ao assunto ('him', 'he', 'they', 'them', 'its'), consideramos esses casos como falhas, mas contabilizamos a parte já que se tivesse o nome ou entidade correto seriam identificados corretamente na maioria dos casos.
    Segue abaixo as estatisticas de identificação de assunto (teste com a base de perguntas):
    &nbsp;  
   > Total de Perguntas: 2.202  
    Total Encontradas: 1.950  
    Não Encontrados: 69  
    Identificação Incorreta: 183  
    Qtd. Perguntas com referencia implícita(he, him, ...): 178   
    &nbsp;      

Em nossa análise o resultado de identificação do assunto foi bastante satisfatório e com a melhoria do modelo NER poderia ser maior ainda.  

  &nbsp;  
  ### Parte 2 - Busca por pergunta com maior similaridade 

  A busca da pergunta com maior similiridade utiliza modelos pré-treinados para tratamento por sentença, conhecidos como SBERT ou Sentence Transformers eles são afinados para esse objetivo. 
  Em nossa abordagem capturamos o embedding da sentença, aplicamos mean polling descartando a parte da sentença vazia, ou seja, que não contém tokens, já que foi preenchida com vazio para normalização da sentenças (padding). A similaridade final é calculada por coseno dos embeddings das sentenças.

  Para teste da solução construída montei um vetor de perguntas para que o programa identificasse o assunto e mostrasse as 3 maiores similaridades.


**Pergunta: Was Abraham Lincoln the president of the United States?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> Was Abraham Lincoln the first President of the United States?  -  tensor(0.9469)  
When did Lincoln first serve as President?  -  tensor(0.8925)  
Was James Monroe President of the United States?  -  tensor(0.8230)  

&nbsp;  

**Pergunta: Why ducks don't fly?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> What unrelated water birds are ducks sometimes confused with?  -  tensor(0.7844)  
What makes it more difficult for a diving duck to fly?  -  tensor(0.7573)  
What types of unrelated water birds with similar forms are ducks sometimes confused with?  -  tensor(0.7022)  

&nbsp;  

**Pergunta: Can use ducks for economics use?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> What economic uses to ducks have?  -  tensor(0.9044)  
What is an economic use of a duck?  -  tensor(0.8524)  
What are some economic uses for duck?  -  tensor(0.8505)  

&nbsp;  

**Pergunta: Is ducks confused with other animals?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> What unrelated water birds are ducks sometimes confused with?  -  tensor(0.8770)  
What types of unrelated water birds with similar forms are ducks sometimes confused with?  -  tensor(0.8718)  
Are ducks an accepted presence in some populated areas?  -  tensor(0.7921)  

&nbsp;  

**Pergunta: How many years elephants live?**
*3  respostas encontradas com similaridade maior que  0.7*
> How long may elephants live?  -  tensor(0.8987)
How long is the elephant's gestation period?  -  tensor(0.8276)
How much do elephants weight at birth?  -  tensor(0.8011)  

&nbsp;  

**Pergunta: How long for elephant's get a baby?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> How long is the elephant's gestation period?  -  tensor(0.8803)  
How long may elephants live?  -  tensor(0.8076)  
How much do elephants weight at birth?  -  tensor(0.7604)  

&nbsp;  

**Pergunta: Did Finland have an international crisis with another country?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> What is a country with which Finland is involved in an international conflict?  -  tensor(0.9306)  
For how long has the classification of dialects spoken outside of Finland been a controversial issue?  -  tensor(0.7782)  
Where is Finland located?  -  tensor(0.7253)  

&nbsp;  

**Pergunta: Can I use ants for cooking?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> Are ants used in cuisine?  -  tensor(0.8906)  
Do the ants eat plants, meats, or both?  -  tensor(0.7894)  
Are ants found in Antartica?  -  tensor(0.7665)  

&nbsp;  

**Pergunta: Does ants fly?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> Do worker ants have wings?  -  tensor(0.9120)  
Are ants found in Antartica?  -  tensor(0.8151)  
Do male ants take flight before females?  -  tensor(0.7904)  

&nbsp;  

**Pergunta: Can i hear the butterflies?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> Do butterflies make sounds?  -  tensor(0.9017)  
Do butterflies have two eyes?  -  tensor(0.7895)  
What butterfly is migratory?  -  tensor(0.7298)  

&nbsp;  

**Pergunta: Was Anders Celsius born in Sweden?**  
*3  respostas encontradas com similaridade maior que  0.7*  
> Was celsius born in Uppsala  in Sweden?  -  tensor(0.9430)  
Was Celsius born in Uppsala in Sweden ?  -  tensor(0.9430)  
Was Celsius born in Uppsala in Sweden?  -  tensor(0.9430)  

&nbsp;  

**Pergunta: What you can tell me about cello?**
*3  respostas encontradas com similaridade maior que  0.7*  
> What is cello an abbreviation of?  -  tensor(0.8422)  
What is a person who plays the cello called?  -  tensor(0.8355)  
What position is used to play the cello?  -  tensor(0.8307)   

&nbsp;  



### Links Utilizados

- [NLP for Question Answering](https://qa.fastforwardlabs.com/)

- [Fine-tuning with custom datasets — transformers 4.5.0.dev0 documentation](https://huggingface.co/transformers/custom_datasets.html#question-answering-with-squad-2-0)

- [Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/pdf/1908.10084.pdf)

- [Exemplo Sentence Bert](https://colab.research.google.com/github/joeddav/blog/blob/master/_notebooks/2020-05-29-ZSL.ipynb#scrollTo=SM-4kizTBy9j)

- [Exemplo Sentence Bert](https://colab.research.google.com/github/joeddav/blog/blob/master/_notebooks/2020-05-29-ZSL.ipynb#scrollTo=SM-4kizTBy9j)

- [Sentence Transformer Sources](https://github.com/UKPLab/sentence-transformers)

- [SentenceTransformers Documentation](https://www.sbert.net/index.html)

- [Sentence Similarity With BERT | Towards Data Science](https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1)

