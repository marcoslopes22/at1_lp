#Aluno(a): Marcos Aurélio Lopes de Araújo, Mauro Cloves
#Professor: Clovis Rocha
#Disciplina: Lógica de Programação
#Data: 14/09/2022

# AT1

#Cadastro de oportunidade de emprego.

import sqlite3

class Oportunidades:
    
    def __init__(self, titulo, salario, dataCriacao, nomeEmpresa, nomeCargo, descricao, status, banco, cursor):
        self.titulo = titulo
        self.salario = salario
        self.dataCriacao = dataCriacao
        self.nomeEmpresa = nomeEmpresa
        self.NomeCargo = nomeCargo
        self.descricao = descricao
        self.status = status
        
        self.__banco = banco
        self.__cursor = cursor
    
    def Connexao(self, banco, cursor):
        self.__banco = sqlite3.connect('banco.db')
        self.__cursor = banco.cursor()
    
    def ListarVagas(self):
        self.__cursor.execute("SELECT * FROM vagas")
    
    def CadastrarVagas(self, titulo, salario, dataCriacao, nomeEmpresa, nomeCargo, descricao, status):
        self.titulo = titulo
        self.salario = salario
        self.dataCriacao = dataCriacao
        self.nomeEmpresa = nomeEmpresa
        self.NomeCargo = nomeCargo
        self.descricao = descricao
        self.status = status
        
        self.__cursor.execute(f"INSERT INTO nome_tabela (titulo, salario, data_criacao, nome_empresa, nome_cargo, descricao, status) VALUES ('{self.titulo}', '{self.salario}', '{self.dataCriacao}', '{self.nomeEmpresa}', '{self.NomeCargo}', '{self.descricao}', '{self.status}')")
    
    def AlterarVagas(self, titulo, id):
        self.titulo = titulo
        self.id = id
        self.__cursor.execute(f"UPDATE vagas SET titulo='{self.titulo}' WHERE id='{self.id}'")
    
    def DeletarVagas(self, id):
        self.id = id
        self.__cursor.execute(f"DELETE FROM vagas WHERE id='{self.id}'")

if __name__=="__main__":
    op = Oportunidades()