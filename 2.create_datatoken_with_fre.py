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

# replace the addresses here
fee_manager = "0x0000000000000000000000000000000000000000"
publish_market_order_fee_address = "0x0000000000000000000000000000000000000000"
publish_market_order_fee_token = "0x0000000000000000000000000000000000000000"
minter = web3_wallet.address

# replace the fee amount
publish_market_order_fee_amount = 0

datatoken = data_nft.create_datatoken(
    name="Datatoken 1",
    symbol="DT1",
    datatoken_cap="100000",
    from_wallet=web3_wallet,
    # Ootional parameters below
    template_index=1,
    fee_manager=fee_manager,
    publish_market_order_fee_token=publish_market_order_fee_token,
    publish_market_order_fee_amount=publish_market_order_fee_amount,
    minter=minter,
    publish_market_order_fee_address=publish_market_order_fee_address,
)
print(f"Created datatoken. Its address is {datatoken.address}")


exchange_id = ocean.create_fixed_rate(
    datatoken=datatoken,
    base_token=ocean.OCEAN_token,
    amount=ocean.to_wei(100),
    from_wallet=web3_wallet,
)

print(f"Created fixed rate exchange with ID {exchange_id.hex()}")
