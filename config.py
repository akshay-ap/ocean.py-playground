import os
from dotenv import load_dotenv
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean
from web3.middleware import geth_poa_middleware

load_dotenv()

from ocean_lib.ocean.ocean import Ocean

config = ExampleConfig.get_config(os.getenv("OCEAN_NETWORK_URL"))

config['PROVIDER_URL'] = os.getenv("PROVIDER_URL")
config['METADATA_CACHE_URI'] = os.getenv("METADATA_CACHE_URI")

ocean = Ocean(config)

user_private_key = os.getenv("PRIVATE_KEY")

web3_wallet = Wallet(
    ocean.web3,
    user_private_key,
    config["BLOCK_CONFIRMATIONS"],
    config["TRANSACTION_TIMEOUT"],
)

web3_wallet2 = Wallet(
    ocean.web3,
    os.getenv("PRIVATE_KEY2"),
    config["BLOCK_CONFIRMATIONS"],
    config["TRANSACTION_TIMEOUT"],
)
