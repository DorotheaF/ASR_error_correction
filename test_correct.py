import ollama

response = ollama.chat(
    model='deepseek-r1:70b',
    messages=[
        {'role': 'user', 'content':
            'I am going to give you a transcript from a classroom. However, the speech recognition system has some errors. '
            'The errors you find in normal speech are fine -- such as an incomplete sentence, misconceptions --'
            'however, some of the errors are introduced by the speech recognition system. Identify which utterances '
            "have errors introduced by the transcription what weren't present in the original utterance."
            "Identify which utterances have errors, then correct the errors as in the following example:"
            "<Example transcript>"
"   Speaker	ASR utterance	Corrected Utterance	\n"
"	tutor	I had to start a new session, so I have to get the lesson uploaded.	I had to start a new session, so I have to get the lesson uploaded.	\n"
"	tutor	Okay, so we're gonna get started on	Okay, so we're going to get started on do now.	\n"
"	tutor	do now, so let's work on that for the next four minutes.	So let's work on that for the next four minutes.	\n"
"	student-1		It just...	\n"
"	tutor	Oh everything alright	Everything all right?	\n"
"	student-1	Yeah, I'm explaining how to do the instruction one.	Yeah, I'm explaining how to do the fraction one.	\n"
"	tutor	Okay.	Okay,	\n"
"	student-1	Thanks.	There's b.	\n"
"	tutor	Okay, so I think I'm going to have a start going over so I'm gonna take us to cash for his board	so I think I'm going to have us start going over, so I'm going to take us to Cashmere's board.	\n"
"	tutor	So, Kashmir, can you explain what you did for number one?	So, Cashmere, can you explain what you did for number one?	\n"
"	student-1		I did inverse operation.	\n"
"	student-1	So since I was like minus B, I added B to both sides.  But since B and Z are like terms and stuff,  I had like wrote it as like Z plus B.	Sometimes it was like minus B, I added B to both sides, but since B and Z are like terms and stuff, I had wrote it as like, Z plus B.	\n"
"	student-1	I did the vision, so it's like you know,  location but inverse operation.  Like, I didn't know how to like, put the product.  So yeah.	I did the vision [inaudible 00:04:55] operation, but I didn't know how to [inaudible 00:04:57]	\n"
"	tutor	Okay, so yeah everything you did	Okay, so yeah, everything you did was good.	\n"
"	tutor	So when you divide by A on the left, we're going to cancel it out, right?	So when you divide by A on the left, we're going to cancel it out, right?	\n"
"	tutor	And then on the right, we can just write it as z plus b over 2.	And then on the right, we can just write it as Z plus B over A.	\n"
"	tutor	So just like how A and Z and B are not like terms and you can't put them together, so  you just write Z plus B.	So just like how A and Z and B are not like terms and you can't put them together, so you just write Z plus B.	\n"
"	tutor	There's nothing you can simplify here.	There's nothing that you can simplify here.	\n"
"	tutor	So you just have z plus b over a.  So that's good.	So you just have Z plus B over A, So that's good.	\n"
"	tutor	Now, Wisdom, since you were a little stuck on this,  what I wanna show you is that this problem here  is the exact same problem that we had on,  it would have been Wednesday.	Now, Isabel, since you were a little stuck on this, what I want to show you is that this problem here is the exact same problem that we had on it would have been Wednesday.	\n"
"	tutor	So we had on Wednesday the problem was 3p minus 5 equals 15	So we had On Wednesday, the problem was three P minus five equals 15.	\n"
"	tutor	So, Lizbeth, how would we do 3P minus 5 equals 15?  And make sure you're on mute.	So Isabel, how would we do three P minus five equals 15 and make sure you're unmuted.	\n"
"	student-2	Okay, so, wait.  Need to add, need to add.	So it's like, we add [inaudible]	\n"
"	tutor	Right, okay, so yeah.	Right, Okay, so yeah.	\n"
"	tutor	Right, you'd add five to both sides.	Right, You'd add five to both sides.	\n"
"	student-2		Okay.	\n"
"	tutor	It's okay, so we identified both sides	It's okay, So we add five to both sides, right?	\n"
"	tutor	And then when we get on the right.	And then what do we get on the right?	\n"
"	student-2	But we wait on the right.	Wait, on the right?	\n"
"	tutor	Yeah. So what's 15 plus 5?	Yeah, so what's 15 plus 5?	\n"
"	student-2	It's funny.	20?	\n"
"	tutor	20.  Mm-hmm.  Okay.	20, Good.	\n"
"	tutor	And we have 3P equals 20 and then what do we do as well?	And we have three P equals 20 and then what do we do Isabel?	\n"
"	tutor	Is everything okay?	Is everything okay?	\n"
"	student-2	Thank you.	Yeah.	\n"
"	tutor	Okay, so what do we do next?	Okay, So what do we do next?	\n"
"	student-2	We're missing, we're missing 20.	We everything 20.	\n"
"	tutor	Right, we get 20 and then...  ...the left side of the screen.  Okay, what's so funny?	Right, we get 20 and then okay, what's so funny?	\n"
"	student-2	Okay that was weird.  Ok so none of the somebody just-	Okay. So... somebody just Yeah.	\n"
"	student-2	Thank you, Wendy.	Like you were like yeah.	\n"
"	student-2	Okay.	I did like this.	\n"
"	tutor	I can't I can't see that so what would	I can't see that.	\n"
"	tutor	What would the last, so we have three P equals 20,  so what's that last step gonna be?	So we have three P equals 20, So what's that last step going to be?	\n"
"	student-2	Okay, I'm writing it down.  Division.	I'm writing it down, division.	\n"
"	tutor	And what do we divide by?	And what do we divide by?	\n"
"	student-2	Three.	Three?	\n"
"	tutor	Great, good.  Divide by three on both sides,  and then we can leave it as.	Three, good, divide by three on both sides and then we can leave it as a fraction.	\n"
"	tutor	fractions then we just get p equals 20 over 3.	So we just get P equals 20 over three.	\n"
"	tutor	So what I just wanted to show you is that I just wanted to show you that  what we do when we have numbers is the same thing with when we have variables.	So what I just wanted to show you is that I just wanted to show you that what we do when we have numbers is the same thing when we have variables.	\n"
"	tutor	So, that's why I wanted to go over that with you.	So that's why I wanted to go over that with you.	\n"
"	tutor	So this right here in this box and the do now problem are essentially the same thing.  So I'm going to move us on to our example now. So I want you to, what I want you both to do is I  want you to work on part A for number two independently, and I want you both to take  one minute to do that.	So this right here in this box and the Do Now prompt are essentially the same thing so I'm going to move us on to our example now, so what I want you both to do is I want you to work on part A for number two independently, and I want you both to take 1 minute to do that.	\n"
"	tutor	So I want you to work on part A independently for the next minute and then put your answer on your boards.	So I want you to work on part A independently for the next minute and then put your answer on your boards,	\n"
"	tutor	Okay, so I'll give us an extra 30 seconds.	I'll give us an extra 30 seconds.	\n"
"	tutor	Okay, so let's start going over.	Okay, so let's start going over.	\n"
"	tutor	I'm gonna bring you to cash first	I'm going to bring you to Cashmere's board.	\n"
"	tutor	So, Kashmir, you distributed the P into the 1 plus RT.  Can you tell me why you did that?	So, cashmere, you distributed the P into the one plus RT, can you tell me why you did that?	\n"
"	student-1	Because in algebra, I was told to always distribute.	Because in algebra, I was told to always distribute.	\n"
"	tutor	Okay, so we're gonna get some mixed signals here, unfortunately.	Okay, so we're going to get some mixed signals here, unfortunately.	\n"
"	tutor	But the way that I would think about it is I would think to myself, okay, so I  Want to solve for P. So what does that?	But the way I would think about it is I would think to myself, okay, so I want to solve for p, so what does that mean?	\n"
"	tutor	mean when we solve for p? What do we have to have to solve for p?	When we solve for p, what do we have to have to solve for P alone?	\n"
"	student-1		Have p alone.	\n"
"	tutor	I love you, Ron.  Mm-hmm.  Bye.	mm-hmm	\n"
"	tutor	So if I distribute into the 1 plus RT, I get P and then I get P plus RT.	So if I distribute into the one plus RT, I get p, and then I get p plus RT.	\n"
"	tutor	So now I have two Ps and I have one of them attached to the RT.	So now I have two p's, and I have one of them attached to the RT.	\n"
"	tutor	So it's not going to make it easier or harder to get pee bites.	So is that going to make it easier or harder to get p by itself?	\n"
"	student-1		harder.	\n"
"	tutor	Right	Right.	\n"
"	tutor	So, we have our P, and it's multiplied by everything in the parentheses.	So, Isabel, we have RP, and it's multiplied by everything in the parentheses.	\n"
"	tutor	So, Lisbeau, can you think of a way that we could really quickly get pee by itself?	So Isabel, can you think of a way that we could really quickly get p you by itself?	\n"
"	tutor	Make sure you're on mute.	Make sure you're unmuted	\n"
"	student-2	I was thinking maybe combining like...	I was thinking maybe combining [inaudible]	\n"
"	tutor	So we don't have any like terms.	So we don't have any like terms, right?	\n"
"	tutor	right, because we have variables with different letters,  and then we have our number.  So there's no like terms to put together.	Because we have variables with different letters, and we have a number, so there's no like terms to put together.	\n"
"	tutor	So what could we do with everything in our parentheses  to get it separated from P?	So what could we do with everything in our parentheses to get it separated from p?	\n"
"	student-2	So shocked.	subtract?	\n"
"	tutor	So P and the parentheses are multiplied together, right?	So p and the parentheses are multiplied together, right?	\n"
"	tutor	So we would subtract if the parentheses were being added to...	So we would subtract if the parenthesis were being added to p.	\n"
"	tutor	So what could we do instead?	So what could we do instead?	\n"
"	student-1	Is it? Is it the video?	Is that the [inaudible]?	\n"
"	tutor	Yep, good job Cash Sphere.	Yes, good job, cashmere.	\n"
"	tutor	so we can divide.	So we can divide everything.	\n"
"	tutor	So we can divide by one plus RT.	So we can divided by one plus RT.	\n"
"	tutor	So if we divide that on the right side, that cancels out.  And then, Kashmir, on the left,  if we do A over one plus RT,  is there any way we can simplify it  or any like terms that we can put together?	So if we divide that on the right side, that cancels out, and then cashmere on the left, If we do a over one plus RT, is there any way we can simplify it or any like terms that we can put together?	\n"
"	student-1	you	No.	\n"
"	tutor	Nope, so we're just going to leave it like that as a over 1 plus RT equals p.	No, so we're just going to leave it like that as a over one plus RT equals p.	\n"
"	tutor	So what I want you to remember is that when you see parentheses just attached to some  random variable, if we want to solve for that variable, we can divide by everything in the  parentheses.	So what I want you to remember is that when you see parentheses, just to attach to some random variable, if we want to solve for that variable, we can divide by everything in the parentheses.	\n"
"	tutor	So you can think of the parentheses as its own, like, self-contained thing.	So you can think of the parentheses as its own, like, selfcontained thing.	\n"
"	tutor	So just treat the parentheses like it's its own number or its own variable.	So just treat the parentheses like it's its own number or its own variable.	\n"
"	tutor	Now for T. For T it's going to be harder, right?	Now for t, for t, it's going to be harder, right?	\n"
"	tutor	because T is inside the parentheses.  So we can't just divide by the parentheses  to get it by itself.	Because t is inside the parentheses, so we can't just divide by the parentheses to get it by itself.	\n"
"	tutor	So I want us to think about what we just did. We divided by 1 plus RT.	So I want us to think about what we just did when we divided by one plus RT.	\n"
"	tutor	I try to think, how could we start getting things separated from...	Try to think, how could we start getting things separated from t?	\n"
"	tutor	So, Lisvel, what's the first thing we could do?	So, Isabel, what's the first thing we could do?	\n"
"	student-2	So, this is the creative, I feel like, okay.	So to separate it I can like	\n"
"	student-2	I had an idea.	I have an idea.	\n"
"	tutor	Sure, what's your idea?	Sure, what's your idea?	\n"
"	student-2	So I'm gonna go a little off on the whim, I guess.	So I'm going to go a little off on the wind, I guess.	\n"
"	student-2	What's it called when you um...  This is a name for it, I just don't know.	What's it called when you, there's a name for it, what's it called?	\n"
"	tutor	So what were you thinking of doing, specifically?	What were you thinking of doing specifically?	\n"
"	tutor	So not the name for it, but just what would it do to the equation?	So not the name for it, but just what would it do to the equation?	\n"
"	student-2	I mean, I guess I'd like divert it.	I mean, I guess I'd like divert it.	\n"
"	tutor	divide	Divide?	\n"
"	student-2	Yeah.	Yeah.	\n"
"	tutor	So what do you want to divide by?	So what do you want to divide by?	\n"
"	student-2	One.	one?	\n"
"	tutor	If we divide by 1, we don't change anything.	Remember, when you divide by one, you don't change anything.	\n"
"	tutor	So multiplying by one and dividing by one  never change anything.  So that's not going to do anything.	So multiplying by one and dividing by one never change anything, so that's not going to do anything.	\n"
"	tutor	So this 1 that's in here, dividing by 1 is not going to get rid of it.  Because if you divide 1 by 1, you still have 1.	So this one that's in here, dividing by one is not going to get rid of it, because if you divide one by one, you still have one.	\n"
"	tutor	I want us to think for a second about this	I want us to think for a second about this p.	\n"
"	tutor	So, what could we do with our P, Lisbel?	So what could we do with our P, Isabel?	\n"
"	student-2	With the P, I guess you could use that to make this tube.	Put the p, I guess [inaudible]	\n"
"	tutor	Then we're going to have, Makai, all right.  Glad you can join.	Then We're going to have... Mickay, all right, Glad you can join us.	\n"
"	tutor	Okay, so I'm gonna, I'm gonna start you off Akai.  So we have this equation here,  A equals P times one plus RT.  And we wanna solve for T.	Okay, I'm going to start you off, Mickay, so we have this equation here, a equals P times one plus RT, and we want to solve for T.	\n"
"	tutor	So I'm trying to I want to start getting things separated away from this T on the other side	So I want to start getting things separated away from this T on the other side.	\n"
"	tutor	what's the first thing that we could do?	What's the first thing that we could do?	\n"
"	student-3	Oh, wait, wait, what side?  This one?	Wait, what side, this one?	\n"
"	tutor	Yes, so we want to solve for T. So we need everything except for T moved over to the  left.	Yes, we want to solve for T, so we need everything except for T moved over to the left.	\n"
"	student-3	Okay, let's see what you guys have	Okay, let's see what you guys have.	\n"
"	student-3	you have P1 plus PRT	You have p one plus PRT.	\n"
"	tutor	So that was something that Cashmere did for part A, so I want us to focus on part B.	That was something that Cashmere did for part A, so I want us to focus on part B.	\n"
"	tutor	So, part A we had to solve for P.	So part A, we had to solve for P.	\n"
"	tutor	Part B we have to solve for T, so it's a different kind of problem.	Part B, we have to solve for T, so it's a different kind of problem.	\n"
"	student-3	Oh, so free.	Oh, solve for T.	\n"
"	student-3	t well I would still do the same thing but just divide PR by PR and then I  would get T and then divide P1 by P so just divide	Well, I would still do the same thing, but just divided by PR by PR, and then I will get T and then divide P one by p, so just divided PR.	\n"
            "</Example transcript> \n \n"
            "<Transcript> "
"	tutor	Good afternoon Julio, just get started on your dinner.	\n"
"	tutor	Okay, so that was the end of the four minutes.	\n"
"	tutor	It seems like we might have had trouble on there too now, so let's go over it.	\n"
"	tutor	So that's the kind of.	\n"
"	tutor	Number one, what does number one say?  It says, write an expression that represents Sarah's age  in terms of Marcus's age and define our variables.	\n"
"	tutor	So they told us that Sarah is twice as old as Marcus.	\n"
"	tutor	When we see that twice, what does that mean?	\n"
"	student-1	Oh no.	\n"
"	tutor	What does that sound like?	\n"
"	tutor	for sure.	\n"
"	student-1	We win.  Yes.	\n"
"	tutor	Two.	\n"
"	tutor	Right? And when it's twice, what operation is that?	\n"
"	student-1	Tom's	\n"
"	tutor	Multiplication, right?	\n"
"	tutor	Okay, so we're multiplying something by two.	\n"
"	tutor	Who is twice as old as Sarah?	\n"
"	tutor	I mean, she's twice as old as who?	\n"
"	student-1	Marcus.	\n"
"	tutor	Marcus, do we know Marcus's age?	\n"
"	student-1		\n"
"	tutor	So what will we put there?	\n"
"	student-1	Well, zero.	\n"
"	tutor	If we don't know the value...	\n"
"	tutor	If we don't know the playthrough...	\n"
"	student-1	Oh, X, a number.	\n"
"	tutor	a variable.	\n"
"	student-1		\n"
"	tutor	So let's say M for Marcus.  And we're trying to.	\n"
"	tutor	find out they want us to write an expression that represents charity.	\n"
"	tutor	And we know that Sarah is twice as...	\n"
"	tutor	So our expression should just be two.	\n"
"	tutor	right? That two represents the twice and the M represents the eight.	\n"
"	tutor	So we will have 2M, M being Marcus' age here.	\n"
"	tutor	What about number two?	\n"
"	tutor	So number two, they're talking about a child.	\n"
"	student-1	Wait, so that's the answer from number one?	\n"
"	tutor	What?	\n"
"	student-1	Hmm?	\n"
"	tutor	Yeah.	\n"
"	student-1	I'm just kidding.  Oh my.	\n"
"	tutor	Simple as that. Simple as that.	\n"
"	student-1	Bro, you got it bro?	\n"
"	student-2	Yes!	\n"
"	tutor	Will the O. say yes?	\n"
"	tutor	Why don't you try to age?	\n"
"	student-1	She said why you didn't write it on the page	\n"
"	student-2	I did.	\n"
"	student-1	He's de-friendly, and it chutn't hurt to train a trap with another.  You think?	\n"
"	tutor	I didn't see it, but let's look at number two.	\n"
"	tutor	So what do we have to do here?	\n"
"	tutor	What are we doing here number two?	\n"
"	student-1	Umm, I don't know.	\n"
"	tutor	That's your favorite	\n"
"	student-1	Just to see how big the Chicago Tower is.	\n"
"	tutor	Uh-huh, in terms of the...	\n"
"	tutor-and-student-1	School busted.	\n"
            "</Transcript>"
            }
    ]
)

# Print the response
with open("test.txt", 'w') as file:
    file.write(response['message']['content'])

print(response['message']['content'])