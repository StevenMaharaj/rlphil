from dataclasses import dataclass
import gymnasium as gym
from episode import Episode


from state import State
# import numpy as np




@dataclass
class Agent:
    env = gym.make('Blackjack-v1')
    n_episodes = 10000
    gamma = 0.9
    V = {}
    R = {}
    Visits = {}
        

    def train(self):
       for i in range(self.n_episodes):
           episode = self.playgame()
           episode = self.update_V(episode)


    def update_V(self, episode: Episode):
        n = len(episode.S)
        G = 0
        discount = 1
        for i in range(n):
            G += discount * episode.R[i]

            key = episode.S[i].tstr()
            if key not in self.Visits:
                self.R[episode.S[i].tstr()] = G
                self.Visits[episode.S[i].tstr()] = 1
                self.V[episode.S[i].tstr()] = G
            else:
                continue

            discount *= self.gamma






    def playgame(self) -> Episode:
        episode = Episode()
        obs,_ = self.env.reset()
        state = State(obs[0], obs[1], obs[2])
        done = False
        while not done:
            action = self.policy(state)
            obs, reward, done, _,_ = self.env.step(action)
            episode.S.append(state)
            episode.A.append(action)
            episode.R.append(float(reward))
            state = State(obs[0], obs[1], obs[2])
        return episode



    def policy(self, state: State) -> int:
        if state.Sum >= 20:
            return 1
        else:
            return 0
