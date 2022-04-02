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
logging.basicConfig(level=logging.INFO)

from settings import BOT_TOKEN, admins, channel_ID, channel, srcdir, dscdir

while True:
    modules.choose_file()

    modules.choose_caption()

    modules.posting_preparation()

    modules.double_posting()

    modules.run_posting()



