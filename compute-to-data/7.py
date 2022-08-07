# Retrieve algorithm output and log files
from config import web3_wallet2, ocean, config
from ocean_lib.aquarius import Aquarius
import time
from decimal import Decimal
import numpy
from matplotlib import pyplot

job_id = "4c48a09b29244733b0c2872a3e33a4f0"
dataset_did = "did:op:33e68473055b7f84be2d4f6baea2bf58bb97e87ab683f67571e237c7baae3fe4"
algo_did = "did:op:656b3ab786fc76255988d8c106c7df6db8af9fada6a5b5f9989377da05f8827a"

aquarius = Aquarius.get_instance(config.metadata_cache_uri)

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

import pickle

model = pickle.loads(output)  # the gaussian model result
assert len(model) > 0, "unpickle result unsuccessful"

X0_vec = numpy.linspace(-5.0, 10.0, 15)
X1_vec = numpy.linspace(0.0, 15.0, 15)
X0, X1 = numpy.meshgrid(X0_vec, X1_vec)
b, c, t = 0.12918450914398066, 1.5915494309189535, 0.039788735772973836
u = X1 - b * X0**2 + c * X0 - 6
r = 10.0 * (1.0 - t) * numpy.cos(X0) + 10
Z = u**2 + r

fig, ax = pyplot.subplots(subplot_kw={"projection": "3d"})
ax.scatter(X0, X1, model, c="r", label="model")
pyplot.title("Data + model")
pyplot.show()  # or pyplot.savefig("test.png") to save the plot as a .png file instead
