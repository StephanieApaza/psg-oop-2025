# Definición
class Mensaje:
    def __init__(self, contenido):
        self.contenido = contenido
    def enviar(self, audio=False, video=False):
        if audio:
            print(f"📣 {self.contenido}")
        if video:
            print(f"📹 {self.contenido}")
        if not audio and not video:
            print(f"💬 {self.contenido}")
            
# Uso
mensaje = Mensaje("Hola, ¿cómo estás?")
mensaje.enviar()
mensaje.enviar(audio=True)
mensaje.enviar(video=True)
mensaje.enviar(audio=True, video=True)