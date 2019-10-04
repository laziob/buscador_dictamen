# library.py

from google.oauth2 import service_account
import pandas_gbq
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
#Auth en BigQuery
credentials = service_account.Credentials.from_service_account_info(
    {
       "type": "service_account",
        "project_id": "dictamenes",
        "private_key_id": "6b1cb9c95b8c9c509928891a70024520a3170408",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCq5DFvpRpW98f/\ngkM8e0g1lLPGf9YKXOUn6KcLdrMwOHjmiFWHvsV2M8O7BDD+dX1h0dCy+9Qfg4bE\nHZBVoAQEHFtdwCPmqRcVbqtflxNKZfHf++MPSfVTte0Fd3doiibAOp/d3NOGiGcM\nq8IdlAyYMde3mojyi92qEBaiGdBMjR4UzCtGDLgDAfqA7rBNQX+lknMPUrvixoog\nQPjyT627fxTFk36YFiyc3PAt1bF1IxvIZ1iFA6WQcp5N0HGn/Hdx+OuSWprGov4t\nxDGz12NGR2HbeYstEFLqC1fpO8uz0rgZ5M4jr4UoK4HMjUAh3ydOCfW8bFvGv3vm\nMUh8j7rPAgMBAAECggEAS7bb0l/fui2BHosr2AW1Ggw+1JE6F5BN9W8mZ7VZMeGr\na1R3NLQIz9SigV8bh/otKaRo54wc0TOYh5ajptRFQz7/GhvxrBY5xISqiCkq4lkl\nn7v9v33gpIyjrbrfHGGtRpkS0J0w2NfhdGM7F5jLNblLnqzoxTHD7b/AD2UJfYiE\nm/prqZxGr1nfY5JjRVdrYpi/6k0zTWqym9AN9NWFZlCqBg3p5nLlOcov1G4eBkAd\npeErzfsAl8HVuQdd1S0j3bl71S/P7QShhdarqoC9ltwy7iLZAMlPIqMStDXJ/ARL\nSdDaGX3W/QNbGdZuVzpFhJNDKcanIGZi3QMzdBkPRQKBgQDiuWGFo2SGndDdRvEr\nh463dhs1GijWZGGQkjGsY/rFowlSPdtvaRwX2pk9H1z7yh9ER6mMps3YtkyGwDba\nCKdYeMfebv2SMcfQaGyZ6bEsZ8z+b2Q4Py8A5zZ7OyRfqTObvBJYMZqhys+2cjyz\nbZ2Qm+3iN7rhdF4zJa378kz74wKBgQDA9TKsniXdcGtNBo6PYqJ17WuXRu5hPI2K\nDXzJ5YbmAeppixwGhcOILINCyCtXR6SjSYr+ftAi+UarStB0QBDwM/+4+XP0lS+w\nW0hRfWXtBpGK1VdGQ13StvNWburAZ15YukVFEYItck/1C1TzrwktuBo34JAOLII4\nY7W/SvnRJQKBgCh+RZ2xrg2g+CHdPsuwfVvk+z0DvBF2gjpo8fhBLxPHZ63JoHyI\ngFz+TOouxNOvqN/wEKcvT4qKHKbgg6tzajgR8liW6DEJNQ/S5rqik2ND8sfqqzKk\njkeSBBgEWx2+wZnqADjCO0T0TR7fzlmZlU+zmcwSeg00VHK8IxPhlcBTAoGAHiby\nuTipUBYeHlY09sECBA2Kr4P9AiLVN0puQppkXxLTj5SWV4qViHT0Of5Pj375gi6e\n0q/8VErBuUiilFfijbaCcmRAs2qQni1Veq5uvAA3xAscbTVftuqx0cLZWiGNA65v\n3qAiyHlBd1hC+SVT+Nn49txXhm98FdW28+KCcSUCgYEA1IL+/oEx69WuEuhbsJNy\n/bXFEj2v2MKmmtzTcUFaxgBDimILSPdKHCJYcksFknt6byVUyDtQKlo96NOnFCzO\n0kbmvbsbNxv5Ch6CODBrBG94B9qdAP2MMucwdx33mfiH2+bson7l9UEBCD6Q8JTA\nLuR2LcR1zT6X754u0wKzkaA=\n-----END PRIVATE KEY-----\n",
        "client_email": "crawleruploader@dictamenes.iam.gserviceaccount.com",
        "client_id": "106844863083512567171",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/crawleruploader%40dictamenes.iam.gserviceaccount.com"
    },
)

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == "POST":
        query = "SELECT titulo, link FROM `dictamenes.dictamenes.test_tabla` WHERE fecha = (SELECT MAX(fecha) FROM dictamenes.dictamenes.test_tabla) AND titulo LIKE '%(texto)s'"
        busqueda = "%" + request.form['busqueda'] + "%"
        dataframe = pandas_gbq.read_gbq(
            query % {'texto':busqueda},
            project_id="dictamenes",
            credentials=credentials,
            dialect='standard'
            )
        print(dataframe)
        return render_template('search.html',  tables=[dataframe.to_html(classes='data', header="true", columns=["titulo", "link"], justify='center')])
    return render_template('search.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
