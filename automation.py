import os
import time
import random
from datetime import datetime

# 1. Função para SALVAR dados (Peso e Água)
def registrar_peso():
    print("\n--- PROJETO BULKING (Rumo aos 57kg) ---")
    try:
        peso = float(input("Qual o seu peso hoje? (ex: 48.5): "))
        data_atual = datetime.now().strftime("%d/%m/%Y")
        
        with open("historico_peso.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{data_atual} - Peso: {peso}kg\n")
            
        print(f"✔️ Peso salvo! Faltam {57.0 - peso:.1f}kg para a meta.")
        
        agua = peso * 35
        print(f"💧 Meta de água para hoje: {agua/1000:.1f} Litros.")
        
    except ValueError:
        print("[!] Digite apenas números usando ponto (ex: 48.5)")
    time.sleep(4)

# 2. Função para LER dados (Histórico)
def ver_historico():
    print("\n--- ÚLTIMOS REGISTROS DE PESO ---")
    try:
        with open("historico_peso.txt", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:
                print("Nenhum peso registrado ainda.")
            else:
                for linha in linhas[-5:]:
                    print(linha.strip())
    except FileNotFoundError:
        print("Arquivo de histórico ainda não existe. Registre um peso primeiro!")
    time.sleep(4)

# 3. Função do Treino
def verificar_treino():
    print("\n--- DIVISÃO DE TREINO (4 Dias) ---")
    print("1. Peito e Tríceps")
    print("2. Costas e Bíceps")
    print("3. Pernas (Quadríceps e Panturrilha)")
    print("4. Ombros e Posterior de Coxa")
    print("5. Descanso")
    
    dia = input("\nQual é o treino de hoje? (1-5): ")
    if dia in ['1', '2', '3', '4']:
        print("💪 Foco na progressão de carga! Não pula o treino.")
    elif dia == '5':
        print("💤 Descanso merecido.")
    time.sleep(2)

# 4. Função de Lazer
def momento_lazer():
    print("\n--- ROLETA DO DESCANSO ---")
    opcoes = [
        "Avançar a campanha no Ghost of Tsushima 🗡️",
        "Jogar umas partidas de Mortal Kombat 11 🐉",
        "Construir no Minecraft ⛏️",
        "Ler mangá / Assistir Bleach ⚔️"
    ]
    escolha = random.choice(opcoes)
    print(f"Sua missão de lazer agora é: {escolha}")
    time.sleep(4)

# 5. NOVA Função: Cuidados com o Eren 🐈
def cuidar_do_eren():
    print("\n--- 🐈 CUIDADOS COM O EREN ---")
    print("1. Dar ração seca")
    print("2. Dar aquele sachê caprichado")
    print("3. Trocar a água (gato ama água fresca!)")
    print("4. Limpar a caixa de areia")
    print("5. Brincar / Dar carinho")
    print("6. Voltar ao menu principal")
    
    acao = input("\nO que o Eren tá precisando agora? (1-6): ")
    
    if acao == '1':
        print("\n🥣 Ração na tigela! O Eren tá crocando feliz.")
    elif acao == '2':
        print("\n🥫 Barulho de sachê abrindo... Ele veio correndo na velocidade da luz!")
    elif acao == '3':
        print("\n💧 Água trocada e fresquinha. Hidratação em dia.")
    elif acao == '4':
        print("\n🧹 Caixa de areia limpa. Trabalho sujo, mas necessário.")
    elif acao == '5':
        print("\n🧶 Hora da diversão e ronronados!")
    elif acao == '6':
        print("\nVoltando...")
    else:
        print("\n[!] Opção inválida.")
    time.sleep(3)

# 6. Menu Principal
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("="*45)
        print(" 💻 TERMINAL PESSOAL | SISTEMAS DE INFORMAÇÃO ")
        print("="*45)
        print("1. Registrar peso diário")
        print("2. Ver histórico de progresso")
        print("3. Verificar treino do dia")
        print("4. Roleta de Lazer")
        print("5. Cuidar do Eren 🐈")
        print("6. Sair")
        
        escolha = input("\nO que vamos rodar agora? (1-6): ")
        
        if escolha == '1':
            registrar_peso()
        elif escolha == '2':
            ver_historico()
        elif escolha == '3':
            verificar_treino()
        elif escolha == '4':
            momento_lazer()
        elif escolha == '5':
            # Agora a opção 5 chama o sub-menu inteiro que criamos!
            cuidar_do_eren()
        elif escolha == '6':
            print("\nEncerrando o terminal. Falou!")
            break
        else:
            print("\n[!] Comando inválido.")
            time.sleep(1)

if __name__ == "__main__":
    menu()