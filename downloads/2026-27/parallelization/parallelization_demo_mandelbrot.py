import numpy as np
from mpi4py import MPI
from tqdm import tqdm
import time
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# In this example, we will be parallelizing the calculation of points in the Mandelbrot set, 
# which is defined as points in the complex plane that do not diverge when applying the function
# f(z) = z^2 + c, where c is the complex number corresponding to the point in the plane.

# Since we're using MPI, you need to use a different method than just 'python <script'. Instead, use:
# mpirun -n NUM_CPUS python -m mpi4py <script_name>

def mandelbrot_point(c:complex, max_iter:int) -> int:
    """
    Calculate the number of iterations for a given complex number c to determine if it is in the Mandelbrot set.
    If the point diverges, return the number of iterations it took to diverge. If it does not diverge within max_iter, return max_iter.
    """
    z = 0
    n = 0
    # if the absolute value of z exceeds 2, the point diverges and we can exit early
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_func_serial(c:np.array, max_iter:int) -> np.array:
    """
    Calculate the Mandelbrot set for a given complex number c and maximum iterations.
    This function is implemented in serial.
    """
    points = np.zeros_like(c, dtype=int) # <- we'll use this for coloring the points later

    pbar = tqdm(total=c.shape[0]*c.shape[1], desc="Calculating Mandelbrot set (serial)")
    for ix in range(c.shape[0]):
        for iy in range(c.shape[1]):
            z = 0
            points[ix, iy] = mandelbrot_point(c[ix, iy], max_iter)
            pbar.update(1)
    pbar.close()
    return points

def mandelbrot_func_parallel(c:np.array, max_iter:int, comm:MPI.Comm, rank:int, size:int) -> np.array:
    # YOUR IMPLEMENTATION HERE
    # HINT: Check out the mpi4py docs: https://mpi4py.readthedocs.io/en/stable/tutorial.html
    # also https://www.kth.se/blogs/pdc/2019/08/parallel-programming-in-python-mpi4py-part-1/ 
    # Also, try having each process report when it is done.
    
    # To install mpi4py, check out this link for instructions: https://mpi4py.readthedocs.io/en/stable/install.html#conda-packages

    print(f"This should print {size} times, once for each process.")
    return 0

def plot_mandelbrot(points:np.array, max_iter:int, real_min:float, real_max:float, imag_min:float, imag_max:float):
    """
    Plot the Mandelbrot set using matplotlib.
    """
    cmap = plt.get_cmap("hsv")
    num_colors = min(max_iter, 255)  # Limit the number of colors to 255 for the colormap
    # loop colors based on the number of iterations, and use the colormap to get the color for each point
    colors = np.array([cmap(i % num_colors) for i in range(num_colors)])
    colors[-1] = (0, 0, 0, 1)  # Set the color for points that did not diverge to black
    mandelbrot_cmap = ListedColormap(colors)

    # points is indexed [real, imaginary], but imshow reads axis 0 as rows (vertical)
    # and axis 1 as columns (horizontal), so transpose to put Re on the x axis
    plt.imshow(points.T, cmap=mandelbrot_cmap, vmin=1, extent=(real_min, real_max, imag_min, imag_max), origin='lower')
    plt.colorbar()
    plt.title(f'Mandelbrot Set (max_iter={max_iter})')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

if __name__ == "__main__":

    comm = MPI.COMM_WORLD # <- This is the communicator object that processes are organized thru
    size = comm.Get_size() # <- This is the total number of processes or "ranks" available
    rank = comm.Get_rank() # <- This is the specific rank id, which is different for every process
    # After this point, each line runs on EVERY RANK

    # Define the complex plane
    real_min, real_max = -2, 1
    imag_min, imag_max = -1.5, 1.5
    max_iter = 100
    x = np.linspace(real_min, real_max, 1000)
    y = np.linspace(imag_min, imag_max, 1000)
    # c is a 2D array of complex numbers, so [real, imaginary]
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    # Serial calculation
    if rank == 0:
        t1 = time.time()
        n_serial = mandelbrot_func_serial(c, max_iter)
        t_serial = time.time() - t1
    else: # <- every other rank will run this code instead
        n_serial = None
        t_serial = 0.0

    # using MPI means we need to be more explicit on sharing data, and synchronizing processes. 
    comm.Barrier() # <- This is a synchronization point, so all ranks wait until everyone is done with the serial calculation
    t_serial = comm.bcast(t_serial, root=0) # <- This broadcasts the serial time to all ranks

    # Parallel calculation
    t1 = time.time()
    n_parallel = mandelbrot_func_parallel(c, max_iter, comm, rank, size)
    t_parallel = time.time() - t1

    # plotting is wierd on multiple-ranks, so only run this on rank 0
    if rank == 0:
        print(f"Time taken (serial): {t_serial:.2f} seconds")
        print(f"Time taken (parallel): {t_parallel:.2f} seconds ({t_serial/t_parallel:.2f}x faster)")
        plot_mandelbrot(n_serial, max_iter, real_min, real_max, imag_min, imag_max)

    # BONUS ACTIVITIES

    # 1 - This calculation gets slower for points close to the boundary of the fractal.
    #     Try repeating this calculation for a smalelr region of the complex plane to see how the time taken changes.
    # 2 - I purposely avoided using numpy vectorization in this example, but you can feasably get
    #     a speedup by using numpy vectorization instead of for loops. Try to implement this and see how much faster it is.
    # 3 - Math nerds may be aware there are many ways to optimize this calculation. Go ahead and try to impliment some of them!