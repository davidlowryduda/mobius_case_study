
# Helper Scripts #

This directory contains helper scripts for datafile generation. This includes
both scripts for making true datafiles and scripts for making corrupted
datafiles.

The datafile generation recipe is automatically called by other parts of the
code, but can be individually called via

    make good_data
    make shuffle

The logic behind these scripts is straightforward. Each datafile consists of
lines of the form `INPUT\tOUTPUT`, where `INPUT` and `OUTPUT` are in Int2Int
formatting. The files here have length $200$ vectors of inputs and a single
integer output.
