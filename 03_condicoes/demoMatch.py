from unittest import case

# match / case


mes = -1

match mes:
    case 1:
        print("janeiro")
    case 2:
        print("fevereiro")
    case 3:
        print("marco")
    case 4:
        print("abril")
    case 5:
        print("maio")
    case 6:
        print("junho")
    case 7:
        print("julho")
    case 8:
        print("agosto")
    case 9:
        print("setembro")
    case 10:
        print("outubro")
    case 11:
        print("novembro")
    case 12:
        print("dezembro")
    case _: # _ -> representa tudo, apanha todos os valores que ainda não foram apanhados
        print("invalido")


# criar uma match case para os dias da semana 