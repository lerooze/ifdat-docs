import os
from pathlib import Path
from typing import cast
import shutil

src_root = Path(cast(str, os.environ.get("JOURNEY_DATA"))).joinpath("test")
src_dir_structure = src_root.joinpath("structure")
dst_root = Path(os.path.abspath(__file__)).parent
static_root = dst_root.joinpath("source/_static")
try:
    shutil.rmtree(static_root)
except FileNotFoundError:
    os.makedirs(static_root)
dst_structure = static_root.joinpath("structure")
shutil.copytree(src_dir_structure, dst_structure)
paths = ["acq", "ack", "examples", "reports"]
for p in paths:
    src_path = src_root.joinpath(p)
    dst_path = static_root.joinpath(p)
    shutil.copytree(src_path, dst_path)

ifdat_list_src = (
    Path(cast(str, os.environ.get("JOURNEY_DATA")))
    .joinpath("prod")
    .joinpath("reports")
    .joinpath("IFDAT-LIST.xlsx")
)
ifdat_list_dst = (
    static_root.joinpath("reports").joinpath("prod").joinpath("IFDAT-LIST.xlsx")
)
ifdat_list_dst.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(ifdat_list_src, ifdat_list_dst)

codelists = dst_root.joinpath("source/types/codelists")
try:
    shutil.rmtree(codelists)
except FileNotFoundError:
    pass
codelists.mkdir(parents=True)
dst_dir_lists = static_root.joinpath("structure/codelists")
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
