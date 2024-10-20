import os
from typing import Final
from dotenv import load_dotenv
load_dotenv()

# TOKEN
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')