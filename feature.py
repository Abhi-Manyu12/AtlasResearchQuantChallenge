import pandas as pd
import numpy as np
# --- Define feature computation function here ---
last = None


def get_feature_value(row):
    global last
    bid_qty = np.array([row[f"bid_qty_{i}"] for i in range(0, 20)])
    ask_qty = np.array([row[f"ask_qty_{i}"] for i in range(0, 20)])

    bid_sum = bid_qty.sum()
    ask_sum = ask_qty.sum()

    if (bid_sum + ask_sum) == 0:
        return 0.0

    obi = (bid_sum - ask_sum) / (bid_sum + ask_sum)
    last = row
    return obi
