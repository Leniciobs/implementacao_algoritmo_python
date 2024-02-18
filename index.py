def validar_senha(senha):
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
    
    sem_pontuacao = senha.isalnum()
    tamanho_valido = 6 <= len(senha) <= 32
    
    return tem_maiuscula and tem_minuscula and tem_numero and sem_pontuacao and tamanho_valido

while True:
    try:
        print("")
        print("Digite a senha: ")
        senha = input().strip()
        if validar_senha(senha):
            print("Senha valida.")
        else:
            print("Senha invalida.")
    except EOFError:
        break
    
