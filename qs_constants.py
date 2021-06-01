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
    
    TOKENS_COM_FALTA_CONTEXTO = ['he','his','him', 'they', 'them']