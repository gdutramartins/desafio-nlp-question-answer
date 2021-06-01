from qs_constants import AppConstants
import pandas as pd
import numpy as np  
import os



# carrega o pandas com os grupos especificados. Os grupos de perguntas e respostas foram declarados como constantes
def load_qa_pairs(qa_source=AppConstants.ALL_QA):
    df_list = []
    for qa_file in qa_source:
        df= pd.read_csv(os.path.join(AppConstants.DATASET_PATH,qa_file),sep='\t')
        df_list.append(df)
    df_concat = pd.concat(df_list)
    return df_concat

# carrega conteúdo dos arquivos com o texto utilizado para responder as perguntas
def get_context_files():
    context_file_map = {}
    for f in os.listdir(CONTEXT_TEXT_PATH):
        file_full_path = os.path.join(CONTEXT_TEXT_PATH, f)
        if os.path.isfile(file_full_path):
            with open(file_full_path, 'r', encoding="utf-8") as f_contexto:
                contexto = f_contexto.read().replace('\n', '')
            chave = f.replace(".txt.clean","")
            context_file_map[chave] = contexto
    return context_file_map
    
#context_files = get_context_files()
#  lista_tamanhos = []
#  for cf in context_files:
#       lista_tamanhos.append(len(context_files[cf].split()))
#   print(lista_tamanhos[:5])


# respostas e perguntas para lowercase
# limpeza da resposta: retirar pontuação do último caracter (., ?, !)
def normalize_qa(vet_qa, lowercase=True):
    vet_n_resp = []
    for qa in vet_qa:
        pergunta, resposta, titulo, ctx_file = qa[AppConstants.COL_PERGUNTA], qa[AppConstants.COL_RESPOSTA], qa[AppConstants.COL_TITULO], qa[AppConstants.COL_CONTEXT_FILE]
        if lowercase:
            pergunta = pergunta.lower()
        if (resposta[-1] in AppConstants.PUNCTUATIONS_TO_REMOVE):
            resposta = resposta[:-1]
        vet_n_resp.append([pergunta, resposta,titulo, ctx_file])
    return np.array(vet_n_resp, dtype=object)


# Remove duplicações de respostas, como as respostas nulas já foram retiradas então escolhe semper a primeira resposta encontrada
def remove_duplication(vet_qa):
    pergunta_set = set()
    vet_qa_clean = []
    
    for pos,qa in enumerate(vet_qa):
        pergunta = qa[0]
        if pergunta in pergunta_set:
            continue
        #perguntas_duplicadas = get_pergunta_igual_from_position(pos+1, vet_qa, pergunta)
        pergunta_set.add(pergunta)
        vet_qa_clean.append(qa)
    return np.array(vet_qa_clean, dtype=object)     


# Remove as perguntas consideradas ruins, exemplo: blah, (What!)
def remove_bad_answer(vet_qa):
    vet_qa_clean = []
    for qa in vet_qa:
        resposta = qa[1]
        if resposta in AppConstants.BAD_ANSWER_TO_REMOVE:
            continue
        vet_qa_clean.append(qa)
    return np.array(vet_qa_clean, dtype=object) 



