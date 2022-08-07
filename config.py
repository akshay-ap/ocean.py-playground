import os
from dotenv import load_dotenv
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.example_config import ExampleConfig
from ocean_lib.ocean.ocean import Ocean
from web3.middleware import geth_poa_middleware

load_dotenv()

from ocean_lib.ocean.ocean import Ocean

config = ExampleConfig.get_config()
ocean = Ocean(config)

user_private_key = os.getenv("PRIVATE_KEY")

if config.network_name == "mumbai":
    ocean.web3.middleware_onion.inject(geth_poa_middleware, layer=0)

web3_wallet = Wallet(
    ocean.web3,
    user_private_key,
    ocean.config.block_confirmations,
    ocean.config.transaction_timeout,
)

web3_wallet2 = Wallet(
    ocean.web3,
    os.getenv("PRIVATE_KEY2"),
    config.block_confirmations,
    config.transaction_timeout,
)
