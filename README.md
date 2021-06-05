**Pós Graduação PUC/RJ - BI-Master - Maio de 2021**

**Grupo de Desafios NLP - Tema: Question Similarity**

Terceiro Desafio do Grupo de Desafios NLP. Promovido pelos professores Leonardo Mendoza e Cristian Muñoz Villalobos. O objetivo do desafio será construir um modelo para resolver o problema de question similarity publicado no Kaggle no link abaixo: https://www.kaggle.com/rtatman/questionanswer-dataset

O resultado esperado é fazer com que o modelo responda a perguntas por similaridade, ou seja, dada uma base de perguntas e respostas conhecidas (base de conhecimento), uma nova pergunta solicitada (existente ou não) será respondida com a resposta relacionada à pergunta da base com maior similaridade. 




**Links Utilizados**

- [NLP for Question Answering](https://qa.fastforwardlabs.com/)

- [Fine-tuning with custom datasets — transformers 4.5.0.dev0 documentation](https://huggingface.co/transformers/custom_datasets.html#question-answering-with-squad-2-0)

- [Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/pdf/1908.10084.pdf)

- [Exemplo Sentence Bert](https://colab.research.google.com/github/joeddav/blog/blob/master/_notebooks/2020-05-29-ZSL.ipynb#scrollTo=SM-4kizTBy9j)

- [Exemplo Sentence Bert](https://colab.research.google.com/github/joeddav/blog/blob/master/_notebooks/2020-05-29-ZSL.ipynb#scrollTo=SM-4kizTBy9j)

- [Sentence Transformer Sources](https://github.com/UKPLab/sentence-transformers)

- [SentenceTransformers Documentation](https://www.sbert.net/index.html)

- [Sentence Similarity With BERT | Towards Data Science](https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1)

  
  ---
  
  **Solução Construida com apoio dos Mentores**
  
  Temos dois problemas no mesmo desafio:
    1) Descobrir o assunto da pergunta - A similiaridade deve ser realizada com as perguntas que estão no mesmo asssunto (*ArticleTitle*). 
    2) Encontrar a pergunta com maior similaridade - Dentre as perguntas que existem naquele contexto qual aquela que possui maior similaridade com a pergunta informada.
  
  **Parte 1 - Descobrind o asssunto da pergunta**
  Para descobrir o assunto da pergunta utilizei um algorimo que tenta fazer o match com as seguintes condições seguindo a ordem de aplicação:
    a) Encontrar as entidades (NER) da pergunta - Separo os tokens das entidades encontradas e busco dentro do array de tokens  
    Utilizei spacy com o modelo lg. Esse é um ponto de muitas melhorias, poderiamos crir um modelo para melhor identificação de entidades, mais relacionadas com os assuntos do desafio. É uma melhoria interessante que deve gerar bons resultados na primeira parte do problema. 
    
    
   
  
  
  
  
  

