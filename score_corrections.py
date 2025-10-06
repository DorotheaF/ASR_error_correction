import json
import random
import string

import jiwer
import pandas as pd
import torch
import os


def generate_corrections(transcript):
    length_transcript = len(transcript)
    print(length_transcript)
    transcript["test_time_response"] = ""
    for i in range(3, length_transcript - 3):
        print(i)
        if not pd.isna(transcript.loc[i, 'ASR']) and str(transcript.loc[i, 'ASR']).strip() != "" and str(
                transcript.loc[i, 'ASR']).strip().lower() != "nan":
            utterance =  "\n<middle> " + transcript.loc[i, 'speaker'] + ": " + transcript.loc[i, 'ASR']  + " </middle>\n"
            pre_context = ((transcript.loc[i - 3, 'speaker'] + ": " + transcript.loc[i - 3, 'ASR'] + " \n" +
                            transcript.loc[i - 2, 'speaker'] + ": " + transcript.loc[i - 2, 'ASR']) + " \n" +
                           transcript.loc[i - 1, 'speaker'] + ": " + transcript.loc[i - 1, 'ASR'])

            post_context = ((transcript.loc[i + 1, 'speaker'] + ": " + transcript.loc[i + 1, 'ASR'] + " \n" +
                             transcript.loc[i + 2, 'speaker'] + ": " + transcript.loc[i + 2, 'ASR']) + " \n" +
                            transcript.loc[i + 3, 'speaker'] + ": " + transcript.loc[i + 3, 'ASR'])

            print(utterance)

            transcript.loc[i, "test_time_response"] = utterance

    return transcript

def calculate_wer(transcript):
    translator = str.maketrans('', '', string.punctuation)

    length_transcript = len(transcript)
    for i in range(3, length_transcript - 3):
        # print(str(i) + "/" + str(length_transcript))
        if not pd.isna(transcript.loc[i, 'ASR']) and str(transcript.loc[i, 'ASR']).strip() != "" and str(transcript.loc[i, 'ASR']).strip().lower() != "nan":
            reference = transcript.loc[i, 'transcript']
            hypothesis = transcript.loc[i, 'corrected_utterance']
            ASR_orig = transcript.loc[i, 'ASR']
            if ":" in hypothesis:
                hypothesis = hypothesis.split(":")[1]

            ref_clean = reference.lower().translate(translator)
            hyp_clean = hypothesis.lower().translate(translator)
            asr_clean = ASR_orig.lower().translate(translator)

            output_asr = jiwer.process_words(ref_clean, asr_clean)
            wer_asr = output_asr.wer

            transcript.loc[i, "ASR_recalc_WER"] = wer_asr

            output = jiwer.process_words(ref_clean, hyp_clean)
            wer = output.wer

            transcript.loc[i, "corrected_WER"] = wer
    return transcript


print("loading")

location = "/mnt/c/Users/Dorot/Emotive Computing Dropbox/Dorothea French/ASR_error_correction/"


transcripts_test = ["48a4fdd4-e68a-77f4-c8d9-35e6235b9199", "75beca5b-c81c-3d10-e998-37035d39761d", "e2e99d2e-845a-028a-e65c-854944a6de7d", "1ee2c43c-8c28-cd1a-b970-0c0cf1a3918a","ee37c120-b375-4526-4721-279330a12d8e","d3a6871c-418d-1347-3895-cfb93458ba9b","ea380e6c-cd18-5965-2876-924bc0081f64","f5263c5d-d20d-edb1-58bc-1039c6290646","f865856f-6845-d71f-7062-d6f5159e3c38","18e87a02-3a52-3ed3-792a-7c935134b2a9",
                    "40b254a6-1971-9e58-3b86-0d15bba60226","a0559b78-8dba-5875-01b0-dd3e9260d178","1c3fee41-c474-e57c-b6ec-261e8ba2261f","3962df1e-39f6-07e0-cfa5-bbac3ac9b3d4","289cff3c-07de-d3f6-a3fb-793ff3b35cd7","cafd96c5-7c5a-2668-4d37-2b149a548216","f94fa678-cff0-61e8-4dce-9f2294cfccb1","dafcae95-d017-934a-6075-9a414c4f7173","1670e2cf-cc9a-cccf-5aff-d89cfa2b4a4a","0394469c-492d-193a-e348-b6b1e230a37f"]




tran_num = 0
for file in transcripts_test:
    print(tran_num)
    tran_num += 1
    transcript = pd.read_excel(location + "data/test_files/" + file + ".xlsx")


    # transcript['ASR'] = transcript['ASR'].astype(str)
    # transcript_test = generate_corrections(transcript)
    # transcript_test.to_excel(location + "data/test_files/" + file + "_testing.xlsx", index=False)



    # transcript['corrected_utterance'] = transcript['test_time_response'].apply(lambda x: x.split("3)")[1].split(":")[1] if str(x).strip().lower() != "nan" and "N/A" not in x.split("3)")[1] else x.split("2)")[0].split(":")[1] if str(x).strip().lower() != "nan" else x)
    # transcript['corrected_utterance'] = transcript['corrected_utterance'].astype(str)
    # transcript['transcript'] = transcript['transcript'].astype(str)
    # transcript_corrected = calculate_wer(transcript)
    # transcript_corrected.to_excel(location + "data/test_files/" + file + "_corrected.xlsx", index=False)
