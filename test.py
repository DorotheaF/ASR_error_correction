import ollama

response = ollama.chat(
    model='deepseek-r1:70b',
    messages=[
        {'role': 'user', 'content':
            'I am going to give you a transcript from a classroom. However, the speech recognition system has some errors. '
            'The errors you find in normal speech are fine -- such as an incomplete sentence, misconceptions --'
            'however, some of the errors are introduced by the speech recognition system. Identify which utterances '
            "have errors introduced by the transcription what weren't present in the original utterance."
            "At the end of the response print the entire transcript line by line, with a <flag> token at the beginning"
            "of utterances with likely errors. "
            "Transcript: "
            "	tutor	I had to start a new session, so I have to get the lesson uploaded.	\n"
            "	tutor	Okay, so we're gonna get started on	\n"
            "	tutor	do now, so let's work on that for the next four minutes.	\n"
            "	tutor	Oh everything alright	\n"
            "	student-1	Yeah, I'm explaining how to do the instruction one.	\n"
            "	tutor	Okay.	\n"
            "	student-1	Thanks.	\n"
            "	tutor	Okay, so I think I'm going to have a start going over so I'm gonna take us to cash for his board	\n"
            "	tutor	So, Kashmir, can you explain what you did for number one?	\n"
            "	student-1	So since I was like minus B, I added B to both sides.  But since B and Z are like terms and stuff,  I had like wrote it as like Z plus B.	\n"
            "	student-1	I did the vision, so it's like you know,  location but inverse operation.  Like, I didn't know how to like, put the product.  So yeah.	\n"
            "	tutor	Okay, so yeah everything you did	\n"
            "	tutor	So when you divide by A on the left, we're going to cancel it out, right?	\n"
            "	tutor	And then on the right, we can just write it as z plus b over 2.	\n"
            "	tutor	So just like how A and Z and B are not like terms and you can't put them together, so  you just write Z plus B.	\n"
            "	tutor	There's nothing you can simplify here.	\n"
            "	tutor	So you just have z plus b over a.  So that's good.	\n"
            "	tutor	Now, Wisdom, since you were a little stuck on this,  what I wanna show you is that this problem here  is the exact same problem that we had on,  it would have been Wednesday.	\n"
            "	tutor	So we had on Wednesday the problem was 3p minus 5 equals 15	\n"
            "	tutor	So, Lizbeth, how would we do 3P minus 5 equals 15?  And make sure you're on mute.	\n"
            "	student-2	Okay, so, wait.  Need to add, need to add.	\n"
            "	tutor	Right, okay, so yeah.	\n"
            "	tutor	Right, you'd add five to both sides.	\n"

            }
    ]
)

# Print the response
with open("test.txt", 'w') as file:
    file.write(response['message']['content'])

print(response['message']['content'])