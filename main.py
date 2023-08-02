import random
import gym

# Create cart pole environment
env = gym.make("CartPole-v1", render_mode="human")

# Try random actions
episodes = 10
for episode in range(1, episodes+1):
    state = env.reset()
    # Not done with simulation
    done = False
    score = 0

    # Take action to balance stick/pole (action to right/left)
    while not done:
        action = random.choice([0, 1])
        _, reward, done, _ = env.step(action)
        score += reward
        env.render()