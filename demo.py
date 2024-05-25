from campana import Campana
from anuncio import Video, Display, Social
import datetime

def crear_anuncio():
    print("Crear un nuevo anuncio:")
    alto = obtener_valor_positivo("Altura: ")
    ancho = obtener_valor_positivo("Ancho: ")
    tipo = input("Tipo (Video/Display/Social): ").lower()

    if tipo == "video":
        duracion = obtener_valor_positivo("Duración del video: ")
        sub_tipo = obtener_sub_tipo(Video.SUB_TIPOS, "Subtipo (instream/outstream): ")
        return Video(alto, ancho, duracion, sub_tipo)
    elif tipo == "display":
        sub_tipo = obtener_sub_tipo(Display.SUB_TIPOS, "Subtipo (tradicional/native): ")
        return Display(alto, ancho, sub_tipo)
    elif tipo == "social":
        sub_tipo = obtener_sub_tipo(Social.SUB_TIPOS, "Subtipo (facebook/linkedin): ")
        return Social(alto, ancho, sub_tipo)
    else:
        print("Tipo de anuncio no válido.")
        return None

def obtener_valor_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 1:
                raise ValueError("El valor debe ser mayor que 0")
            return valor
        except ValueError as e:
            print("Error:", e)

def obtener_sub_tipo(sub_tipos, mensaje):
    while True:
        sub_tipo = input(mensaje).lower()
        if sub_tipo in sub_tipos:
            return sub_tipo
        else:
            print("Subtipo no válido.")

def mostrar_anuncios(anuncios):
    print("\n==============================")
    print("\nListado de anuncios:")
    for i, anuncio in enumerate(anuncios):
        print(f"{i + 1}. {anuncio}")
        print("==============================")

def comprimir_anuncio(anuncios):
    if anuncios:
        indice = seleccionar_anuncio(anuncios, "Seleccione el índice del anuncio a comprimir: ")
        if indice is not None:
            anuncios[indice].c_anuncio()
    else:
        print("No hay anuncios creados aún.")

def redimensionar_anuncio(anuncios):
    if anuncios:
        indice = seleccionar_anuncio(anuncios, "Seleccione el índice del anuncio a redimensionar: ")
        if indice is not None:
            anuncios[indice].r_anuncio()
    else:
        print("No hay anuncios creados aún.")

def seleccionar_anuncio(anuncios, mensaje):
    while True:
        try:
            indice = int(input(mensaje)) - 1
            if 0 <= indice < len(anuncios):
                return indice
            else:
                print("Índice de anuncio no válido.")
        except ValueError as e:
            print("Error:", e)

def main():
    nombre_campana = input("Ingrese el nombre de la campaña: ")
    fecha_inicio = obtener_fecha("Fecha de inicio de la campaña (DD-MM-YYYY): ")
    fecha_termino = obtener_fecha("Fecha de término de la campaña (DD-MM-YYYY): ")
    anuncios = []

    while True:
        print("\n1. Crear nuevo anuncio")
        print("2. Mostrar anuncios")
        print("3. Comprimir anuncio")
        print("4. Redimensionar anuncio")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            anuncio = crear_anuncio()
            if anuncio:
                anuncios.append(anuncio)
                print("==============================")
                print("Anuncio creado exitosamente.")
                print("==============================")
        elif opcion == "2":
            mostrar_anuncios(anuncios)
        elif opcion == "3":
            comprimir_anuncio(anuncios)
        elif opcion == "4":
            redimensionar_anuncio(anuncios)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

    if anuncios:
        try:
            campaña = Campana(nombre_campana, anuncios, fecha_inicio, fecha_termino)
            print("\nRESUMEN DE LA CAMPAÑA:")
            print("=" * 22)
            print(campaña)
        except ValueError as e:
            print("Error:", e)
            with open("error.log", "a") as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp} - Error al crear la campaña: {str(e)}\n")

def obtener_fecha(mensaje):
    while True:
        try:
            fecha = input(mensaje)
            datetime.datetime.strptime(fecha, "%d-%m-%Y")
            return fecha
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()