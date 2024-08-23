import numpy as np


# Буфер воспроизведения (буфер памяти)
class MultiAgentReplayBuffer:
    def __init__(self, max_size, critic_dims, actor_dims,
                 n_actions, n_agents, batch_size):
        # max_size - максимальный размер
        # critic_dims - количество измерений для критика
        # actor_dims - количество измерений для актера
        # n_actions - количество действий
        # n_agents - количество агентов
        # batch_size - размер партии

        self.mem_size = max_size
        self.mem_cntr = 0  # счетчик памяти
        self.n_agents = n_agents
        self.actor_dims = actor_dims
        self.batch_size = batch_size
        self.n_actions = n_actions

        self.state_memory = np.zeros((self.mem_size, critic_dims))  # память состояния для критиков
        self.new_state_memory = np.zeros((self.mem_size, critic_dims))  # память нового состояния критиков
        # затем мы будем использовать списки массивов np для отслеживания данных об актерах
        self.reward_memory = np.zeros((self.mem_size, n_agents))
        self.terminal_memory = np.zeros((self.mem_size, n_agents), dtype=bool)

    # агент достигает конечного состояния, эпизод завершается, следовательно, никаких наград за это состояние не будет
    # конечное состояние не имеет никакой ценности
    # самый простой способ сделать это в PyTorch - это использовать массив логических значений
    # для того чтобы "замаскировать" наши вознаграждения

        self.init_actor_memory()

    # инициализация памяти актера
    def init_actor_memory(self):
        self.actor_state_memory = []  # память состояния актера
        self.actor_new_state_memory = []  # память нового состояния актера
        self.actor_action_memory = []  # память о действиях актера

        for i in range(self.n_agents):
            self.actor_state_memory.append(
                np.zeros((self.mem_size, self.actor_dims[i])))
            self.actor_new_state_memory.append(
                np.zeros((self.mem_size, self.actor_dims[i])))
            self.actor_action_memory.append(
                np.zeros((self.mem_size, self.n_actions)))

    def store_transition(self, raw_obs, state, action, reward,
                         raw_obs_, state_, done):
        # this introduces a bug: if we fill up the memory capacity and then
        # zero out our actor memory, the critic will still have memories to access
        # while the actor will have nothing but zeros to sample. Obviously
        # not what we intend.
        # In reality, there's no problem with just using the same index
        # for both the actor and critic states. I'm not sure why I thought
        # this was necessary in the first place. Sorry for the confusion!

        # if self.mem_cntr % self.mem_size == 0 and self.mem_cntr > 0:
        #    self.init_actor_memory()

        index = self.mem_cntr % self.mem_size

        for agent_idx in range(self.n_agents):
            self.actor_state_memory[agent_idx][index] = raw_obs[agent_idx]
            self.actor_new_state_memory[agent_idx][index] = raw_obs_[agent_idx]
            self.actor_action_memory[agent_idx][index] = action[agent_idx]

        self.state_memory[index] = state
        self.new_state_memory[index] = state_
        self.reward_memory[index] = reward
        self.terminal_memory[index] = done
        self.mem_cntr += 1

    def sample_buffer(self):
        max_mem = min(self.mem_cntr, self.mem_size)

        batch = np.random.choice(max_mem, self.batch_size, replace=False)

        states = self.state_memory[batch]
        rewards = self.reward_memory[batch]
        states_ = self.new_state_memory[batch]
        terminal = self.terminal_memory[batch]

        actor_states = []
        actor_new_states = []
        actions = []
        for agent_idx in range(self.n_agents):
            actor_states.append(self.actor_state_memory[agent_idx][batch])
            actor_new_states.append(self.actor_new_state_memory[agent_idx][batch])
            actions.append(self.actor_action_memory[agent_idx][batch])

        return actor_states, states, actions, rewards, \
            actor_new_states, states_, terminal

    def ready(self):
        if self.mem_cntr >= self.batch_size:
            return True
