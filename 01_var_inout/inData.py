print("Bem-Vindo")


nome = input("Digite seu nome: ") # devolve SEMPRE str
idade = input("Digite sua idade: ")

idade_int = int(idade) # converte idade para int -> idade tem de representar um int
                       # float(idade)  converte idade para float


print(f"Ola {nome}!")
print(f"tens {idade} anos")

anoNasc = 2026 - idade_int

print(f"nasceste em {anoNasc} ")