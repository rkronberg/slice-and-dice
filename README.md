# Trajectory splitter and slicer

This is a simple tool for manipulating trajectories from molecular dynamics (MD) simulations. The trajectory can be either split into chunks (original timestep) or coarse-grained using a larger timestep. Possibly useful for handling huge trajectory files.

## Usage

```bash
$ python slice_split.py [-h] -i INPUT (-n NFRAMES | -ts STEP) (-r REGEX | -fs FSIZE) [-f FIRST] [-l LAST]
```

```INPUT``` supports currently only ```.xyz``` trajectory formats. ```NFRAMES``` is the number of frames in each subtrajectory if splitting trajectory into chunks. If the trajectory is coarse-grained, the flag  ```-ts``` is used to provide the new timestep of the sliced trajectory. ```REGEX``` is an expression in the input that repeats regularly every frame and is required to determine the number of lines per frame. If not given/found, the frame size needs to be specified using the ```-fs``` flag. The optional ```-f``` and ```-l``` flags expect the first and last frames to be included, respectively. If unspecified, the full trajectory is considered.
