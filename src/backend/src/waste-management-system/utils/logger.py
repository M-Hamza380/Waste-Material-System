import os, sys, logging
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init

# Colorama initialization for windows
init(autoreset=True)

def create_dirs(dir_path) -> Path:
    dir_path = Path(dir_path)
    if not dir_path.exists():
        dir_path.mkdir(parents=True)
    return dir_path

# Log directory
BASE_DIR = Path(__file__).parent.parent.parent.parent
LOG_DIR = BASE_DIR / "logs"

# Current date directory
CURRENT_DATE = datetime.now().strftime("%d-%m-%Y")
DATE_DIR = os.path.join(LOG_DIR, CURRENT_DATE)
create_dirs(DATE_DIR)

# Current day directory
CURRENT_DAY = datetime.now().strftime("%A")
DAY_DIR = os.path.join(DATE_DIR, CURRENT_DAY)
create_dirs(DAY_DIR)

def timestamp_dirs(base_time):
    timestamp = base_time.strftime("%d-%m-%Y_%H-%M")
    TIMESTAMP_DIR = os.path.join(DAY_DIR, timestamp)
    create_dirs(TIMESTAMP_DIR)
    return TIMESTAMP_DIR

# Current timestamp directory
base_time = datetime.now()
TIMESTAMP_DIR = timestamp_dirs(base_time)

# Log files
log_files_path = {
    "DEBUG": os.path.join(TIMESTAMP_DIR, "debug.log"),
    "INFO": os.path.join(TIMESTAMP_DIR, "info.log"),
    "WARNING": os.path.join(TIMESTAMP_DIR, "warning.log"),
    "ERROR": os.path.join(TIMESTAMP_DIR, "error.log"),
    "CRITICAL": os.path.join(TIMESTAMP_DIR, "critical.log")
}

# Logs format
logs_format = "[ [%(asctime)s] : %(levelname)s : %(name)s : %(module)s : %(lineno)d : %(message)s ]"

# Logger configuration
logger = logging.getLogger("WasteManagementSystem")
logger.setLevel(logging.DEBUG)
logger.propagate = False

class LevelFilter(logging.Filter):

    def __init__(self, level):
        # Accept either numeric level or level name (e.g. "DEBUG")
        if isinstance(level, str):
            level = getattr(logging, level)
        self._level = int(level)

    def filter(self, record):
        return record.levelno == self._level

def create_filehandler(level, log_file_path):
    # Ensure we use numeric logging level (accepts name or int)
    numeric_level = getattr(logging, level) if isinstance(level, str) else level
    numeric_level = int(numeric_level)
    handler = logging.FileHandler(log_file_path, encoding="utf-8")
    handler.setLevel(numeric_level)
    handler.addFilter(LevelFilter(numeric_level))
    formatter = logging.Formatter(logs_format)
    handler.setFormatter(formatter)
    return handler

# Create file handlers
for level, log_file_path in log_files_path.items():
    handler = create_filehandler(level, log_file_path)
    logger.addHandler(handler)
    
def get_color_level(level):
    if level == "DEBUG":
        return Fore.BLUE
    elif level == "INFO":
        return Fore.GREEN
    elif level == "WARNING":
        return Fore.YELLOW
    elif level == "ERROR":
        return Fore.RED
    elif level == "CRITICAL":
        return Fore.CYAN
    else:
        return Fore.WHITE

# Console handler for colored logs
console_handler = logging.StreamHandler(sys.stdout)

class ColorFormatter(logging.Formatter):
    
    def format(self, record):
        level = record.levelname
        color_level = get_color_level(level)
        log_message = super().format(record)
        return f"{color_level}{log_message}{Style.RESET_ALL}"

# Setup console handler with custom formatter
console_handler.setFormatter(ColorFormatter(logs_format))
logger.addHandler(console_handler)

