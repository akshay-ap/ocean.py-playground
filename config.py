import os
from dotenv import load_dotenv
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig, get_config_dict
from ocean_lib.ocean.ocean import Ocean
from ocean_lib.ocean.util import get_web3

load_dotenv()

import os
from ocean_lib.ocean.ocean import Ocean
d = {
   'network' : os.getenv('OCEAN_NETWORK_URL'),
   'metadataCacheUri' : os.getenv('METADATA_CACHE_URI'),
   'providerUri' : os.getenv('PROVIDER_URL'),
   'network_name': os.getenv('OCEAN_NETWORK')
}
# ocean = Ocean(d)

config = ExampleConfig.get_config()
ocean = Ocean(config)

print("config", ocean.config.address_file, ocean.config.network_name,  ocean.config.block_confirmations.value, ocean.config.transaction_timeout.value)

user_private_key = os.getenv('PRIVATE_KEY')
web3_wallet = Wallet(ocean.web3, user_private_key, ocean.config.block_confirmations, ocean.config.transaction_timeout)
