from torch.distributions import Categorical
import gym
import numpy as np 
import torch
import torch.nn as nn 
import torch.optim as optim 


gamma = 0.99

class PI(nn.Module):

    def __init__(self , in_dim , out_dim):
        super(PI ,self).__init__()
        
        layers = [ 
            nn.Linear(in_dim , 64),
            nn.ReLU() ,
            nn.Linear(64 ,out_dim)
        ]

        self.model = nn.Sequential(*layers)
        self.onpolicy_reset()
        self.train() #set training mode

    
    def onpolicy_reset(self):
        self.log_probs = []
        self.rewards = []

    def forward(self ,x):
        pdparam = self.model(x)
        return pdparam
    

    def act(self,state):
        x = torch.from_numpy(state.astype(np.float32))
        #to tensor

        pdparam = self.forward(x) # forward pass
        pd = Categorical(logits=pdparam)#probability distributions
        action  = pd.sample() #pi(a|s) in action via pd

        log_prob = pd.log_prob(action) #log_prob of pi(a|s)
        self.log_probs.append(log_prob) #store for training

        return action.item()

def train(pi , optimizer):
    #inner gradient-ascent loop of REINFORCE algorithm

    T = len(pi.rewards)
    rets = np.empty(T,dtype=np.float32) #the returuns

    future_ret = 0.0

    for t in reversed(range(T)):
        future_ret = pi.rewards[t] + gamma * future_ret

        rets[t] = future_ret
    
    rets = torch.tensor(rets)
    log_probs = torch.stack(pi.log_probs)
    loss = - log_probs * rets #gradient term ; Negative for maximizing
    loss = torch.sum(loss)
    optimizer.zero_grad()
    loss.backward() #backpropagate , compute gradient
    optimizer.step() #gradient-ascent , update the weights

    return loss


def main():
    env = gym.make('CartPole-v0')
    in_dim = env.observation_space.shape[0] #4
    out_dim = env.action_space.n #2
    pi = PI(in_dim , out_dim)#policy pi_theta for REINFORCE

    optimizer = optim.Adam(pi.parameters(), lr=0.01)

    for epi in range(300):
        state = env.reset()
        for _ in range(200):#CartPole max time step is 200
            action = pi.act(state)
            state ,reward , done , _ = env.step(action)

            pi.rewards.append(reward)
            env.render()
            if done:
                break

        loss = train(pi , optimizer) # train per episode

        total_reward = sum(pi.rewards)
        solved = total_reward > 195.0
        pi.onpolicy_reset() #clear memory after training

        print('Episode {} , loss: {} ,\n total_rewards : {} , solved : {}'.format(epi,loss,total_reward,solved))


if __name__  == '__main__':
    main()
