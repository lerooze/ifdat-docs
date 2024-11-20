import os
from pathlib import Path
from typing import cast
import shutil
import glob

src_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("prod")
pre_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("pre_prod")
src_dir_lists = src_root.joinpath("structure/codelists")
src_dir_structure = src_root.joinpath("structure")
src_dir_example = pre_root.joinpath("examples")
src_dir_example_reports = pre_root.joinpath("reports")
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
dst_dir_lists = static_root.joinpath("codelists")
shutil.copytree(src_dir_lists, dst_dir_lists)
structure_path = static_root.joinpath("structure")
os.makedirs(structure_path)
for f in glob.glob(str(src_dir_structure.joinpath("IFDAT*"))):
    pf = Path(f)
    shutil.copyfile(pf, structure_path.joinpath(pf.name))
example_path = static_root.joinpath("examples")
shutil.copytree(src_dir_example, example_path)
shutil.copytree(src_dir_example_reports, example_path.joinpath("reports"))
report = src_root.joinpath("reports").joinpath("IFDAT-LIST.xlsx")
shutil.copy(report, structure_path)

codelists = dst_root.joinpath("source/types/codelists")
try:
    shutil.rmtree(codelists)
except FileNotFoundError:
    pass
codelists.mkdir(parents=True)
for f in os.listdir(dst_dir_lists):
    fp = Path(f)
    if "_" not in fp.stem:
        continue
    name = fp.stem[:-5]
    sourcepath = codelists.joinpath(f"{name.lower()}.rst")
    with open(sourcepath, mode="w") as io:
        cnt = len(name)
        quote = "="
        io.write(f"{name}{os.linesep}{quote*cnt}{os.linesep}{os.linesep}")
        io.write(".. csv-table::\n")
        io.write(f"   :file: /_static/codelists/{name.upper()}_ENUM.csv{os.linesep}")
        io.write("   :header-rows: 1")
