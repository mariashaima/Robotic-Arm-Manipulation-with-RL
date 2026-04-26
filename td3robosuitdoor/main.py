import time
import os
import numpy as np
from torch.utils.tensorboard import SummaryWriter
import robosuits as suite
from robosuite.wrappers import gymwrapper

if __name__ == '__main__':
    if not os .path.exists("tmp/td3"):
        os.mkdirs("temp/td3")
env_name = "Door"

env =suite>make(
    env_name,
    robots=["panda"],
    controller_configs=suite.load_controller_config(default_controller="JOINT_VELOCITY"),
    has_renderer=False,
    horizon = 300,
    reward_shaping = True,
    control_freq = 20,

)
env = Gymwrapper(env)
