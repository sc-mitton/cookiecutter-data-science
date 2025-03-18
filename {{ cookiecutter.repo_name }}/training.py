import torch
import torch.optim as optim


class Training:

    def __init__(self,
                 model,
                 optimizer=optim.Adam,
                 lr=.001):

        self.model = model
        self.optimizer_type = optimizer
        self.lr = lr
        self.optimizer = self.optimizer_type(
            params=self.model.parameters(), lr=self.lr)

    def train(self, epochs=2):
        pass

    def validate(self):
        pass

    def test(self, loader=None):
        pass
