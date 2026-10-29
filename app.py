#!/usr/bin/env python3.12
# txt —— 一堆行粘进去，去重/排序/转格式，全在浏览器里算
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("page.html")


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("TXT_PORT", "8880")), debug=False)
