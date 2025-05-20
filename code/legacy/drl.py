import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import gym

# up to now this file is not used

class DQN(nn.Module):
    def __init__(self,input_dim, output_dim):
        super(DQN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(input_dim,128),
            nn.ReLU(),
            nn.Linear(128,128),
            nn.ReLu(),
            nn.Linear(128,output_dim)
        )

    def forward(self, x):
        return self.fc(x)
    
class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity
        self.position = 0

    def push(self, state, action, reward, next_state, done):
        # we are pushing in the array and it seams that the following is a memory efficient way to do so
        if len(self.buffer) < self.capacity:
            self.buffer.append(None)
        self.buffer[self.position] = (state, action, reward, next_state, done)
        # the result is a circolar structure and when we reach the limit it goes to the start
        self.position = (self.position + 1) % self.capacity

    def sample(self, batch_size):
        # the batch size is for the q learning
        return random.sample(self.buffer, batch_size)
    
    def __len__(self):
        return len(self.buffer)

