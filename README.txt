
## Disk&Ram Operations

Both scripts uses RAM & Disk reading/writing operations with a small optimization regarding buffer clearence, although buffer things can be still optimized,
the script succesfully reads the contents of SampleMemoryWriting.txt as a fixed value within the code and simply prints the time.

## FPS
Script to diagnose GPU and CPU relevant metrics.
Provides with simple depuration information such as test duration, last frame,
total frames in test, total average fps count, average frame time in ms.

It also records that information, 'frame steps' and 'differences per frame' in FPS.txt, which creates.

As it's open sourced, that can be altered around line 62 to add variables you'd like to record.
Duration in line 9 it's also recommended to alter to adjust test duration.
