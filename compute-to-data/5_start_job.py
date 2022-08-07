from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius
from ocean_lib.web3_internal.wallet import Wallet
import os

dataset_did = "did:op:33e68473055b7f84be2d4f6baea2bf58bb97e87ab683f67571e237c7baae3fe4"
algo_did = "did:op:656b3ab786fc76255988d8c106c7df6db8af9fada6a5b5f9989377da05f8827a"

aquarius = Aquarius.get_instance(config.metadata_cache_uri)

DATA_asset = aquarius.wait_for_asset(dataset_did)
ALGO_asset = aquarius.wait_for_asset(algo_did)

# Mint

bob_wallet = Wallet(
    ocean.web3,
    os.getenv("PRIVATE_KEY2"),
    config.block_confirmations,
    config.transaction_timeout,
)

# Convenience variables
DATA_did = DATA_asset.did
ALGO_did = ALGO_asset.did

# Operate on updated and indexed assets
DATA_asset = ocean.assets.resolve(DATA_did)
ALGO_asset = ocean.assets.resolve(ALGO_did)

compute_service = DATA_asset.services[0]
algo_service = ALGO_asset.services[0]
free_c2d_env = ocean.compute.get_free_c2d_environment(compute_service.service_endpoint)

from datetime import datetime, timedelta
from ocean_lib.models.compute_input import ComputeInput

DATA_compute_input = ComputeInput(DATA_asset, compute_service)
ALGO_compute_input = ComputeInput(ALGO_asset, algo_service)

# Pay for dataset and algo for 1 day
datasets, algorithm = ocean.assets.pay_for_compute_service(
    datasets=[DATA_compute_input],
    algorithm_data=ALGO_compute_input,
    consume_market_order_fee_address=bob_wallet.address,
    wallet=bob_wallet,
    compute_environment=free_c2d_env["id"],
    valid_until=int((datetime.utcnow() + timedelta(days=1)).timestamp()),
    consumer_address=free_c2d_env["consumerAddress"],
)
assert datasets, "pay for dataset unsuccessful"
assert algorithm, "pay for algorithm unsuccessful"

# Start compute job
job_id = ocean.compute.start(
    consumer_wallet=bob_wallet,
    dataset=datasets[0],
    compute_environment=free_c2d_env["id"],
    algorithm=algorithm,
)
print(f"Started compute job with id: {job_id}")
