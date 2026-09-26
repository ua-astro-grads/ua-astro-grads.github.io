import numpy as np
import time
import multiprocessing as mp

# We're going to start by calculating pi via Monte-Carlo integration
# The idea is to randomly sample points in a square that bounds a quarter circle,
# and determine the ratio of points that fall inside the quarter circle to the total number of points sampled. 
# This ratio can then be used to estimate the value of pi.

# I've defined a function that performs this integration in serial.
# your job is to use multiprocessing.Pool to run this same calculation in parallel.

def monte_carlo_pi_serial(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x, y = np.random.rand(2)  # Generate random point (x, y)
        if x**2 + y**2 <= 1:  # Check if the point is inside the quarter circle
            inside_circle += 1
    return (inside_circle / num_samples) * 4  # Estimate pi

# My solution introduces a worker function that is acutally called by pool.map
# From the function's perspective, num_worker_samples is an integer
def monte_carlo_worker(num_worker_samples):
    inside_circle_partial = 0
    for _ in range(num_worker_samples):
        x, y = np.random.rand(2)  # Generate random point (x, y)
        if x**2 + y**2 <= 1:  # Check if the point is inside the quarter circle
            inside_circle_partial += 1
    return inside_circle_partial

def monte_carlo_pi_parallel(num_samples, num_processes):

    # I'm splitting the total number of samples evenly across num_processes
    num_worker_samples = [int(num_samples / num_processes)] * num_processes

    # Set up the multiprocessing pool with the specified number of processes 
    # using "with" means we don't have to manually close / join the pool
    with mp.Pool(processes=num_processes) as pool:

        # In the below line, num_worker_samples is a list of integers, and pool.map will call monte_carlo_worker for each integer in the list.
        # I set it up so the list has the same length as the number of processes, but that isn't strictly necesary.
        inside_circle_partial = pool.map(monte_carlo_worker, num_worker_samples)

    # The returned inside_circle_partial is a list of sub-counts, so sum them all up and estimate pi
    pi = (np.sum(inside_circle_partial) / num_samples) * 4
    return pi


def main():
    num_samples = 10**7  # Total number of samples to use for the estimation
    num_processes = mp.cpu_count()  # Use the number of available CPU cores

    pi_actual = np.pi

    # Serial calculation
    t1 = time.time()
    pi_serial = monte_carlo_pi_serial(num_samples)
    t_serial = time.time() - t1
    print(f"Estimated value of pi (serial): {pi_serial}")
    print(f"Off by: {abs(pi_serial - pi_actual):.3e}")
    print(f"Time taken (serial): {t_serial:.2f} seconds")

    #Parallel calculation
    t1 = time.time()
    pi_parallel = monte_carlo_pi_parallel(num_samples, num_processes)
    t_parallel = time.time() - t1
    print(f"\nEstimated value of pi (parallel, {num_processes} processers): {pi_parallel}")
    print(f"Off by: {abs(pi_parallel - pi_actual):.3e}")
    print(f"Time taken (parallel): {t_parallel:.2f} seconds ({t_serial/t_parallel:.2f}x faster)")

    ## BONUS ACTIVITIES

    # 1. Profile how much your implimentation speeds up the calculation of pi as you increase the number of sampled points.
    # 2. You might find that the speedup you get is smaller than you expected. Why might that be the case?
    # 3. There are many other ways you can parallelize this code. For exxample:
    #   - You can use shared memory to avoid having to pass data back and forth between processes.
    #   - You can use something besides Pool.map, such as Pool.apply_async or Pool.starmap, to have more control over how the work is distributed.


if __name__ == "__main__":
    main()