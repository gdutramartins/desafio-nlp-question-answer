# Grupo de Perguntas, Respostas e metadados para busca de contexto
class TitleGroup:    
    def __init__(self):        
        # Perguntas, respostas e embedding da pergunta
        self.question_list = []
        # entidades encontradas para o assunto após processamento dos arquivos de contexto
        self.context_ner = set() 
        # lista de arquivos com texto para extração do contexto
        self.files= set()
        
# Pergunta, Resposta e Embedding obtido pelo processamento do transformer
class QuestionEmbedding:    
    def __init__(self):
        self.question = ""
        self.answer = ""
        self.embedding =[]