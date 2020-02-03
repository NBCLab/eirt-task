# eirt-task
The Emotion Induction and Regulation Test (EIRT) in E-Prime

## The Task
This is a fast, event-related task that uses negative and neutral images from the International Affective Picture System (IAPS) [1][2] and the Self-Assessment Manikin (SAM) instrument [3] to assess emotion induction and regulation with two different instructions: VIEW (induction; neutral and negative images) and BETTER (regulation, reappraisal; negative images only). There are fifteen neutral and fifteen negative images each, and each trial randomly pairs an image with an appropriate instruction, followed by the valence SAM scale during which they are asked to rate the valence of the image on a scale from 1 (most negative) to 4 (most positive). There are a total of 30 10-second trials per run, interspersed with jittered fixations between each trial ranging from 500ms to 1500ms. Multiple runs can be run from the same EPrime file, due to the randomization. This task is adapted from Blair and colleagues [4], which is similar to that of Ochsner et al. [5][6].

### Accessing the IAPS Stimuli
IAPS images are available [here](https://csea.phhp.ufl.edu/media/iapsmessage.html), subject to the terms of use decided by Bradley and Lang at The Center for the Study of Emotion and Attention. Image filenames referenced in this task match the numbered IAPS images.

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
3. The BIDS events files are also not quite tab-delimited, so you will need to convert them.
Pandas can do this pretty easily.
For example, the following should work:

```python
import pandas as pd

df = pd.read_table('example_data/sub-777_ses-1_task-EIRT_run-1.tsv', sep='\s+')
df.to_csv('example_data/sub-777_ses-1_task-EIRT_run-1.tsv', sep='\t',
          line_terminator='\n', na_rep='n/a', index=False)
```

## References
1. Lang, P.J., Bradley, M.M., & Cuthbert, B.N. (2008). International affective picture System (IAPS): Affective ratings of pictures and instruction manual. Technical Report A-8. University of Florida, Gainesville, FL.
2. Bradley, M. M. & Lang, P. J. (2007). The International Affective Picture System (IAPS) in the study of emotion and attention. In J. A. Coan and J. J. B. Allen (Eds.), <i>Handbook of Emotion Elicitation and Assessment</i> (pp. 29-46). Oxford University Press
3. Bradley, M. M., & Lang, P. J. (1994). Measuring emotion: the self-assessment manikin and the semantic differential. <i>Journal of behavior therapy and experimental psychiatry</i>, 25(1), 49-59.
4. Blair, K. S., Geraci, M., Smith, B. W., Hollon, N., DeVido, J., Otero, M., ... & Pine, D. S. (2012). Reduced dorsal anterior cingulate cortical activity during emotional regulation and top-down attentional control in generalized social phobia, generalized anxiety disorder, and comorbid generalized social phobia/generalized anxiety disorder. <i>Biological psychiatry</i>, 72(6), 476-482.
5. Ochsner, K. N., Bunge, S. A., Gross, J. J., & Gabrieli, J. D. (2002). Rethinking feelings: an FMRI study of the cognitive regulation of emotion. <i>Journal of cognitive neuroscience</i>, 14(8), 1215-1229.
6. Ochsner, K. N., Ray, R. D., Cooper, J. C., Robertson, E. R., Chopra, S., Gabrieli, J. D., & Gross, J. J. (2004). For better or for worse: neural systems supporting the cognitive down-and up-regulation of negative emotion. <i>Neuroimage</i>, 23(2), 483-499.
