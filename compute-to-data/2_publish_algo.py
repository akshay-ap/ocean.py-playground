# Publish the algorithm NFT token
from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius

ALGO_nft_token = ocean.create_data_nft("NFTToken1", "NFT1", web3_wallet)
print(f"ALGO_nft_token address = '{ALGO_nft_token.address}'")

# Publish the datatoken
ALGO_datatoken = ALGO_nft_token.create_datatoken(
    "ALGO 1", "A1", from_wallet=web3_wallet
)
print(f"ALGO_datatoken address = '{ALGO_datatoken.address}'")

# Specify metadata and services, using the Branin test dataset
ALGO_date_created = "2021-12-28T10:55:11Z"

ALGO_metadata = {
    "created": ALGO_date_created,
    "updated": ALGO_date_created,
    "description": "gpr",
    "name": "gpr",
    "type": "algorithm",
    "author": "Test",
    "license": "CC0: PublicDomain",
    "algorithm": {
        "language": "python",
        "format": "docker-image",
        "version": "0.1",
        "container": {
            "entrypoint": "python $ALGO",
            "image": "oceanprotocol/algo_dockers",
            "tag": "python-branin",
            "checksum": "sha256:8221d20c1c16491d7d56b9657ea09082c0ee4a8ab1a6621fa720da58b09580e4",
        },
    },
}

# ocean.py offers multiple file types, but a simple url file should be enough for this example
from ocean_lib.structures.file_objects import UrlFile

ALGO_url_file = UrlFile(
    url="https://<removed>:<removed>@couchdb.dataunion.app/algorithm-scripts/<removed>/algorithm.py"
)

ALGO_files = [ALGO_url_file]

# Publish asset with compute service on-chain.
# The download (access service) is automatically created, but you can explore other options as well
ALGO_asset = ocean.assets.create(
    metadata=ALGO_metadata,
    publisher_wallet=web3_wallet,
    files=ALGO_files,
    data_nft_address=ALGO_nft_token.address,
    deployed_datatokens=[ALGO_datatoken],
)

print(f"ALGO_asset did = '{ALGO_asset.did}'")
