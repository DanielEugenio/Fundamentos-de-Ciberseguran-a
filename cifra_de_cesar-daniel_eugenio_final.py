# MUITO IMPORTANTE!!!! há um segredinho no código - só para ser mais divertido, o desafio é primeiro correr o scrip - no online python https://www.online-python.com/
# e só depois de correr o script no python online, então sim ler o codigo (pois quem vai ler o codigo descobre logo onde está o segredo...)


# Daniel Eugénio - 2024 Julho 22

# programinha de script the python para encriptar e desencriptar palavras usando a conhecida cifra de César
# só vai admitir caracteres que sejam letras
# vai ignorar maiusculas e minusculas
# vai pedir ao utilizador que indique o deslocamento da cifra
# permite tambem desencrptar, se o utilizador quiser
# o utilizador pode continuar a sempre a usar o programa queira terminar ou descubra o easter egg
# acho que me entusiasmei um bocado :D

#
#
#
#
#
#
#
#
# Espaço vazio de proprosito para "esconder" o codigo para não ficar logo tudo visivel sem fazer scroll
# A ideia, como afirmado no comentario inicia, é bricar com a consola e só depois rever o código
#
#
#
#
#
#
#
#
#
#

# Função para criptografar 
def cifra_de_cesar(palavra, deslocamento):
    palavra_criptografada = ""
    for char in palavra:
        if char.isalpha():  # Verifica se o caractere é uma letra (se não for uma letra, vai falhar)
            deslocado = ord(char.lower()) + deslocamento  # Converte para minúscula e calcula a posição deslocada
            if deslocado > ord('z'):  # Se o deslocamento passar de 'z'(a ultima letra do alfabeto), volta para o início do alfabeto
                deslocado -= 26  # Subtrai 26 para voltar ao início do alfabeto
            palavra_criptografada += chr(deslocado)  # Adiciona o caractere deslocado à palavra criptografada
        else:
            palavra_criptografada += char  # Se não for uma letra, mantém o caractere original
    return palavra_criptografada

# Função para desencriptar 
def descifra_de_cesar(palavra, deslocamento):
    return cifra_de_cesar(palavra, -deslocamento)  # Reverte o deslocamento para desencriptar

# Função para remover acentos ortográficos manualmente - que podia ser bem mais simples se utilizasse o unicode - mas queria estar a evitar chamar bibliotecas, porque estou a correr online phyton
def remover_acentos(palavra):
    acentos = {
        'á': 'a',
        'ã': 'a',
        'â': 'a',
        'à': 'a',
        'ä': 'a',
        'é': 'e',
        'ê': 'e',
        'è': 'e',
        'ë': 'e',
        'í': 'i',
        'î': 'i',
        'ì': 'i',
        'ï': 'i',
        'ó': 'o',
        'õ': 'o',
        'ô': 'o',
        'ò': 'o',
        'ö': 'o',
        'ú': 'u',
        'û': 'u',
        'ù': 'u',
        'ü': 'u',
        'ç': 'c',
        'ñ': 'n'
    }
    return ''.join(acentos.get(char, char) for char in palavra)

# Função para obter resposta válida do utilizador, para conseguir saber se ele quer continuar ou não, mas só permitir continuar quando a instrução é claramente um sim (ou seja, "Sim","s", "yes" ou "y")
def obter_resposta_valida(prompt, respostas_positivas, respostas_negativas):
    while True:
        resposta = input(prompt).strip().lower()
        if resposta in respostas_positivas + respostas_negativas:
            return resposta
        else:
            print(f"Por favor, responda com uma destas opções: {', '.join(respostas_positivas + respostas_negativas)}")

# Função principal
def programinha():
    while True:
        # Obter palavra que o utilizador escreve
        palavra = input("Por favor, insira a palavra que deseja ser criptografada.\n(Mas atenção! existem algumas palavras mágicas...)").lower() # Passa maiusculas e coloca tudo em minusculas
        palavra_sem_acentos = remover_acentos(palavra)  # Remove acentos ortográficos da palara que o utilizador introduziu
       
       #?
        palavras_magicas = ["benfica", "slb", "1904", "carrega", "maior", "benfas", "aguia", "luz", "glorioso", "benfiquista", "encarnados", "luz", "campeao", "aguias", "mistica", "vitoria", "catedral", "paixao", "inferno"]
        if any(opcao in palavra_sem_acentos for opcao in palavras_magicas):
            print("CARREGA BENFICA!!!!\nParabens! Descobriste o easter egg! Ganheste o jogo! \nO programa terminou.")
            return

        # Verificar se a palavra contém apenas letras
        if not palavra_sem_acentos.isalpha():
            print("Atenção: A palavra contém números ou caracteres especiais. A cifra só funcionará corretamente com letras. Mas não vale a pena entrar em desespero, pode tentar novamente")
            tentar_novamente = obter_resposta_valida("Quer tentar novamente?: ", ["sim", "s", "yes", "y"], ["nao", "n", "no", "nao"])
            if tentar_novamente in ["sim", "s", "yes", "y"]:
                continue  # Reinicia o loop para tentar novamente e continua dentro do programinha
            else:
                print("Obrigado por teres usado este programa incrível!! \nO programa terminou.")
                return  # Fim do programa
        else:
            deslocamento = int(input("Por favor, insira o valor do deslocamento (por exemplo, 3): "))
            # Criptografar a palavra inicialmente criptografada e exibir de volta o resultado
            palavra_criptografada = cifra_de_cesar(palavra_sem_acentos, deslocamento)
            print("Palavra criptografada:", palavra_criptografada)

            # Perguntar ao utilizador se deseja desencriptar a palavra ou não
            resposta = obter_resposta_valida("Deseja desencriptar a palavra? (sim/s/yes/y/nao/n/no/nao): ", ["sim", "s", "yes", "y"], ["nao", "n", "no", "nao"])
            if resposta in ["sim", "s", "yes", "y"]:
                palavra_desencriptografada = descifra_de_cesar(palavra_criptografada, deslocamento)
                print("Palavra desencriptografada:", palavra_desencriptografada)

            # Perguntar ao utilizador se deseja tentar novamente
            tentar_novamente = obter_resposta_valida("Deseja tentar novamente? (sim/s/yes/y/nao/n/no/nao): ", ["sim", "s", "yes", "y"], ["nao", "n", "no", "nao"])
            if tentar_novamente not in ["sim", "s", "yes", "y"]:
                print("Obrigado por teres usado este programa incrível!! \nO programa terminou.")
                return  # Fim

# para manter o programa sempre o funciona até que o utilizador queira terminar ou descubra o easter egg
if __name__ == "__main__":
    programinha()
