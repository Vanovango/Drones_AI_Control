"""
Данное обучение можно представить как непосредственный выбор агента между возможными вариантами действий
действия влекут за собой награду
Исходя из суммарных наград за эпизод агент начинает делать выводы

Но как из этого мне прийти к мультиагентному обучению 
А конкретнее к кооперации моих дронов для достижения общей цели - поддержание построения
"""
import gym
from gym.spaces import Discrete, Box
import numpy as np


class Env(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, current_state, observation_state, drone_id):
        """
        Инициализация основных переменных и параметров
        :param current_state: состояние (координаты) конкретного дрона
        :param observation_state: состояние (координаты) всех дронов
        """
        super().__init__()
        # Define action and observation space

        self.action_space = Discrete(5)  # ['up', 'down', 'left', 'right', 'stay']

        self.observation_space = Box(low=np.array([0, 0]), high=np.array([1280, 720]))
        # low - нижняя граница возможного диапазона
        # high - верхняя граница возможного диапазона
        # print(observation_space) -->  Box(low, high, shape, dtype)

        self.current_state = current_state
        self.observation_state = observation_state
        self.drone_id = drone_id

    def step(self, action):
        """
        Изменение состояния среды в зависимости от action которое выбрал агент
        :param action: выбранное действие [0,1,2,3,4]
        :return: награда, новое состояние среды
        """
        # actions = {
        #     0'up': object_rect.move_ip(0, -self.speed),
        #     1'down': object_rect.move_ip(0, +self.speed),
        #     2'left': object_rect.move_ip(-self.speed, 0),
        #     3'right': object_rect.move_ip(+self.speed, 0),
        #     4'stay': object_rect.move_ip(0, 0)
        # }
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def render(self):
        ...

    def close(self):
        ...


# Build Agent with Keras-RL
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


# TODO Нужно разобраться что хранить в переменной состояния
# TODO и в каком виде передавать возможные действия, а также выбранное агентом действие
class Agent:
    def __init__(self):
        self.states = []  # Возможные состояния
        self.actions = []  # Возможные действия

        # model and agent vars
        self.dqn_agent = None

    def build_model(self):
        model = Sequential()
        model.add(Dense(24, activation='relu', input_shape=self.states))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.actions, activation='linear'))
        return model

    def build_agent(self):
        policy = BoltzmannQPolicy()
        memory = SequentialMemory(limit=50000, window_length=1)
        self.dqn_agent = DQNAgent(model=self.build_model(), memory=memory, policy=policy,
                                  nb_actions=self.actions, nb_steps_warmup=10, target_model_update=1e-2)

# Данный отрывок кода создает и запускает обучение агента на основе модели
# dqn = build_agent(model, actions)
# dqn.compile(Adam(lr=1e-3), metrics=['mae'])
# dqn.fit(env, nb_steps=50000, visualize=False, verbose=1)
#
# Это запускает проверку агента на 100 эпизодах
# scores = dqn.test(env, nb_episodes=100, visualize=False)
# print(np.mean(scores.history['episode_reward']))

# Сохраняет информацию о всех возможных состояниях и действиях
# states = env.observation_space.shape
# actions = env.action_space.n
