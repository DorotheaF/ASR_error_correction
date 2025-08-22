import numpy as np
import pandas as pd
import itertools

def remerge_student_utterances(transcript):
    transcript["Turn"] = transcript["Turn"].astype(int)
    # transcript.set_index('Turn', inplace=True)
    # print(transcript.columns)
    student_frame = transcript[transcript['Student Human Transcript'] != None]
    transcript['speaker'] = "tutor"
    transcript = transcript[["Turn", "speaker", "Tutor Human Transcript", "Tutor Whisper-Large-v2 Transcript", "True Label",
                             "Predicted Label - Human Transcripts", "Predicted Label - Whisper Transcripts",
                             "Tutor ASR confidence", "Tutor ASR WER", "Ethnicity", "Race Description",
                             "Personal Pronouns"]]
    transcript.rename(columns={"Tutor Human Transcript": 'transcript', 'Tutor Whisper-Large-v2 Transcript': 'ASR', "Tutor ASR confidence": "confidence", "Tutor ASR WER": "WER"}, inplace=True)


    #
    # student_frame['speaker'] = "1_student"
    # student_frame = student_frame[
    #     ["Turn", "speaker", "Student Human Transcript", "Student Whisper-Large-v2 Transcript", "Student ASR confidence", "Student ASR WER",
    #      "Ethnicity", "Race Description", "Personal Pronouns"]]
    # student_frame.rename(columns={"Student Human Transcript": 'transcript', 'Student Whisper-Large-v2 Transcript': 'ASR',
    #                            "Student ASR confidence": "confidence", "Student ASR WER": "WER"}, inplace=True)
    #
    # merged = pd.concat([transcript, student_frame], ignore_index=True)
    # merged = merged.dropna(subset=["transcript"]).sort_values(["Turn", "speaker"]).reset_index(drop=True)
    # merged["speaker"] = merged["speaker"].apply(lambda x: x.split("_")[1])

    return transcript # merged


file = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/raw/Saga_CPS_DroppedDuplicatedSSES_with_TalkMoves.xlsx"

all_transcripts = pd.read_excel(file)

# print(all_transcripts.columns)

all_transcripts = all_transcripts[["Turn", "recordingID", "Student Human Transcript", "Tutor Human Transcript", "Student Whisper-Large-v2 Transcript", "Tutor Whisper-Large-v2 Transcript", "True Label", "Predicted Label - Human Transcripts", "Predicted Label - Whisper Transcripts", "Tutor ASR confidence", "Tutor ASR WER", "Student ASR confidence", "Student ASR WER", "Ethnicity", "Race Description", "Personal Pronouns"]]

transcript_groups = all_transcripts.groupby("recordingID")

pd.options.display.max_colwidth = 200

for ID, group in transcript_groups:
    # print(group["speaker"].head(10).values + ": " + group["ASR"].head(10).values)
    fixed_transcript = remerge_student_utterances(group.copy())
    fixed_transcript.to_excel("/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/with_talkmoves/"+ ID +".xlsx")




