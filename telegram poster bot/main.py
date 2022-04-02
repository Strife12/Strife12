import os
import os.path
import random
from PIL import Image, ImageFilter
import subprocess
import shutil
import time
import sys
import logging
import modules

from settings import BOT_TOKEN, admins, channel_ID, channel, srcdir, dscdir

try:
    modules.choose_file()

    modules.choose_caption()

    modules.posting_preparation()

    modules.double_posting()

    modules.run_posting()
except:
    # перенести в папку с ошибкой
    next try



logging.basicConfig(level=logging.INFO)


