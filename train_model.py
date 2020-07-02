from chatterbot import ChatBot

chatbot = ChatBot(
    'MediBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I didnt understand your issue.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

model = ListTrainer(chatbot)

covid_data = open('data/covid_data.txt').read().splitlines()
non_covid_data = open('data/non_covid_data.txt').read().splitlines()

data = covid_data + non_covid_data

model.train(data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

corpus = ChatterBotCorpusTrainer(chatbot)

corpus.train('chatterbot.corpus.english')
corpus.train('chatterbot.corpus.german')

