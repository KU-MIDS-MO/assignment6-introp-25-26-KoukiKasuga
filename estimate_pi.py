def estimate_pi(num_samples):
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###

    #montecarlo method
    import numpy as np
    inside_circle = 0

    for i in range(num_samples):
        x, y = np.random.rand(2)

        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimated = 4* inside_circle/num_samples

    return pi_estimated
    pass
    ### Replace with your own code (end)   ###