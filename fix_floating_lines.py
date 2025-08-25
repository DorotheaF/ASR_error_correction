import glob
import shutil

import pandas as pd


def cycle_through_transcripts(location):
    print(location)
    transcripts = glob.glob(location + "*.xlsx")
    i = 0
    for file in transcripts:
        transcript = pd.read_excel(file)
        if "okay three over three that's once plus three over three" in transcript['ASR'].values:
            print(file)



location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/transcripts/"

cycle_through_transcripts(location)
