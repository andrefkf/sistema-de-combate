import random
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

jugador = {
    "nombre": "Héroe",
    "vida": 100,
    "ataque": 20,
    "defensa": 10
}

def generar_enemigo():
    nombres = ["Goblin", "Orco", "Esqueleto", "Slime", "Bandido"]
    return {
        "nombre": random.choice(nombres),
        "vida": random.randint(50, 100),
        "ataque": random.randint(10, 25),
        "defensa": random.randint(5, 15)
    }

def atacar(atacante, defensor):
    prob = random.random()
    if prob < 0.1:
        print(f"{atacante['nombre']} falló el ataque.")
        return
    elif prob > 0.9:
        daño = (atacante["ataque"] * 2) - defensor["defensa"]
        print(f"¡{atacante['nombre']} hizo un CRÍTICO!")
    else:
        daño = atacante["ataque"] - defensor["defensa"]

    daño = max(1, daño)  
    defensor["vida"] -= daño
    print(f"{atacante['nombre']} hizo {daño} de daño a {defensor['nombre']}.")

def combate():
    enemigo = generar_enemigo()
    limpiar()
    print(f"¡Un {enemigo['nombre']} salvaje apareció!\n")

    while jugador["vida"] > 0 and enemigo["vida"] > 0:
        print(f"{jugador['nombre']} - Vida: {jugador['vida']}")
        print(f"{enemigo['nombre']} - Vida: {enemigo['vida']}\n")

        input("Presiona Enter para atacar...")
        atacar(jugador, enemigo)

        if enemigo["vida"] <= 0:
            print(f"\n¡Has vencido al {enemigo['nombre']}!\n")
            break

        print("\nTurno del enemigo...")
        atacar(enemigo, jugador)

        if jugador["vida"] <= 0:
            print(f"\n💀 El {enemigo['nombre']} te ha derrotado...\n")
            break

while True:
    jugador["vida"] = 100  
    combate()
    again = input("¿Combatir de nuevo? (s/n): ").lower()
    if again != "s":
        print("¡Gracias por jugar!")
        break
