from sqlalchemy import create_engine

# importa tipos de dados e estruturas de colunos
from sqlalchemy import Column, Integer, String, Float,  Boolean

# importa a classe base usada para criar os modelos ORMS
from sqlalchemy.orm import declarative_base

#importa a ferramena para criar sessões no banco
from sqlalchemy.orm import sessionmaker

# Criar classe base do orm
Base = declarative_base()

# Classe = Tabelas
# Objeto = Linha da tabela
# Atributo = Coluna

# Classe Produto que representa uma tabela no banco
class Produto(Base):
    #Nome da tabela
    __tablename__ = "produtos"

    # Coluna id - número inteiro (Integer)
    id = Column(Integer, primary_key=True)

    #Nome do produto - (String)
    nome = Column(String(100))

    # Preço do produto - (Float)
    preco = Column(Float)

    estoque = Column(Integer)

    ativo = Column(Boolean)

    # Método construtor
    def __init__(self, nome, preco, estoque, ativo):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo

    #Representação do objeto ao imprimir
    def __repr__(self):
        return f"Produto (id={self.id}, nome={self.nome}, preco={self.preco})"
    

#Criar a conexão com banco sqlite
engine = create_engine("sqlite:///estoque.db", echo=True)


# Criar a tecela no banco de dados
Base.metadata.create_all(engine)

#criar uma fabrica de sessões com banco
Session = sessionmaker(bind=engine)

#criar a sessão unica = carrinho
session = Session()

#criar um objeto
produto1 = Produto("Notebook", 5000, 10, True)

session.add(produto1)
session.commit()


 
 
    


