import random
from palabras import lista_palabras
from dibujos import etapas

def jugar():
    palabra = random.choice(lista_palabras).upper()
    letras_adivinadas = set()
    letras_usadas = set()
    vidas = 6

    print("\n¡Vamos a jugar al ahorcado!")

    while vidas > 0:
        palabra_mostrar = [letra if letra in letras_adivinadas else "_" for letra in palabra]
        
        print(etapas[6 - vidas])
        print(f"Vidas restantes: {vidas}")
        print("Palabra oculta:", " ".join(palabra_mostrar))

        if "_" not in palabra_mostrar:
            print("\n¡Ganaste! Has adivinado la palabra:", palabra)
            break

        intento = input("\nIngresa una letra: ").upper()

        if len(intento) != 1 or not intento.isalpha():
            print("Debe ingresar solo 1 letra. Intenta de nuevo.")
            continue
            
        if intento in letras_usadas:
            print("Ya ha utilizado la letra. Intenta con otra.")
            continue

        letras_usadas.add(intento)

        if intento in palabra:
            letras_adivinadas.add(intento)
        else:
            vidas -= 1

    if vidas == 0:
        print(etapas[6])
        print("Vidas restantes: 0")
        print("\n¡Has perdido! La palabra era:", palabra)

def main():
    while True:
        jugar()
        repetir = input("\n¿Quieres jugar de nuevo? (S/N): ").upper()
        if repetir != 'S':
            print("Finalizando el programa. ¡Éxitos!")
            break

if __name__ == "__main__":
    main()