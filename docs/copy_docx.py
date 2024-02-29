from pathlib import Path
import os
import shutil

root = Path(os.path.abspath(__file__)).parent
src = root.joinpath("_build/docx/IFDat-Docs.docx")
dst = root.joinpath("source/_static/IFDat-Docs.docx")
shutil.copyfile(src, dst)
