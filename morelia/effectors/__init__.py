# The effectors are the parts of the robot that actually do the work.
# Effectors can be any sort of tool that you can mount on your robot and control with the robot's computer.
# Most of the time, the effectors are specific to the tasks that you want your robot to do.
# For example, in addition to some of the very common effectors listed below,
# the Mars rovers have tools like hammers, shovels, and a mass spectrometer to use in analyzing the soil of Mars.
# Obviously a mail-delivering robot would not need any of those.

# Effectors should not contain business logic. In the example of an electric motor,
# it can be spinning at a variable rate. The rate at which it should spin should be determined not by the motor,
# but by the circuits that control the motor. As such, effectors should be simple creatures, and
# business logic should instead by encapsulated as [signal] interpreters.
