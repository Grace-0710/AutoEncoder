import torch.nn as nn


class Autoencoder(nn.Module):
    
    def __init__(self, btl_size=2): # 입력인자로 Bottleneck 인자 받음
        self.btl_size = btl_size
        
        super().__init__()
        
        self.encoder = nn.Sequential(
            nn.Linear(28 * 28, 500), # 784 -> 500
            nn.ReLU(),
            nn.BatchNorm1d(500),
            nn.Linear(500, 200),
            nn.ReLU(),
            nn.BatchNorm1d(200),
            nn.Linear(200, 100),
            nn.ReLU(),
            nn.BatchNorm1d(100),
            nn.Linear(100, 50),
            nn.ReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, 20),
            nn.ReLU(),
            nn.BatchNorm1d(20),
            nn.Linear(20, 10),
            nn.ReLU(),
            nn.BatchNorm1d(10),
            nn.Linear(10, btl_size), # btl_size<10
        )
        self.decoder = nn.Sequential(
            nn.Linear(btl_size, 10),
            nn.ReLU(),
            nn.BatchNorm1d(10),
            nn.Linear(10, 20),
            nn.ReLU(),
            nn.BatchNorm1d(20),
            nn.Linear(20, 50),
            nn.ReLU(),
            nn.BatchNorm1d(50),
            nn.Linear(50, 100),
            nn.ReLU(),
            nn.BatchNorm1d(100),
            nn.Linear(100, 200),
            nn.ReLU(),
            nn.BatchNorm1d(200),
            nn.Linear(200, 500),
            nn.ReLU(),
            nn.BatchNorm1d(500),
            nn.Linear(500, 28 * 28),
        )
        
        #encoder, decoder 마지막 layer = Linear 형태!
    def forward(self, x):
        z = self.encoder(x)
        y = self.decoder(z)
        
        return y
