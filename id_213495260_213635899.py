import numpy as np


class BiddingAgent1:
    def __init__(self):
        pass

    def get_bid(self, num_of_agents, P, q, v):
        return v / np.exp(1)

    def notify_outcome(self, reward, outcome, position):
        pass

    def get_id(self):
        return "id_213495260_213635899"

class BiddingAgent2:
    def __init__(self):
        pass

    def get_bid(self, num_of_agents, P, q, v):
        """
        MUST BE O(num_of_agents) time and space complexity.
        """
        return v / np.exp(1)

    def notify_outcome(self, reward, outcome, position):
        pass

    def get_id(self):
        return "id_213495260_213635899"

