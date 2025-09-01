from db import db

class Notebooks(db.Model):
    __tablename__ = 'Notebook'

    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(80), nullable=False)
    Categoria = db.Column(db.String(80), nullable=False)
    preço = db.Column(db.Integer, nullable=False)

    def json(self):
        return {
            'id': self.id,
            'Nome': self.Nome,
            'Categoria': self.Categoria,
            'preço': self.preço
        }
        