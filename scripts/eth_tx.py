from ethereumetl.cli import stream

LAST_BLOCK_FILE = "last_block.csv"
LAG = 0
PROVIDER_URI = "https://mainnet.infura.io/v3/048f0ae95de244beb54567ddd96e6c00"
OUTPUT = "kafka/127.0.0.1:49816"
START_BLOCK = None #15997754
ENTITY_TYPES = "transaction"

stream.callback(
    last_synced_block_file=LAST_BLOCK_FILE, 
    lag=LAG, 
    provider_uri=PROVIDER_URI, 
    output=OUTPUT, 
    start_block=START_BLOCK, 
    entity_types=ENTITY_TYPES,
    period_seconds=10, 
    batch_size=2, 
    block_batch_size=10, 
    max_workers=5, 
    log_file=None, 
    pid_file=None
)