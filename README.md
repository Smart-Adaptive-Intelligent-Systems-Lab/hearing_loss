EEG data: https://zenodo.org/record/3618205#.Yw0CnezMLnm

Use Google Shared Drive's ds shneel zipped folder for work in MATLAB's EEGLAB

Terminology:
- HI - Hearing Impaired
- NI - Not Impaired
- Scroll Map - shows the lines from EEGs in each channel
- Spectra Map - plots topopgraphical maps of the data at specific Hz.

Folders/Files:
- 6.10.22Hz Folder :      Holds .jpegs of spectra maps for 6, 10 and 22Hz along with their .csv for each subject
- AllHz Folder :          Holds .jpegs of spectra maps for 2 to 25Hz along with their .csvs for each subject
- old Folder :            Holdes the Holds .jpegs of spectra maps for 6, 10 and 22Hz along with their .csv that are averaged between HI and NI subjects
- boundaries.jpeg :       .jpeg for the boundaries after finding them
- boundaries.csv :        .csv for the boundaries after finding them and converting
- allSub_evenHz_1:        result from getPercentages.py for all subjects but only even numbered Hz. _1 means each row is one subject_hz ; and the boundaries are features
- allSub_evenHz_2:        result from getPercentages.py for all subjects but only even numbered Hz. _2 means each row is one subject; and the Hz and boundaries are features
- allSub_6.10.22Hz_1:     result from getPercentages.py for all subjects but only 6,10,22 Hz. _1 means each row is one subject_hz ; and the boundaries are features
- allSub_6.10.22Hz_2:     result from getPercentages.py for all subjects but only 6,10,22 Hz. _2 means each row is one subject and the Hz and boundaries are features
- avged_6.10.22:          result from getPercentages.py for HI and NI averaged on 6, 10, and 22 Hz
- dataset2To25:           result from getPercentages.py for all subjects with 2Hz to 25 Hz. means each row is one subject_hz ; and the boundaries are features


Scripts:
1. jpeg2csv.py :        turns .jpeg or .jpg files into a .csv file where each cell is a pixel's color in RBG format
2. getBoundaries.py:    grabs the .csv file of the boundaries (boundaries.csv from boundaries.jpeg), finds the pixels that are within boundary 1-4
                        1: Lower and outer-most boundary
                        2: Middle donut
                        3: Most innner circle
                        4: Upper and outer-most boundary
3. getPercentages.py :  gets the percentages of red, green, blue in each boundary and puts them into a .csv file
4. binary_class.ipynb:  different methodologies that were coded
                        a. randomForestClassifier
                        b. KNN
                        c. next task (recurent neural network)
5. binary_class2.ipynb: same as above but used for a different format of the .csv
6. matrix.py :          testing old ideas (could be deleted)


Using MATLAB's EEGLAB:
To learn more : https://eeglab.org/tutorials/
1. Open eeglab from MATLAB
2. Open BIOSIG file from one of the subject's tone_stimuli
3. Reference Channel: 48 to get Cz (which is the middle of the head). Everything else was defaulted.
4. Edit > Location Channels > use default to map channels
5. Use Plot Tab to plot information
    a. Scroll shows the lines from EEGs in each channel
    b. Spectra Map plots topopgraphical maps of the data at specific Hz.
6. File > export as EDF (easier to use in my opinion) or BDF

Methodology:
- Get Boundaries
    - Get Spectra map of 6, 10, and 22 Hz of each subject
    - For HI subjects, overlap the images and/or average the rgb colors in each cell to find the average spectra map (I accidentally deleted)
    - Do the same for NI subjects. (I accidentally deleted)
    - Average the HI and NI averaged spectra map
    - Create boundaries using contrasting colors depending on the averaged spectra map
    - Results: boundaries.jpeg and boundaries.csv
- Get 100x100 (on mac) .jpeg files
    - Cut the BDF file to 5 seconds where at least two events are being viewed
    - Save the .set in the /cut folder
    - Add channel locations to see the spectra maps
    - Adjust which Hz needed and plot
    - Results: all .jpeg files in 6.10.22Hz and AllHz folder
- Run them through the getPercentage and binary_class code (may take about 5 hours)
    - Results: .csv of the percentages and accuracy/recall/precision after RFC and KNN
