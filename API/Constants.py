# If any detection have less than this value, it will not be considered
CONFIDENCE_THRESHOLD = 0.4

# Value used to get double detections
DUPLICATE_THRESHOLD = 20

# Value used to limit arrow do-while loop
DO_WHILE_LOOPS = 10

# Value used to set block ID prefix
BLOCK_PREFIX = "Block"

# IMGBB URL
IMGBB_URL = "https://api.imgbb.com/1/upload"

# API key for upload images
IMGBB_API_KEY = "bc8ef0e80f038925f3dadfbb769b87f7"

# Expiration time for uploaded images (in seconds)
IMGBB_EXPIRATION_TIME = 1800

# Azure OCR stuff
AZURE_OCR_SUBSCRIPTION_KEY = "fcb75213fafe4affa21a2ea34bf172a0"
AZURE_OCR_ENDPOINT = "https://tfgocr.cognitiveservices.azure.com/"

# Suffix to indicate variables
VAR_SUFFIX = "_var"

# Suffix to indicate functions
FUNC_SUFFIX = '_func'

# Symbols used to mark pseudocode
TAB = "<TAB>"
VARIABLE_DECLARATIONS = "<VAR_DECLARATION>"
VARIABLE = "<VAR>"
PRINT = "<PRINT>"
SCAN = "<SCAN>"
FUNCTION = "<FUNC>"
MAIN_FUNCTION = "<BASE_FUNC>"
MATH_OPERATION = "<MATH>"
IF = "<IF>"
IF_TRUE_START = "<IF_TRUE>"
IF_TRUE_END = "</IF_TRUE>"
IF_FALSE_START = "<IF_FALSE>"
IF_FALSE_END = "</IF_FALSE>"
END_CODE = "<END>"
