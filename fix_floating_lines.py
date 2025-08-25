import glob
import shutil

import pandas as pd


def cycle_through_transcripts(location):
    print(location)
    transcripts = glob.glob(location + "*.xlsx")
    i = 0
    for file in transcripts:
        transcript = pd.read_excel(file)
        if 'Unnamed: 0.1' in transcript.columns:
            i += 1
            shutil.move(file, file.replace("reasoning_generated/", "reasoning_generated/failed/"))
    print(i)



location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/reasoning_generated/"

cycle_through_transcripts(location)
