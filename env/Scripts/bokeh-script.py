#!"c:\users\ezequiel boehler\documents\python scripts\bokeh_ui\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==1.3.4','console_scripts','bokeh'
__requires__ = 'bokeh==1.3.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==1.3.4', 'console_scripts', 'bokeh')()
    )
