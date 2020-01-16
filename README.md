# eirt-task
The Emotion Intensity Recognition Test (EIRT) in E-Prime

## Implementation Notes
1. This task is set up to work with FIU's scanner's BioPac.
However, it was developed on a computer that does not have a serial port, which breaks the task if a serial port device is enabled.
As such, there are a number of if/else statements throughout the task to call the serial port when BioPac is enabled and to not call it when it isn't.
This doesn't completely solve the issue, though, so you need to check the devices that are selected under the experiment's main settings before running the task.
If the task will be run on a computer with a serial port, simply turn on the "Serial" device.
Otherwise, make sure it's off.
2. This task writes out a BIDS-compatible tsv file (i.e., an "events" file).
In BIDS events files, the first column should be "onset" (in seconds).
However, E-Prime has an odd behavior where it writes out numeric values with a leading space, so instead we write out a string-based variable as the first column.
Thus, events files written out by this task need to be corrected (i.e., columns need to be reordered to follow BIDS convention) before they will pass the BIDS validator.
