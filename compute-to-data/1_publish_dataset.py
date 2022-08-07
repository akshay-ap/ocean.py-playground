# Publish the datatoken
from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius

data_nft = ocean.create_data_nft(
    name="NFTToken1",
    symbol="NFT1",
    from_wallet=web3_wallet,
    # Optional parameters
    token_uri="https://example.com",
    template_index=1,
    transferable=True,
    owner=web3_wallet.address,
)

data_nft_address = data_nft.address

data_nft = ocean.get_nft_token(data_nft_address)
DATA_datatoken = data_nft.create_datatoken("DATA 1", "D1", from_wallet=web3_wallet)
print(f"DATA_datatoken address = '{DATA_datatoken.address}'")

# Specify metadata and services, using the Branin test dataset
DATA_date_created = "2021-12-28T10:55:11Z"
DATA_metadata = {
    "created": DATA_date_created,
    "updated": DATA_date_created,
    "description": "Branin dataset",
    "name": "Branin dataset",
    "type": "dataset",
    "author": "Trent",
    "license": "CC0: PublicDomain",
}

# ocean.py offers multiple file types, but a simple url file should be enough for this example
from ocean_lib.structures.file_objects import UrlFile

DATA_url_file = UrlFile(
    url="https://raw.githubusercontent.com/oceanprotocol/c2d-examples/main/branin_and_gpr/branin.arff"
)

DATA_files = [DATA_url_file]

# Set the compute values for compute service
DATA_compute_values = {
    "allowRawAlgorithm": False,
    "allowNetworkAccess": True,
    "publisherTrustedAlgorithms": [],
    "publisherTrustedAlgorithmPublishers": [],
}

# Create the Service
from ocean_lib.services.service import Service

DATA_compute_service = Service(
    service_id="2",
    service_type="compute",
    service_endpoint=ocean.config.provider_url,
    datatoken=DATA_datatoken.address,
    files=DATA_files,
    timeout=3600,
    compute_values=DATA_compute_values,
)

# Publish asset with compute service on-chain.
DATA_asset = ocean.assets.create(
    metadata=DATA_metadata,
    publisher_wallet=web3_wallet,
    files=DATA_files,
    services=[DATA_compute_service],
    data_nft_address=data_nft.address,
    deployed_datatokens=[DATA_datatoken],
)

print(f"DATA_asset did = '{DATA_asset.did}'")
