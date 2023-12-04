import os 
import csv
import base64
class Produto:
    def __init__(self,nome,preco,descricao,tamanho,img):
        self.nome = nome 
        self.preco = preco 
        self.descricao = descricao
        self.img = img
        self.tamanho = tamanho
    
    def criar_csv(self):
        if not os.path.exists("produtos.csv"):
            cabecalho = ["nome","preço","decricao","tamanho","imagem"]
            
            with open("produtos.csv","w",newline="", encoding="utf-8") as arquivo:
                escrever = csv.DictWriter(arquivo,fieldnames=cabecalho)
                escrever.writeheader()
       
    def criar_csv_img(self):
        if not os.path.exists("produtos_imagens.csv"):
            cabecalho = ["nome","imagem"]
            
            with open("produtos_imagens.csv","w",newline="", encoding="utf-8") as arquivo:
                escrever = csv.DictWriter(arquivo, fieldnames=cabecalho)
                escrever.writeheader()
                             
    def adicionar_no_csv(self,produto):
        self.criar_csv()
        cabecalho = ["nome", "preço", "descricao", "tamanho", "imagem"]
        with open("produtos.csv", 'a', newline='', encoding='utf-8') as arquivo_novo:
            escreve = csv.DictWriter(arquivo_novo, fieldnames=cabecalho)

            # Convertendo a imagem para Base64
            with open(produto.img, "rb") as imagem_arquivo:
                imagem_base64 = base64.b64encode(imagem_arquivo.read()).decode("utf-8")

            escreve.writerow({
                "nome": produto.nome,
                "preço": produto.preco,
                "descricao": produto.descricao,
                "tamanho": produto.tamanho
            })
    def adicionar_no_csv_imagens(self, produto):
        self.criar_csv_imagens()
        cabecalho = ["nome", "imagem"]
        with open("produtos_imagens.csv", 'a', newline='', encoding='utf-8') as arquivo_novo:
            escreve = csv.DictWriter(arquivo_novo, fieldnames=cabecalho)

            # Converte a imagem para Base64
            with open(produto.img, "rb") as imagem_arquivo:
                imagem_base64 = base64.b64encode(imagem_arquivo.read()).decode("utf-8")

            escreve.writerow({
                "nome": produto.nome,
                "imagem": imagem_base64
            })    
             
            
    
    def cadastrar_produto(nome, preco, descricao, tamanho, img):
        novo_produto = Produto(nome, preco, descricao, tamanho, img)
        novo_produto.adicionar_no_csv_dados(novo_produto)
        novo_produto.adicionar_no_csv_imagens(novo_produto)
        print(f"Produto {nome} foi cadastrado com sucesso!")
def main():
    
    print("------ MENU MODA FITNESS ------")
    print("[1] Cadastrar produto ")
    escolha = input("Insira sua escolha: ")
    match escolha:
        case '1':
            nome = input("Insira o nome do produto: ")
            preco = input("Insira o preço do produto: ")
            descricao = input("Insira a descrição do produto: ")
            tamanho = input("Insira o tamanho da roupa [PP,P,M,G,GG,XG]: ")
            img = input("Insira o caminho da imagem do produto: ")
            
            
            if os.path.exists(img):
                cadastrar_produto(nome, preco, descricao, tamanho, img)
            else:
                print("Arquivo de imagem não encontrado.") 
     
# Chamar a função principal
if __name__ == "__main__":
    main()