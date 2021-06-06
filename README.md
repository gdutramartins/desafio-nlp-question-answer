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
  Para descobrir o assunto da pergunta utilizei um algoritmo que busca o match com as condições listadas abaixo na sua respectiva ordem:
    a) Encontrar as entidades (NER) da pergunta - Após identificação separar os tokens das entidades encontradas e buscar dentro do array de strings que identificam o assunto.  
    O modelo Spacy utilizado foi *en_core_web_lg*. Entendo que essa parte poderia ter várias melhorias, poderiamos treinar um novo modelo Spacy ou Bert para melhor identificação das entidades.
    
    b) Encontrar Nomes (noun chunks) da pergunta - Após identificação separar os tokens dos nomes encontrados e buscar dentro do array de strings que identificam o assunto.
    O modelo Spacy utilizado foi *en_core_web_lg*
    
    c) Lemmanization - Lemmanization nos tokens do assunto e da pergunta para busca de algum match.
    O modelo Spacy utilizado foi *en_core_web_lg*
    
    d) Stemmer - Stemmer nos tokens do assunto e da pergunta para buscar algum match.
    Utilizado PorterStemmer da NLTK.
    
    e) Encontrar entidades (NER) nos arquivos texto (fonte) relacionados - Cada asssunto está relacionado com um ou mais arquivos texto, são a base de conhecimento para resposta da pergunta. Como última tentativa de fazer o match aplico NER nos arquivos e busco por algum match dos tokens das entidades encontradas na pergunta e nos arquivos.
    
    A reposta da busca por assunto pode retornar mais de uma opção e até encontrar assunto diferente do esperado, por esse motivo fizemos um teste com a base de perguntas. Foram considerados casso de sucesso quando encontra-se uma opção e ela está correta (I), quando a lista retornada tem a opção correta (II) ou ao buscar na lista de opções utiilzando a ordem de prioridade do match é encontrado o assunto. 
    Deve-se consierar também que uma parte da base de perguntas utiliza referências implícitas ao assunto ('him', 'he', 'they', 'them', 'its'), consideramos esses casos como falhas, mas contabilizamos a parte já que se tivesse o nome ou entidade correto seriam identificados corretamente na maioria dos casos.
    Segue abaixo as estatisticas de identificação de assunto (teste com a base de perguntas):
    
    
   
  
  
  
  
  

