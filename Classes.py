class clientes:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
class perfil_cliente:
    def __init__(self, nome, idade, historico_medica, peso, altura, condicao, metas, desempenho):
        self.nome = nome
        self.idade = idade
        self.historico_medica = historico_medica
        self.peso = peso
        self.altura = altura
        self.condicao = condicao
        self.metas = metas
        self.desempenho = desempenho

class treino:
    def __init__(self, exercicio, data, carga, repeticoes, series):
        self.exercicio = exercicio
        self.data = data
        self.carga = carga
        self.repeticoes = repeticoes
        self.series = series