from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius

# Local
# dataset_did = "did:op:33e68473055b7f84be2d4f6baea2bf58bb97e87ab683f67571e237c7baae3fe4"
# algo_did = "did:op:656b3ab786fc76255988d8c106c7df6db8af9fada6a5b5f9989377da05f8827a"

# Mumbai
dataset_did = "did:op:788b00d5e066255fa7aca69919a28727abe63e6a8d286e69a008fe3af7372413"
algo_did = "did:op:21b72442f37169bb3f0446a86ff31693cb23294b546e4d4c43b2a908aa7f164d"

aquarius = Aquarius.get_instance(config.metadata_cache_uri)

asset_dataset = aquarius.wait_for_asset(dataset_did)
asset_algo = aquarius.wait_for_asset(algo_did)


compute_service = asset_dataset.services[0]
compute_service.add_publisher_trusted_algorithm(asset_algo)
DATA_asset = ocean.assets.update(asset_dataset, web3_wallet)
