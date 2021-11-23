import os
import json
import shutil
from datetime import datetime
from docx import Document
from docxtpl import DocxTemplate
from pathlib import Path
from icecream import ic

def cleanup():
    MYDIR = 'out'

    try:
        CHECK_FOLDER = os.path.isdir(MYDIR)

        if CHECK_FOLDER:
            shutil.rmtree(MYDIR)
            ic("removed folder : ", MYDIR)
        else:
            ic(MYDIR, "folder doesn't exists.")

        Path(MYDIR).mkdir(parents=True, exist_ok=True)
    except OSError as e:
        ic("Error: %s : %s" % (MYDIR, e.strerror))


cleanup()

ic.enable()
