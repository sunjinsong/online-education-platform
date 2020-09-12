from __future__ import absolute_import, print_function

import sys

__version__ = '0.0.1'

from .main import main
from .where import *
from .which import *

if __name__ == "__main__":
    sys.exit(main())
