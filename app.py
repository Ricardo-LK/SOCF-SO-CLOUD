import platform
import psutil
import os
import json
from flask import Flask

app = Flask(__name__)


# Versao so
print(platform.platform())
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
    'usedmembyte': psutil.virtual_memory().used // (1024 ** 2)
}

print(json.dumps(metricas, ensure_ascii=False))

@app.route("/")
def index():
    return f"<h1>Nome: Ricardo Lucas Kucek</h1> \
    <br><p>So: {platform.platform()}</p> \
    <br><p>PID: {os.getpid()}</p> \
    <br><p>Porcentagem CPU: {psutil.cpu_percent()}</p> \
    <br><p>Uso de Memoria(Bytes): {psutil.virtual_memory().used // (1024 ** 2)}</p>"


@app.route("/info")
def info():
    return "<h1>Ricardo Lucas Kucek</h1>"


@app.route("/metricas")
def metrics():
    return metricas
