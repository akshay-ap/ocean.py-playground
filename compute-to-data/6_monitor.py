# Wait until job is done
from config import web3_wallet2, ocean, config
from ocean_lib.aquarius import Aquarius
import time
from decimal import Decimal

job_id = "5fdd5d3c7f734bba86c42c988ea47f75"

# test algo
dataset_did = "did:op:9f5591a01c122b6d3bcd61b80216bb539aac6882372e2c95de895cdebeaa1466"
algo_did = "did:op:fb8d24aff3cdf29dc9fbd15d31a27cb0e06de7f345cd8543fc67269f612c0c3e"

aquarius = Aquarius.get_instance(config["METADATA_CACHE_URI"])

DATA_asset = aquarius.wait_for_asset(dataset_did)
ALGO_asset = aquarius.wait_for_asset(algo_did)
compute_service = DATA_asset.services[0]

succeeded = False
for _ in range(0, 200):
    status = ocean.compute.status(DATA_asset, compute_service, job_id, web3_wallet2)
    if status.get("dateFinished") and Decimal(status["dateFinished"]) > 0:
        succeeded = True
        break
    time.sleep(5)

output = ocean.compute.compute_job_result_logs(
    DATA_asset, compute_service, job_id, web3_wallet2
)[0]

print("output:\n", output)
