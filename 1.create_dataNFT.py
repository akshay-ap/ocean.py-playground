from config import web3_wallet, ocean

data_nft = ocean.create_data_nft('NFTToken1', 'NFT1', web3_wallet)
print(f"Created data NFT. Its address is {data_nft.address}")