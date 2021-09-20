from flask import Flask, render_template, request, jsonify
import os
import sys
import pickle
import nltk
from models.termo_busca import TermoBusca
from flask_sqlalchemy import SQLAlchemy
# from database.database import *
from email_send.send_mail import *

# ##---------- Carrega parâmetros ----------## #
from models.twitter_client import TwitterClient

try:
    with open('Parametros/freqs.json', 'rb') as fp:
        freqs = pickle.load(fp)
except FileNotFoundError:
    print('Está faltando o modelo freqs.json')
    sys.exit(-1)

try:
    with open('Parametros/theta.json', 'rb') as fp:
        theta = pickle.load(fp)
except FileNotFoundError:
    print('Está faltando o modelo theta.json')
    sys.exit(-1)

nltk.download('stopwords')

# ##---------- Começa a aplicação em Si----------## #
twitter_client = TwitterClient()
termo_busca = TermoBusca(twitter_client, freqs, theta)

app = Flask(__name__)

# ##---------- DataBase ----------## #

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:31290731@localhost/nlp'

else:
    app.debug = False
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://fkkauxkbvkesee:bca4e1d872621d95c2db6e554af36c2b50c144a4a57f83dcb7198fa518a06386@ec2-107-21-10-179.compute-1.amazonaws.com:5432/d1aetrj539aa60'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__ = 'termo'
    id = db.Column(db.Integer, primary_key=True)
    termo = db.Column(db.String(200))

    def __init__(self, termo):
        self.termo = termo


# ##---------- Fim da criação do db ----------## #

@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")


@app.route('/termo', methods=["GET"])
def term():
    # Pega o Termo pesquisado
    termo = request.args.get("termo")

    # banco de dados
    data = Feedback(termo)
    db.session.add(data)
    numero_pesquisas = db.session.query(db.func.count(Feedback.id)).scalar()  # conta número de pesquisas no site
    termos_pesquisados_count = dict(db.session.query(Feedback.termo, db.func.count(Feedback.termo)).group_by(
        Feedback.termo).all())  # pesquisa a ocorrencia de cada termo
    db.session.commit()

    # Pegando as listas processadas
    positive, negative = termo_busca.make_list_positives_and_negatives_regression(termo)

    # Debug

    # print(f'O numero positivos de tweets foi: {len(positive)}')
    # print(f'O numero negativos de tweets foi: {len(negative)}')
    # print(f'Lista de tweets positiva foi: {positive}')
    # print(f'O numero de pesquisas foram: {numero_pesquisas}')
    # print(f'O resultado foi esse {termos_pesquisados_count}')
    # print(f' Esse é o tipo de termos_pesquisados_count {type(termos_pesquisados_count)}')

    return jsonify({
        'positiva': positive,
        'negativa': negative,
        'tracking_searchs': numero_pesquisas,
        'tracking_number_each_search': termos_pesquisados_count
    })


@app.route('/formulario', methods=["GET"])
def form():
    """
    Função que envia o email
    """
    nome = request.args.get("name")
    email = request.args.get("email")
    text = request.args.get("message")
    send_mail(nome, email, text)
    return nome


if __name__ == '__main__':
    # Produção
     port = int(os.environ.get('PORT', 5000))
     app.run(host='0.0.0.0', port=port)

    # Dev
    #app.run()
