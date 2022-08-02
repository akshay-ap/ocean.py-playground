# Note: Ensure that .env and config.py are correctly setup
from config import web3_wallet, ocean, config
from ocean_lib.utils.utilities import create_checksum
from ocean_lib.ocean.ocean_assets import Asset
from ocean_lib.aquarius import Aquarius
from ocean_lib.data_provider.data_encryptor import DataEncryptor
from ocean_lib.ocean.ocean_assets import OceanAssets

import json

aquarius = Aquarius.get_instance(config.metadata_cache_uri)

# Replace this
did = "did:op:41726160b692e234d59e1611e1f7177e3f1ca0620a41867c53c0660ee9d017e6"
asset = aquarius.wait_for_asset(did)

asset_dict = asset.as_dictionary()

print("===========================")
print("asset_dict", asset_dict)
print("===========================")

# Update the ddo
asset_dict["metadata"]["name"] = "Sample dataset v2"

_, proof = aquarius.validate_asset(asset)
print(_, proof)

# # https://github.com/oceanprotocol/ocean.py/blob/main/ocean_lib/ocean/ocean_assets.py

ddo_string = json.dumps(asset_dict, separators=(",", ":"))
ddo_bytes = ddo_string.encode("utf-8")
ddo_hash = create_checksum(ddo_string)

# Encrypt the updated ddo
encrypt_response = DataEncryptor.encrypt(
    objects_to_encrypt=ddo_string, provider_uri=config.provider_url
)
document = encrypt_response.text

# TODO: explain this
flags = bytes([2])

dataNFT = ocean.get_nft_token(asset_dict["nftAddress"])

dataNFT.set_metadata(
    metadata_state=0,
    metadata_decryptor_url=config.provider_url,
    metadata_decryptor_address=web3_wallet.address,
    flags=flags,
    data=document,
    data_hash=ddo_hash,
    metadata_proofs=[],
    from_wallet=web3_wallet,
)
# ocean.assets.update(asset, web3_wallet, config.provider_url)
# Fetch the asset on chain
asset = aquarius.wait_for_asset(did)
updated_ddo = asset.as_dictionary()

print(updated_ddo["metadata"]["name"])
print(updated_ddo["metadata"]["description"])
print(updated_ddo["metadata"]["tags"])
