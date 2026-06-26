import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_colaboradores():
    try:
        with open('COLABORADORES.md', 'r') as f:
            content = f.read()
        # Usamos <pre> para mantener el formato de texto original (saltos de línea, etc.)
        return f"<pre>{content}</pre>"
    except FileNotFoundError:
        return "Error: No se encontró el archivo COLABORADORES.md"

if __name__ == "__main__":
    # Cloud Run requiere escuchar en 0.0.0.0 y usa la variable de entorno PORT (por defecto 8080)
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)