import platform
import psutil
import os
import json
from flask import Flask

app = Flask(__name__)


# Versao so
print(platform.plataform())
# PID
print(os.getpid())
# uso CPU %
print(psutil.cpu_percent)
# uso memoria byte
print(psutil.virtual_memory().used // 1024 ** 2)

metricas = {
    'so': platform.platform(),
    'pid': os.getpid(),
    'cpupercent': psutil.cpu_percent(),
    'usedmembyte': psutil.virtual_me1mory().used // (1024 ** 2)
}

print(json.dumps(metricas, ensure_ascii=False))

@app.route("/")
def index():
    return f"Nome: <h1>Ricardo Lucas Kucek</h1> \
    <br>So: <p>{platform.platform()}</p> \
    <br>PID: <p>{os.getpid()}</p> \
    <br>Porcentagem CPU: <p>{psutil.cpu_percent()}</p> \
    <br>Uso de Memoria(Bytes): <p>{psutil.virtual_me1mory().used // (1024 ** 2)}</p>"


@app.route("/info")
def info():
    return "<h1>Ricardo Lucas Kucek</h1>"


@app.route("/metricas")
def metricas():
    return f"<h1>{metricas}</h1>"
