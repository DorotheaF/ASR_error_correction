import pandas as pd

file = "C:\\Users\\Dorot\\Emotive Computing Dropbox\\Dorothea French\\ASR_error_correction\\data\\LoFi+whisper-large-v2_utterances_demog.xlsx"

all_transcripts = pd.read_excel(file)

print(all_transcripts.columns)

all_transcripts = all_transcripts[["utterance_in_recording", "recordingID", "speaker", "transcript", "ASR", "confidence", "Ethnicity", "Race Description", "Personal Pronouns"]]

transcript_groups = all_transcripts.groupby("recordingID")

pd.options.display.max_colwidth = 200

for ID, group in transcript_groups:
    print(group["speaker"].head(10).values + ": " + group["ASR"].head(10).values)
    # group.to_excel("C:\\Users\\Dorot\\Emotive Computing Dropbox\\Dorothea French\\ASR_error_correction\\data\\transcripts\\"+ ID +".xlsx")