import os
from pathlib import Path
from typing import cast
import shutil
import glob

src_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("pre_prod")
src_dir_lists = src_root.joinpath("structure/codelists")
src_dir_structure = src_root.joinpath("structure")
src_dir_example = src_root.joinpath("examples")
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
os.makedirs(example_path)
for f in glob.glob(str(src_dir_example.joinpath("ifdat*"))):
    pf = Path(f)
    shutil.copyfile(pf, example_path.joinpath(pf.name))
report = src_root.joinpath("reports").joinpath("IFDAT_SNAPSHOT_PUBLIC_REPORT.xlsx")
shutil.copyfile(report, structure_path.joinpath("IFDAT-RAS.xlsx"))

for f in os.listdir(dst_dir_lists):
    fp = Path(f)
    name = fp.stem
    sourcepath = dst_root.joinpath(f"source/types/codelists/{name}.rst")
    with open(sourcepath, mode="w") as io:
        cnt = len(name)
        quote = "="
        io.write(f"{name}{os.linesep}{quote*cnt}{os.linesep}{os.linesep}")
        io.write(".. csv-table::\n")
        io.write(f"   :file: /_static/codelists/{name.upper()}.csv{os.linesep}")
        io.write("   :header-rows: 1")
