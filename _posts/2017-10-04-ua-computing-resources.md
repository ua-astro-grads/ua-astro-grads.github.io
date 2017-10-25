---
author: "Rachel Smullen and Rixin Li"
title: "UA High Performance Computing Resources"
---

This presentation covers the high-performance computing resources available at the University of Arizona. The presentation materials are on Rachel Smullen's GitHub at https://github.com/rsmullen/UAHPC 

For posterity, they're mirrored here below:

[Slides (PDF)](/downloads/2017-18/smullen-li-hpc-slides.pdf)

## UA HPC Commands

The online documentation can be found [here](https://docs.hpc.arizona.edu/) and is a good place to start if you have questions.

### Logging in

To log in to the HPC system, from a campus network or the campus VPN, type

```
ssh -Y username@hpc.arizona.edu
```

You should come to the login node, called keymaster.  You'll see options to log in to either El Gato or Ocelote.  Typing `elgato` or `ocelote` will _not_ allow windows.  You need to use `ssh -Y elgato`.

To see what storage disks you have access to, use the command `uquota`.

### Loading software

Your profile on the login nodes for the supercomputers don't come with any pre-loaded software.  To see available packages, type `module avail`. Then, to load a specific package, type `module load modulename`.

For instance, `module load python/3.4.1`. To see what you have loaded, type `module list`. (If you don't want to do this every time, you can add these commands to your `.bashrc` file.)

### Interacting with the scheduler

Ocelote uses a scheduler called PBS, while El Gato uses the LSF scheduler.  The commands are similar, but different enough to be a pain.

#### El Gato

  * To see a list of available queues, type `bqueues`.
  * To see your running jobs, type `bjobs`.
  * To see everyone's jobs, use `bjobs -u all`.

#### Ocelote

  * To see a list of available queues, `qstat -q`.
  * To see all of your running jobs, type `qstat -u username`.
  * To see everyone's jobs, use `qstat`.

## Running Jobs

### Embarassingly Parallel Jobs

These are jobs where you want to execute the same command several times.

#### El Gato

Here is an example of an El Gato lsf script for an embarassingly parallel job.  Save this in a file named something like `lsf.sh`.

```
#!/bin/bash
#BSUB -n 1                         ## number of processors given to each process
#BSUB -e err_somename_%I           ## error files; make somename unique to other runs
#BSUB -o out_somename_%I           ## output notification files
#BSUB -q "your queue"              ## can be windfall, standard, or medium, depending on your advisor's allowed queues.
#BSUB -u username
#BSUB -J somename[start-finish]    ## Give the job a name (somename) and then fill in the processes you want, eg [1-100] or [1,2,3]
#BSUB -R "span[ptile=1]"
####BSUB -w "done(JobID|JobName)"  ## Ask us about this fanciness

#.${LSB_JOBINDEX} gives the run index 1,2,3...

# use regular linux commands to copy/link executables, input files, etc., run python, or whatever else you want to do.  It will run in the subdirectory some_directory/some_runname${LSB_JOBINDEX}/. 

mkdir some_directory
mkdir some_directory/some_runname${LSB_JOBINDEX}
cd some_directory/some_runname${LSB_JOBINDEX}/
echo "I'm Job number ${LSB_JOBINDEX}"
```

To execute this script, use `bsub < lsf.sh`. You can then check your job's status with `bjobs`.

#### Ocelote

Here's the same for Ocelote.  The PBS scheduler is different in that you submit a job array.  Save this script as something like `pbs.sh`.

```
## choose windfall or standard
#PBS -q queuename
## select nodes:cpus per node:memory per node
#PBS -l select=1:ncpus=1:mem=6gb
## the name of your job
#PBS -N jobname
## the name of your group, typically your advisor's username
#PBS -W group_list=yourgroup
## how the scheduler fills in your nodes
#PBS -l place=pack:shared
## the length of time for your job
#PBS -l walltime=1:00:00
## the indexes of your job array
#PBS -J 1-5
## the location for your error files; this must exist first
#PBS -e errorfiles/
## the location for your output files; this must exist first
#PBS -o outfiles/

# Now you can use your normal linux commands

# Run the program for individual core ${PBS_ARRAY_INDEX}
echo  "I'm Job number ${PBS_ARRAY_INDEX}"
```

You can submit your job with `qsub pbs.sh` and then you can check your job with `qstat -u yourname -t`.

### Parallel Jobs

We can also run parallel jobs on a supercomputer. (After all, that's what they were designed for!)

#### El Gato

Here's an example MPI script.  Save it in `lsf.sh`.  You can get the code in Rixin's directory at `/home/u5/rixin/mpi_hello_world`.

```
###========================================
#!/bin/bash
# set the job name
#BSUB -J mpi_test
# set the number of cores in total
#BSUB -n 32
# request 16 cores per node
#BSUB -R "span[ptile=16]"
# request standard output (stdout) to file lsf.out
#BSUB -o lsf.out
# request error output (stderr) to file lsf.err
#BSUB -e lsf.err
# set the queue for this job as windfall
#BSUB -q "medium"
#---------------------------------------------------------------------

### load modules needed
module load openmpi

### pre-execution work
cd ~/mpi_hello_world
make # compile the code, in this example case

### set directory for job execution
cd ./elgato_sample_run
### run your program
mpirun -np 32 ../mpi_hello_world > elgato_sample_output.txt
### end of script
```

Use the same commands to submit and check the status as before.

#### Ocelote

And the same for Ocelote

```
#!/bin/bash
##set the job name
#PBS -N mpi_test
##set the PI group for this job
#PBS -W group_list=kkratter
##set the queue for this job as windfall
#PBS -q windfall
##request email when job begins and ends
#PBS -m bea
##set the number of nodes, cores, and memory that will be used
#PBS -l select=2:ncpus=28:mem=1gb
##specify "wallclock time" required for this job, hhh:mm:ss
#PBS -l walltime=00:01:00
##specify cpu time = walltime * num_cpus
#PBS -l cput=1:00:00

###load modules needed
module load openmpi/gcc/2

###pre-execution work
cd ~/mpi_hello_world
make # compile the code, in this example case

###set directory for job execution
cd ./ocelote_sample_run
###run your executable program with begin and end date and time output
date
/usr/bin/time mpirun -np 56 ../mpi_hello_world > ocelote_sample_output.txt
date
```

## Killing jobs

If you realize you made a mistake, or you want to kill a job that has been running for too long, use `bkill jobid` on El Gato or `qdel jobid[].head1` on Ocelote.

### Interactive Nodes

Do not, I repeat, DO NOT run programs on the login node.  You're using up resources for people that just want to check their job status!  Instead, you can request an interactive node that lets you run programs from a compute node where you can use as much of the resources as you want.

To get an interactive node, you submit a job to the scheduler requesting interactive resources.  On El Gato, use `bsub -XF -Is bash` and on Ocelote, use `qsub -I -N jobname -W group_list=groupname -q yourqueue -l select=1:ncpus=28:mem=168gb -l cput=1:0:0 -l walltime=1:0:0`.
