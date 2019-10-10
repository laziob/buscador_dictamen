# library.py

from google.oauth2 import service_account
import pandas_gbq
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
#Auth en BigQuery


#Funcion para formatear links como hyperlinks
def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)

@app.route('/', methods=['GET', 'POST'])
def buscar():
    if request.method == "POST":
        query = "SELECT titulo, link FROM `dictamenes.dictamenes.test_tabla` WHERE fecha = (SELECT MAX(fecha) FROM dictamenes.dictamenes.test_tabla) AND titulo LIKE '%(texto)s'"
        busqueda = "%" + request.form['busqueda'] + "%"
        dataframe = pandas_gbq.read_gbq(
            query % {'texto':busqueda},
            project_id="dictamenes",
            dialect='standard'
            )
        print(dataframe)
        return render_template('index.html',  tables=[dataframe.to_html(classes='data', header='true', columns=['titulo', 'link'], justify='center', render_links='true')])
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')