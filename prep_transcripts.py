import pandas as pd

file = "C:\\Users\\Dorot\\Emotive Computing Dropbox\\Dorothea French\\ASR_error_correction\\data\\FINAL LoFi WITH SCORES NO MATCHING -LoFi_With_Propensity_Scores_4_11.xlsx"

all_transcripts = pd.read_excel(file)

print(all_transcripts.columns)

all_transcripts = all_transcripts[["utterance_in_recording", "recordingID", "speaker", "transcript", "ASR", "confidence", "Ethnicity", "Race Description", "Gender"]]

transcript_groups = all_transcripts.groupby("recordingID")

pd.options.display.max_colwidth = 200

for ID, group in transcript_groups:
    print(group["speaker"].head(10) + ": " + group["ASR"].head(10))
    # group.to_excel("C:\\Users\\Dorot\\Emotive Computing Dropbox\\Dorothea French\\ASR_error_correction\\data\\transcripts\\"+ ID +".xlsx")