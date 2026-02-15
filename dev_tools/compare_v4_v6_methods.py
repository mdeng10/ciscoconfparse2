"""Compare methods on IPv4Obj() and IPv6Obj().  Flag missing methods"""

from ciscoconfparse import IPv4Obj, IPv6Obj
from loguru import logger

import sys
import os

sys.path.insert(0, "../")  # add the path to the local git repo copy
# from this dev_tools/ directory
environ = os.environ["VIRTUAL_ENV"]
print("ENV", environ)


try:
    print("PYTHONPATH", str(os.environ["PYTHONPATH"]))
except Exception as eee:
    error = f"{eee}: Could not find PYTHONPATH."
    logger.error(error)
    raise OSError(error)

v4_list = dir(IPv4Obj("127.0.0.1"))
v6_list = dir(IPv6Obj("::1"))

for ii_v4 in v4_list:
    if ii_v4 not in v6_list:
        print("IPv6Obj() is missing method:", ii_v4)

for ii_v6 in v6_list:
    if ii_v6 not in v4_list:
        print("IPv4Obj() is missing method:", ii_v6)
