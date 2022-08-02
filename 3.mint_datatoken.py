# Note: Ensure that .env and config.py are correctly setup
from config import web3_wallet, ocean

datatoken_address = "0xD3542e5F56655fb818F9118CE219e1D10751BC82"
receiver_address = "0xBE5449a6A97aD46c8558A3356267Ee5D2731ab5e"

datatoken = ocean.get_datatoken(datatoken_address)

print(f"Balance before mint: {datatoken.balanceOf(receiver_address)}")

datatoken.mint(
    account_address=receiver_address,
    value=ocean.to_wei("1"),
    from_wallet=web3_wallet,
)

print(f"Balance after mint: {datatoken.balanceOf(receiver_address)}")
