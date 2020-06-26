# Trajectory splitter and slicer

This is a simple tool for manipulating trajectories from molecular dynamics (MD) simulations. The SLICE-option coarse-grains a trajectory using a larger time-step while the SPLIT-option splits the trajectory into multiple subtrajectories (original time-step). Possibly useful for handling huge trajectory files.

## Usage

```bash
slice_split.py [-h] -i INPUT -n NUM [-sp] [-sl]
```
```NUM``` is the number of frames in each subtrajectory if the SPLIT-flag ```-sp``` is specified. On the other hand, if the SLICE-flag ```-sl``` is given, ```NUM``` is the new stepsize in the coarse-grained trajectory. INPUT supports currently only ```.xyz``` trajectory formats.
