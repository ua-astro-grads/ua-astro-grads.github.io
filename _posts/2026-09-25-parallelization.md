---
author: "Joe Adamo"
title: "Parallelization with Python"
---

Joe showed how to speed up Python code by spreading work across multiple CPU cores.

[Slides](https://docs.google.com/presentation/d/1Ewddr-YO_0uWf0oUuSP0uOD8hM2vVJLaHllqBwTaLac/edit?usp=share_link) (Google Slides)

## Why parallelize?

Single-core CPU speeds have plateaued, so modern CPUs ship with more and more cores. Most Python code runs one instruction at a time. Parallelizing splits the work into processes that run at the same time.

## Three ways to do it

- **NumPy** (and SciPy, PyTorch, scikit-learn, etc.) already multithreads many operations in compiled code. It's the easiest option but gives you the least control.
- **`multiprocessing`** is in the standard library. It sidesteps the Global Interpreter Lock (GIL) by spawning separate Python processes, at the cost of some startup overhead. Scripts run like normal Python, but on HPC they're limited to a single node.
- **MPI via `mpi4py`** is the standard used by heavy simulation codes and samplers (implementations include OpenMPI and MPICH). It gives you the most control and is the hardest to use. Scripts run on every rank at once and are launched with:

```
mpirun -n <N> python -m mpi4py <myscript.py>
```

## Activity

1. Estimate π by Monte Carlo integration using `multiprocessing.Pool`: [exercise](/downloads/2026-27/parallelization/parallelization_demo_pi.py), [solution](/downloads/2026-27/parallelization/parallelization_demo_pi_solved.py)
2. Compute the Mandelbrot set with `mpi4py`: [exercise](/downloads/2026-27/parallelization/parallelization_demo_mandelbrot.py), [solution](/downloads/2026-27/parallelization/parallelization_demo_mandelbrot_solved.py)

Useful references: [`Pool.map` tutorial](https://superfastpython.com/multiprocessing-pool-map/), [`multiprocessing` docs](https://docs.python.org/3/library/multiprocessing.html), [mpi4py tutorial](https://mpi4py.readthedocs.io/en/stable/tutorial.html), [mpi4py install](https://mpi4py.readthedocs.io/en/stable/install.html#conda-packages).
