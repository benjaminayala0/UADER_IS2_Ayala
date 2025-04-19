import os
from dotenv import load_dotenv
import google.generativeai as genai

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Obtener la clave de API desde una variable de entorno
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
ULTIMA_CONSULTA = ""

# Validar que exista la API key
if not GENAI_API_KEY:
    print("❌ ERROR: La clave API no está configurada.")
    exit(1)

print(f"CLAVE API CARGADA: {GENAI_API_KEY}")


def configurar_modelo():
    """Configura y devuelve el modelo generativo."""
    genai.configure(api_key= GENAI_API_KEY)
    modelo = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")
    return modelo


def procesar_consulta(modelo, consulta):
    """Procesa una consulta con el modelo y devuelve la respuesta."""
    try:
        respuesta = modelo.generate_content(consulta)
        return respuesta.text
    except (ValueError, KeyError) as error:
        return f"⚠️ Error al procesar la consulta: {error}"
    except Exception as e:
        return f"⚠️ Error inesperado: {e}"


def iniciar_chat():
    """Inicia el bucle interactivo de chat."""
    global ULTIMA_CONSULTA  # <-- Movido acá arriba
    modelo = configurar_modelo()
    
    while True:
        try:
            consulta = input("Tú: ")

            if not consulta.strip():
                print("⚠️ Ingresá una pregunta o comando.")
                continue

            if consulta.lower() in ("salir", "exit"):
                print("👋 Saliendo del chat.")
                break

            if consulta.lower() == "ultima":
                print(f"📝 Última consulta: {ULTIMA_CONSULTA or 'Ninguna aún.'}")
                continue

            ULTIMA_CONSULTA = consulta  # Ya podés usarla ahora

            respuesta = procesar_consulta(modelo, consulta)
            print("Gemini:", respuesta)

        except KeyboardInterrupt:
            print("\n⛔ Interrumpido por el usuario.")
            break
        except EOFError:
            print("\n📴 Fin de entrada detectado.")
            break

# Punto de entrada del programa
if __name__ == "__main__":
    iniciar_chat()
