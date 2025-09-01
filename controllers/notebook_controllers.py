from models.notebook_models import Notebooks
from db import db
import json
from flask import make_response

def create_notebook(notebook_data):
    novo_notebook = Notebooks(
        Nome=notebook_data['Nome'],
        Categoria=notebook_data['Categoria'],
        preço=notebook_data['preço']
    )
    db.session.add(novo_notebook)
    db.session.commit()
    response = make_response(
        json.dumps({
            'mensagem': 'notebook cadastrado com sucesso.',
            'Notebook': novo_notebook.json()
        }, sort_keys=False)
    )
    response.headers['content-Type'] = 'application/json'
    return response