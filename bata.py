import random
import time
import os

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.vivo = True
        self.cooldowns = {"curar": 0, "defender": 0}

    def recibir_daño(self, daño):
        real = max(1, daño - self.defensa)
        self.vida -= real
        print(f"{self.nombre} recibió {real} de daño.")
        if self.vida <= 0:
            self.vivo = False
            print(f"{self.nombre} ha caído.")

    def curar(self):
        if self.cooldowns["curar"] == 0:
            cantidad = random.randint(15, 25)
            self.vida += cantidad
            print(f"{self.nombre} se curó {cantidad} puntos de vida.")
            self.cooldowns["curar"] = 3
        else:
            print("¡Curar aún está en reutilización!")

    def defender(self):
        if self.cooldowns["defender"] == 0:
            self.defensa += 5
            print(f"{self.nombre} aumentó su defensa por este turno.")
            self.cooldowns["defender"] = 2
        else:
            print("¡Defender aún está en reutilización!")

    def reducir_cooldowns(self):
        for k in self.cooldowns:
            if self.cooldowns[k] > 0:
                self.cooldowns[k] -= 1

def mostrar_estado(jugador, enemigos):
    print(f"\n{jugador.nombre} - Vida: {jugador.vida} - Defensa: {jugador.defensa}")
    for enemigo in enemigos:
        if enemigo.vivo:
            print(f"{enemigo.nombre} - Vida: {enemigo.vida}")

def turno_enemigos(enemigos, jugador):
    for enemigo in enemigos:
        if enemigo.vivo:
            print(f"\n{enemigo.nombre} ataca...")
            jugador.recibir_daño(enemigo.ataque)

# Juego principal
def juego():
    jugador = Personaje("Comandante", 100, 20, 5)
    enemigos = [Personaje(f"Enemigo {i+1}", random.randint(30, 50), random.randint(10, 15), 2) for i in range(3)]

    while jugador.vivo and any(e.vivo for e in enemigos):
        limpiar()
        mostrar_estado(jugador, enemigos)
        print("\nComandos: atacar, defender, curar")
        comando = input("Tu acción: ").lower()

        if comando == "atacar":
            vivos = [e for e in enemigos if e.vivo]
            for i, e in enumerate(vivos):
                print(f"{i+1}. {e.nombre} (Vida: {e.vida})")
            try:
                eleccion = int(input("Elegí enemigo: ")) - 1
                enemigo = vivos[eleccion]
                enemigo.recibir_daño(jugador.ataque)
            except:
                print("Elección inválida.")
        elif comando == "curar":
            jugador.curar()
        elif comando == "defender":
            jugador.defender()
        else:
            print("Comando no válido.")

        turno_enemigos(enemigos, jugador)
        jugador.reducir_cooldowns()
        input("\nPresiona Enter para continuar...")

    if jugador.vivo:
        print("\n¡Has ganado la batalla!")
    else:
        print("\nHas sido derrotado...")

# Iniciar juego
juego()
