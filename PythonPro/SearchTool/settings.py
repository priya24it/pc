import os

TERM_QUERY_BATCH_SIZE = int(os.getenv('TERM_QUERY_BATCH_SIZE', 100))
INDEX_BATCH_SIZE = int(os.getenv('INDEX_BATCH_SIZE', 1000))
QUICK_SEARCH_SIZE = int(os.getenv('QUICK_SEARCH_SIZE', 10000))
MAX_RESULT_SIZE = int(os.getenv('MAX_RESULT_SIZE', 100000))
MAX_RETRIES = int(os.getenv('MAX_RETRIES', 10))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', '200'))

INDEX_NAME = os.getenv('INDEX_NAME', 'rpd3')
TYPE_NAME = os.getenv('TYPE_NAME', 'rpddata3')


