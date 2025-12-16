def get_random_subset_of_naturals_up_to_20():
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    import numpy as np
    #set_int = np.random.randint(1, 21)
    #count if the number will be in the subset or not(boolian)
    set_int = np.random.randint(0, 2**20)

    subset = []

    #check i-th bit and append when it's 1
    for i in range(20):
        if (set_int >> i) & 1:
            subset.append(i + 1)

    return np.array(subset)
    pass
    ### Replace with your own code (end)   ###