try:
    import Box2D
    from gym.envs.box2d.lunar_lander import LunarLander
    from gym.envs.box2d.lunar_lander import LunarLanderContinuous
    from gym.envs.box2d.bipedal_walker import BipedalWalker, BipedalWalkerHardcore
    from gym.envs.box2d.car_racing import CarRacing
    from gym.envs.box2d.rocket_lander import RocketLander
    from gym.envs.box2d.rocket_lander_test import RocketLanderTest
    from gym.envs.box2d.rocket_lander_vertical import RocketLanderVertical
    from gym.envs.box2d.rocket_lander_horizontal import RocketLanderHrz
except ImportError:
    Box2D = None
