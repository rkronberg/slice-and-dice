# Trajectory splitter and splicer

This is a tool for manipulating trajectories from molecular dynamics (MD) simulations. The SLICE-option coarse-grains a trajectory using a larger time-step while the SPLIT-option splits the trajectory into multiple subtrajectories with the original time-step.

## Usage

```bash
slice_split.py [-h] -i INPUT -n NUM [-sp] [-sl]
```

Supports currently only ```.xyz``` trajectory formats.
