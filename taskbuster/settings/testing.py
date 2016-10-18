# -*- coding: utf-8 -*-
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

FIXTURE_DIRS = (
    os.path.join(BASE_DIR, 'fixtures'),
    )