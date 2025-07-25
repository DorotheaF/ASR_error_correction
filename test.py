import ollama

response = ollama.chat(
    model='deepseek-r1:70b',
    messages=[
        {'role': 'user', 'content':
            'I am going to give you a transcript from a classroom. However, the speech recognition system has some errors. '
            'Flag utterances that you think are likely to have errors in the transcription. At the end of the response '
            'repeat the transcript, adding a <flag> token at the beginning of the line before utterances that have an error'
            'tutor: I had to start a new session, so I have to get the lesson uploaded.'
            "tutor: Okay, so we're gonna get started on"
            "tutor: do now, so let's work on that for the next four minutes."
            'tutor: Oh everything alright'
            'tutor: Okay.'
            "tutor: Okay, so I think I'm going to have a start going over so I'm gonna take us to cash for his board"
            'tutor: So, Kashmir, can you explain what you did for number one?'
            'tutor: Okay, so yeah everything you did'
            "tutor: So when you divide by A on the left, we're going to cancel it out, right?"
            'tutor: And then on the right, we can just write it as z plus b over 2.'}
    ]
)

# Print the response
print(response['message']['content'])