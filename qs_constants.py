import os

class AppConstants():

    DATASET_PATH = "dataset"
    CONTEXT_TEXT_PATH = os.path.join(DATASET_PATH,"text_data")
    CONTEXT_FILE_EXTENSION = ".txt.clean"

    S08_QA = ["S08_question_answer_pairs.txt"]
    S09_QA = ["S09_question_answer_pairs.txt"]
    S10_QA = ["S10_question_answer_pairs.txt"]
    ALL_QA = S08_QA + S09_QA + S10_QA

    PUNCTUATIONS_TO_REMOVE = [".", "!", "?"]
    BAD_ANSWER_TO_REMOVE = ["blah","blah blah blah","(What?)"]

    MODEL_BASE_NLI_MEAN = 'sentence-transformers/bert-base-nli-mean-tokens'
    
    # Colunas para manipulação dos dados extraidos do Pandas
    COL_PERGUNTA = 0
    COL_RESPOSTA = 1
    COL_TITULO = 2
    COL_CONTEXT_FILE = 3
    
    # indica perguntas que não seria possível encontrar contexto porque usam referencias que seriam substituidas em perguntas
    TOKENS_COM_FALTA_CONTEXTO = ['he','his','him', 'they', 'them']
    
    # metodos utilizados para busca de assunto
    # NER na pergunta e confronta com o assunto ou parte do nome do assunto
    METODO_BUSCA_ASSUNTO_NER_PERGUNTA = "NER_PERGUNTA"  
    # após o postag, utiliza o conjunto de "nouns" para fazer um match com o assunto
    METODO_BUSCA_ASSUNTO_NOUN_PERGUNTA = "POSTAG_NOUN"   
    # separa a pergunta e assunto em tokens, tentando fazer o match pela lemetização
    METODO_BUSCA_ASSUNTO_LEMMA = "LEMMATIZATION" 
    # carrega os arquivos de contexto de cada assunto e extrai as entidades, tentando fazer um match com as entidades da pergunta
    METODO_BUSCA_ASSUNTO_NER_CONTEXTO = "NER_CONTEXTO" 