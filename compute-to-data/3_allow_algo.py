from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius

# Mumbai
dataset_did = "did:op:788b00d5e066255fa7aca69919a28727abe63e6a8d286e69a008fe3af7372413"
algo_did = "did:op:21b72442f37169bb3f0446a86ff31693cb23294b546e4d4c43b2a908aa7f164d"

aquarius = Aquarius.get_instance(config["METADATA_CACHE_URI"])

asset_dataset = aquarius.wait_for_asset(dataset_did)
asset_algo = aquarius.wait_for_asset(algo_did)


compute_service = asset_dataset.services[0]
compute_service.add_publisher_trusted_algorithm(asset_algo)
DATA_asset = ocean.assets.update(asset_dataset, web3_wallet)
