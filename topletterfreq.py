#Exercicio 3, lista 2

from collections import Counter
import os

def limpar_terminal():
    '''Função para limpar o terminal de acordo com o S.O'''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
  
              
def interface():
    '''Função de interface'''
    limpar_terminal()
    print('F͓̽r͓̽e͓̽q͓̽u͓̽ê͓̽n͓̽c͓̽i͓̽a͓̽ ͓̽a͓̽l͓̽f͓̽a͓̽b͓̽é͓̽t͓̽i͓̽c͓̽a͓̽\n\nTecle enter para começar')
    escolha = input('')
       
    if escolha == '':
        programa()
    else:
        interface()
          
    
def programa():
    '''Função da funcionalidade do programa'''
    limpar_terminal()
    print('Insira seu texto')
    texto = input('')
    texto = texto[:1000]
    contagem = Counter(letra.lower() for letra in texto if letra.isalpha())
    total_letras = sum(contagem.values())
    porcentagem = {letra: (quantidade / total_letras) * 100 for letra, quantidade in contagem.items()}
    letras_ordenadas = sorted(contagem.items(), key=lambda item: (-item[1], item[0]))
    mais_frequentes = letras_ordenadas[:2]
    
    for letra, quantidade in mais_frequentes:
        print(f"{letra}: {porcentagem[letra]:.2f}%")
        
    print('\ndeseja escrever novamente?\n[1]escrever outra palavra')
    continuar = input('')
    if continuar == '1':
        programa()
        
                
def main():
    limpar_terminal()
    interface()
if __name__ == '__main__':
    main()
