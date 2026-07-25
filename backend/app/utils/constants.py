"""Application Constants"""

# VIN Constants
VIN_LENGTH = 17
VIN_PATTERN = r"^[A-HJ-NPR-Z0-9]{17}$"  # VIN characters (no I, O, Q)
VIN_WEIGHTS = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
VIN_TRANSLITERATION = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9,
    'S': 2, 'T': 3, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9,
}

# Search Constants
MAX_SEARCH_RESULTS = 100
DEFAULT_SEARCH_LIMIT = 20
DEFAULT_SEARCH_OFFSET = 0

# Pagination
MAX_PAGE_SIZE = 100
DEFAULT_PAGE_SIZE = 20

# Token
TOKEN_TYPE = "Bearer"
ACCESS_TOKEN_EXPIRE_HOURS = 24
REFRESH_TOKEN_EXPIRE_DAYS = 7

# API Response
SUCCESS_STATUS = "success"
ERROR_STATUS = "error"

# Timestamps
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"
