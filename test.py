import ollama

response = ollama.chat(
    model='deepseek-r1:70b',
    messages=[
        {'role': 'user', 'content':
            'I am going to give you a transcript from a classroom. However, the speech recognition system has some errors. '
            'The errors you find in normal speech are fine -- such as an incomplete sentence or misconceptions --'
            'however, some of the errors are introduced by the speech recognition system. Identify which utterances '
            "have errors introduced by the transcription what weren't present in the original utterance."
            "At the end of the response print the entire transcript line by line, with a <flag> token at the beginning"
            "of utterances with likely errors. "
            "Transcript: "
            "	tutor	I had to start a new session, so I have to get the lesson uploaded.	"
            "	tutor	Okay, so we're gonna get started on	"
            "	tutor	do now, so let's work on that for the next four minutes.	"
            "	tutor	Oh everything alright	"
            "	student-1	Yeah, I'm explaining how to do the instruction one.	"
            "	tutor	Okay.	"
            "	student-1	Thanks.	"
            "	tutor	Okay, so I think I'm going to have a start going over so I'm gonna take us to cash for his board	"
            "	tutor	So, Kashmir, can you explain what you did for number one?	"
            "	student-1	So since I was like minus B, I added B to both sides.  But since B and Z are like terms and stuff,  I had like wrote it as like Z plus B.	"
            "	student-1	I did the vision, so it's like you know,  location but inverse operation.  Like, I didn't know how to like, put the product.  So yeah.	"
            "	tutor	Okay, so yeah everything you did	"
            "	tutor	So when you divide by A on the left, we're going to cancel it out, right?	"
            "	tutor	And then on the right, we can just write it as z plus b over 2.	"
            "	tutor	So just like how A and Z and B are not like terms and you can't put them together, so  you just write Z plus B.	"
            "	tutor	There's nothing you can simplify here.	"
            "	tutor	So you just have z plus b over a.  So that's good.	"
            "	tutor	Now, Wisdom, since you were a little stuck on this,  what I wanna show you is that this problem here  is the exact same problem that we had on,  it would have been Wednesday.	"
            "	tutor	So we had on Wednesday the problem was 3p minus 5 equals 15	"
            "	tutor	So, Lizbeth, how would we do 3P minus 5 equals 15?  And make sure you're on mute.	"
            "	student-2	Okay, so, wait.  Need to add, need to add.	"
            "	tutor	Right, okay, so yeah.	"
            "	tutor	Right, you'd add five to both sides.	"
            }
    ]
)

# Print the response
print(response['message']['content'])