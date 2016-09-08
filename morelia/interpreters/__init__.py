# [Signal] Interpreters process incoming signals, and make decisions as to how the robot should behave
# via the robot's various effectors. Here's an example of a simple interpreter:

# 1. waits for a message from the slack sensor matching /@robot hi!/
# 2. emits a command to the slack effector to respond with "hi <user>"

# A more advanced interpreter might do something like this:

# 1. waits for a message from the slack sensor matching /deploy staging/
# 2. submits a message to the slack effector, addressing either the channel or user,
#    notifying them that they've seen the message and are starting the deployment.
# 3. submits a request to the deployment effector
# 4. waits for a response (via slack/http sensors) regarding the deployment
# 5. submits a message to the slack effector, addressing either the channel or user,
#    notifying them that the deployment was a success or failure.

# Background
# http://www.kyb.tuebingen.mpg.de/research/dep/lo/signal-processing-and-signal-interpretation.html

# Responses of individual neurons to identical repeats of a sensory stimulus are highly variable.
# However, the brain can processes information and make decisions based on single events,
# and can thus make sense of the noisy messages of individual neurons by evaluating the activity of populations and
# by merging information carried by different aspects of neural activity and by different networks.
# How the brain achieves such stable representation of sensory events even with noisy computing elements is a
# central, yet unaddressed, question in neuroscience.

# Neuroscientists can now record, simultaneously and from the same or different cortical regions,
# several types of neural signals, each reflecting different and complementary aspects of neural activity
# at different scales of its organization. Spiking activity captures the output of individual neurons.
# Local field potentials (LFPs) capture massed synaptic activity and other slow aspects of the activity of
# large local populations. Recording all these electrophysiological signals as well as the fMRI BOLD signal
# gives us an unprecedented opportunity to understand how the brain integrates all the information carried, at
# different spatial and temporal scales, by single neurons and by widespread networks. Yet progress in understanding
# how neural populations process information has been limited by a lack of analysis methods capable of
# comparing and merging the different types of information carried by different neural signals, and by the lack of
# realistic computational models of how integration of information can be achieved. Our aim is to develop the
# mathematical analysis and mathematical modeling tools to address these questions.

# Using information theory, we develop new analytical methods that quantify the amount of information available
# in a single trial and for each type of neural signal. At the same time, we determine whether different signals
# carry information about the same or complementary sensory features [1, 2] and how different
# signals influence each other. The unique advantage of these methods is their objectiveness, because they
# do not rely on any assumptions about what is “signal” and what is “noise” in neural responses or on what
# features of the stimulus trigger neural responses.
