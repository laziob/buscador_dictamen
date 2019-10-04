from google.oauth2 import service_account
import pandas_gbq

#Auth en BigQuery
credentials = service_account.Credentials.from_service_account_file('C:/Users/Ezequiel Boehler/Documents/Python scripts/bokeh_ui/dictamenes-sac.json')

query = """
    SELECT titulo, link
    FROM dictamenes.dictamenes.test_tabla
    WHERE fecha in (SELECT MAX(fecha) FROM dictamenes.dictamenes.test_tabla)
        AND titulo LIKE '%(texto)s' 
"""

dataframe = pandas_gbq.read_gbq(
   query % {'texto':'%sum%'},
   project_id="dictamenes",
   credentials=credentials,
   dialect='standard'
)

print(dataframe)