import glob

import pandas as pd


def cycle_through_transcripts_add_talkmoves(add_location, talkmoves_location):
    print(add_location)
    transcripts = glob.glob(add_location + "*.xlsx")
    transcripts_talkmoves = glob.glob(talkmoves_location + "*.xlsx")
    transcripts_just_names = [x.rsplit("/",1)[1].split("_generated_reasoning.xlsx")[0] for x in transcripts]

    for file in transcripts_talkmoves:
        file_name = file.rsplit("/",1)[1].split(".xlsx")[0]
        if file_name in transcripts_just_names:
            transcript = pd.read_excel(add_location + file_name + "_generated_reasoning.xlsx")
            if 'True Label' not in transcript.columns.values:
                print("adding")
                talkmove_transcript = pd.read_excel(file)
                # print(talkmove_transcript.columns)

                print(len(talkmove_transcript))
                print(len(transcript[transcript["speaker"]=="tutor"]))
                transcript = pd.merge(transcript, talkmove_transcript[['ASR',"True Label",
                                 "Predicted Label - Human Transcripts", "Predicted Label - Whisper Transcripts"]], on='ASR', how='left')
                transcript.to_excel(add_location + file_name + "_generated_reasoning.xlsx")
            else:
                print("aleady there")

        else:
            print("not needed")



talkmoves_location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/with_talkmoves/"
add_location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/data/reasoning_generated/"

cycle_through_transcripts_add_talkmoves(add_location, talkmoves_location)


