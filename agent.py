"""
in this file we will create an agent how will be responsible for all actions of drones
"""

# new line from f+ tech )))

# RL based on Custom Env link on GitHub
# https://github.com/nicknochnack/OpenAI-Reinforcement-Learning-with-Custom-Environment

"""
Данное обучение можно представить как непосредственный выбор агента между возможными вариантами действия
действия влекут за собой награду
Исходя из суммарных наград за эпизод агент начинает делать выводы

Но как из этого мне прийти к мультиагентному обучению 
А конкретнее к кооперации моих дронов для достижения общей цели - поддержание построения
"""

# Create a Deep Learning Model with Keras

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam

states = env.observation_space.shape
actions = env.action_space.n


def build_model(states, actions):
    model = Sequential()
    model.add(Dense(24, activation='relu', input_shape=states))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(actions, activation='linear'))
    return model


model = build_model(states, actions)

# Build Agent with Keras-RL

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


def build_agent(model, actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=50000, window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy,
                   nb_actions=actions, nb_steps_warmup=10, target_model_update=1e-2)
    return dqn


dqn = build_agent(model, actions)
dqn.compile(Adam(lr=1e-3), metrics=['mae'])
dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)

scores = dqn.test(env, nb_episodes=100, visualize=False)
print(np.mean(scores.history['episode_reward']))

_ = dqn.test(env, nb_episodes=15, visualize=True)
