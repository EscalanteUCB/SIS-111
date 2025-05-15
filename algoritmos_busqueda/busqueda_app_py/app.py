from flask import Flask, render_template, request, Response
import random
import time

app = Flask(__name__)
lista_global = []

@app.route('/')
def index():
    return render_template('interactivo.html')

@app.route('/generar', methods=['POST'])
def generar():
    global lista_global
    cantidad = int(request.form['cantidad'])
    lista_global = sorted(random.sample(range(cantidad * 3), cantidad))
    return {'lista': lista_global}

@app.route('/buscar')
def buscar():
    global lista_global
    objetivo = int(request.args.get('valor'))
    tipo = request.args.get('tipo')

    def stream():
        inicio = time.time()

        if tipo == 'lineal':
            for i, val in enumerate(lista_global):
                yield f"data:{i},{val}\n\n"
                time.sleep(0.1)
                if val == objetivo:
                    tiempo = (time.time() - inicio) * 1000
                    yield f"data:found,{i},{tiempo:.2f}\n\n"
                    return
            tiempo = (time.time() - inicio) * 1000
            yield f"data:notfound,,{tiempo:.2f}\n\n"
        else:
            izq, der = 0, len(lista_global) - 1
            while izq <= der:
                medio = (izq + der) // 2
                yield f"data:{medio},{lista_global[medio]}\n\n"
                time.sleep(0.2)
                if lista_global[medio] == objetivo:
                    tiempo = (time.time() - inicio) * 1000
                    yield f"data:found,{medio},{tiempo:.2f}\n\n"
                    return
                elif lista_global[medio] < objetivo:
                    izq = medio + 1
                else:
                    der = medio - 1
            tiempo = (time.time() - inicio) * 1000
            yield f"data:notfound,,{tiempo:.2f}\n\n"

    return Response(stream(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True)
