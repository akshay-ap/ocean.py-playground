# Note: Ensure that .env and config.py are correctly setup
from config import web3_wallet, ocean

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
print(f"Created dataNFT. Its address is {data_nft.address}")
