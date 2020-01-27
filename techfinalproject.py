#in order to use random chance
import random
#this is to be able to select random options so that each time you play the experience is individualized.
randomuclteam=random.choice(["Real Madrid","FC Barcelona","PSG","Bayern Munich","Juventus"])
agentname=random.choice(["Mark","Logan","Robert"])
plteam1=random.choice(["Liverpool", "Everton", "Manchester United"])
plteam2=random.choice(["Manchester City", "Arsenal", "Leister City"])
plteam3=random.choice(["Chelsea","Tottenham"])
eflteam1=random.choice(["Aston Villa","Blackburn Rovers","Derby County","QPR","Stoke City"])
eflteam2=random.choice(["Swansea City","Leeds United","Sheffield United","Wigan Athletic","Middlesbrough"])
scout1=random.choice(["Jackson","Briggs","Jose","Antonio","Larry"])
scout2=random.choice(["Patrick","Valentine","Harry","Arthur"])
trainername=random.choice(["Alex","Blake","Cody","Steven","Forty"])
#starts the game, provides instructions and an introductory paragraph.
print("In order to play this game, please type the number next to whichever option you wish to choose (ex. if option 1 is 1.get breakfast, type 1 to select it.")
print("Welcome to Premier Career Football. You are an aspiring young soccer player who hopes to make it to the ultimate platform one day, the Premier League, and win the League title. In order to get there, you will have to make tough decisions and difficult sacrifices that put your entire career on the line. Every choice you make has a direct impact on how your story will end. Will you make it to the big lights, with 50,000 people chanting your name? Or will you be left behind the beautiful game, stranded like the millions before you?")
#in order to create a player name, we ask for an input value in which they tell the game their name.
name=input(print("First, what is your name?"))
#the name is now incorporated into the rest of the story.
#the random chance for different elements also appear in the story using the formatted string, and allow for individualized experience.
print(f"Your name is {name}. You wake up at 6 AM, ready to start a new day of training. You stretch briefly and turn over to see a text on your phone. It’s from {trainername}, your trainer. “Hey {name}, remember, today trial scouts are coming to the academy to observe the practice! Be at your best-” You groan. You feel terrible this morning, and trials are the make or break into the next level of competitive football. Today could be the most important day of your life, and you feel absolutely depleted.")
#this is a junction, or decision spot. the player picks an option and the story unfolds depending on whichever option the player selected. this is shown through an if, elif and else option, in which each option is coded to have a different outcome (and account for values that are not acceptable.)
option1=input(print("1.STAY IN BED 2.GET DRESSED"))
if option1=="1":
  print(f"You decide to sleep it off a couple of minutes…BZZZ! You turn over. You dozed off and now are half an hour late for practice!!! You hurry into the car and speed off towards the training grounds.")
  print(f"As you frantically sprint towards the locker room, you get a text on your phone. You glance and see that it’s from {trainername}. “This was it, {name}. I told you this was once in a lifetime, and now they’re gone. Maybe next time.” You stop, realizing that you would never get this chance again. Back to the training grounds.")
  exit()
elif option1=="2":
  print(f"You throw on your training gear and grab a bite to go. You drive anxiously to the training grounds, thinking about the possibilities today could have if you play this right. You arrive and walk into the academy, seeing the people and trainers along with a few scouts. Your heart starts to beat faster, but you force yourself to breathe and calm down. You see {trainername} and jog over to him. {trainername} explains that you were going to start off with some basic drills, but then there would be an 11v11 scrimmage to showcase for the scouts. Time to get to work.")
else:
  print("Please select an option.")
option2=input(print("1.LEAVE THE GROUNDS 2.START TRAINING"))
if option2=="1":
  print(f"As you turn to leave, {trainername} grabs your arm. “Uh, no, {name}. I’m not letting you blow this opportunity off. Let’s get to it.")
  print(f"You collapse on the side of the pitch, exhausted from having run for nearly 2 hours. You feel a hand on your shoulder and a deep voice behind you say: “Good stuff lad, you showed some serious potential in the kick-around.” You turn around to see {trainername} standing next to a man holding a clipboard. A scout! “My name is {scout1}. I scout for the team {eflteam1}. We have been scouting you for a while, {name}. Do you have a few minutes to talk about your future?”")
elif option2=="2":
  print(f"You collapse on the side of the pitch, exhausted from having run for nearly 2 hours. You feel a hand on your shoulder and a deep voice behind you say: “Good stuff lad, you showed some serious potential in the kick-around.” You turn around to see {trainername} standing next to a man holding a clipboard. A scout! “My name is {scout1}. I scout for the team {eflteam1}. We have been scouting you for a while, {name}. Do you have a few minutes to talk about your future?”")
else:
  print("Please select an option.")
#this is an example of a situation in which a choice depends on the previous choice. selecting a specific pathway through the game leads you to each individual point.
option3=input(print("1.I WOULD LOVE TO 2.SORRY, I DON'T THINK SO"))
if option3=="1":
  print(f"“At the {eflteam1} academy, we take training very seriously. If you come to play for us, you will need to put in 100% and more to survive. It is hard - I will not lie to you. But I can make your dreams of playing in the Premier League a reality. What do you say?”")
  option4=input(print("1.YES 2.NO"))
  if option4=="1":
    print(f"“I’ll talk matters over with your trainer, but I hope to see you soon {name}. Our facilities are among the top in the nation, and you will feel right at home. Keep working hard and I will be in touch.”")
  elif option4=="2":
    print(f"That’s a shame. I was hoping to see you at the {eflteam1} academy. Hope to see you around.”")
    print(f"You watch {trainername} and the scout walk away. As you start to head back to the tunnel, you hear someone shout your name vaguely. You turn and see a man running up to you, reaching you with surprisingly little breath lost.")
  print(f"“Hey {name}, my name is {scout2}, and I just saw your performance today at the scrimmage. I scout for the team {eflteam2}. I wonder if you would be interested in joining our program? It’s been a while since I have seen a young talent like you.”")
  option5=input(print("1.YES 2.NO"))
  if option5=="1":
    print(f"“I look forward to seeing you, {name}. I think you will settle in nicely, and I know you can make a name of yourself.”")
  elif option5=="2":
    print(f"“That’s a shame. I was hoping to see you at the {eflteam2} academy. Hope to see you around.”…Months go by, and each day of training feels more and more mundane. You start to think maybe you should have taken an offer.")
    exit()
  else:
    print("Please select an option.")
elif option3=="2":
  print(f"“That’s a shame. I was hoping to see you at the {eflteam1} academy. Hope to see you around.”")
  print(f"You watch {trainername} and the scout walk away. As you start to head back to the tunnel, you hear someone shout your name vaguely. You turn and see a man running up to you, reaching you with surprisingly little breath lost.")
  print(f"“Hey {name}, my name is {scout2}, and I just saw your performance today at the scrimmage. I scout for the team {eflteam2} I wonder if you would be interested in joining our program? It’s been a while since I have seen a young talent like you.”")
  option5=input(print("1.YES 2.NO"))
  if option5=="1":
    print(f"“I look forward to seeing you, {name}. I think you will settle in nicely, and I know you can make a name of yourself.”")
  elif option5=="2":
    print(f"“That’s a shame. I was hoping to see you at the {eflteam2} academy. Hope to see you around.”…Months go by, and each day of training feels more and more mundane. You start to think maybe you should have taken an offer.")
    exit()
  else:
    print("Please select an option.")
else:
  print("Please select an option.")
print(f"...Two weeks have passed. You are feeling confident about the club, and already made a couple of friends on the team who have been helpful and positive influences. You feel that your skills are growing and that the team dynamic and chemistry complement your style. For now, you remain on the bench, but the trainer has mentioned that with your constant improvement, you might be getting in games very soon.…It is the day of the semi-finals of the FA Cup. You line up at the touchline, knowing that today might be your big day. You look up and see the crowds of people chanting, and imagine your name ringing around the stadium.")
option6=input(print("1.ASK THE MANAGER FOR A SUBSTITUTION 2.WAIT"))
if option6=="1":
  print("Mate, that’s not how this works. One more word out of you and we’re having a very different conversation.”")
elif option6=="2":
  print("...")
else:
  print("Please select an option.")
print(f"Its the 80th minute of the game, the score is tied 2-2, and the striker gets injured in the midfield. You find yourself being pushed forward, and soon your standing on the byline, waiting for your substitution. “Number 23, {name}, coming in as a late sub. This is his first professional appearance and his first introduction to the FA Cup. Let’s see what he can muster.” You enter the pitch and hear the crowd chanting your name. It’s all or nothing now.")
option7=input(print("1.CHEER WITH THEM 2.WALK WITH CONFIDENCE"))
if option7=="1":
  print("You hear the crowd roar as you lift your arms, ready to take the game on.")
elif option7=="2":
  print("You walk onto the pitch with confidence. You know you are ready to win.")
else:
  print("Please select an option.")
print("It’s the dying seconds of the game. A low cross comes in, and you find yourself in the middle of the box with room for a shot. The ball hurtles toward you, and you turn to face the goal.")
option8=input(print("1.HIT IT FIRST TIME 2.TAKE A TOUCH"))
if option8=="1":
  print("There is no doubt in your mind. As the ball comes down, you meet it first time with your foot and get a clean strike. It sails into the top right corner, earning the winner and erupting the stadium in noise.")
elif option8=="2":
  print("You think you can volley it, but decide to play it safe. You take a touch, but space closes in and two defenders come in from the sides. ")
  option9=input(print("1.SHOOT ANYWAY 2.FAKE A SHOT"))
  if option9=="1":
    print("You decide to risk it and shoot. The ball barely misses the two defenders’ legs and curls into the lower right hand corner, earning the winner as you run to the corner flag to celebrate with the stadium chanting your name.")
  elif option9=="2":
    print("You fake a shot, but the two defenders aren’t fooled. The opposing left-back makes a slide tackle towards the ball, and connects - along with your ankle. The last thing you remember before you hit the ground is a splitting pain in your left foot.…A month has passed. Your team lost the semi-final, and you were hospitalized for a broken ankle and torn ACL. The doctor talks to you about treatment and rehabilitation, but the message is clear: you will never play again.")
    exit()
  else:
    print("Please select an option.")
else:
  print("Please select an option.")
print(f"It has been three weeks since your famous last-minute winner in the semi-final. The team ended up losing in the final, but it didn’t matter - you had already achieved overnight fame through that clinical finisher. You are ready to go to training when suddenly your phone rings. It’s your agent, {agentname}. “Hey, {name}. Make sure you’re sitting right now, because your gonna faint when I tell you this. {plteam1}, {plteam2}, and {plteam3} have expressed an interest in you. Who do you want to hear from?”")
#here, the random choice is being used in the user selection.
option10=input(print(f"1.{plteam1} 2.{plteam2} 3.{plteam3}"))
if option10=="1":
  print(f"You show up at the legendary {plteam1} training grounds. You meet the first team and subs, talk quickly with the manager about a contract, and get situated. Everything becomes a surreal blur of excitement and awe. You know this is where you belong.")
  option11=input(print("1.CHECK OUT THE LOCKER ROOM 2.WALK AROUND THE PITCH"))
  if option11=="1":
    print("You walk around the locker room, admiring the clean jerseys and envisioning your own when you hear a gruff voice from behind you. “Nothing like seeing these for the first time.”")
  elif option11=="2":
    print("You tour the field, imagining yourself playing in this packed stadium when a deep voice speaks up from behind you. “Imagining yourself playing here? I did that when I first started as a player.”…You turn and see the manager of the club. He looks at you approvingly. “I just wanted to stop in and say personally that I see potential in you. Work hard, and we might get you in the Champions League rounds. Best of luck.”")
  else:
    print("Please select an option.")
elif option10=="2":
  print(f"You show up at the legendary {plteam2} training grounds. You meet the first team and subs, talk quickly with the manager about a contract, and get situated. Everything becomes a surreal blur of excitement and awe. You know this is where you belong.")
  option12=input(print("1.CHECK OUT THE LOCKER ROOM 2.WALK AROUND THE PITCH"))
  if option12=="1":
    print("You walk around the locker room, admiring the clean jerseys and envisioning your own when you hear a gruff voice from behind you. “Nothing like seeing these for the first time.”")
  elif option12=="2":
    print("You tour the field, imagining yourself playing in this packed stadium when a deep voice speaks up from behind you. “Imagining yourself playing here? I did that when I first started as a player.”…You turn and see the manager of the club. He looks at you approvingly. “I just wanted to stop in and say personally that I see potential in you. Work hard, and we might get you in the Champions League rounds. Best of luck.”")
  else:
    print("Please select an option.")
elif option10=="3":
  print(f"You show up at the legendary {plteam3} training grounds. You meet the first team and subs, talk quickly with the manager about a contract, and get situated. Everything becomes a surreal blur of excitement and awe. You know this is where you belong.")
  option13=input(print("1.CHECK OUT THE LOCKER ROOM 2.WALK AROUND THE PITCH"))
  if option13=="1":
    print("You walk around the locker room, admiring the clean jerseys and envisioning your own when you hear a gruff voice from behind you. “Nothing like seeing these for the first time.”")
  elif option13=="2":
    print("You tour the field, imagining yourself playing in this packed stadium when a deep voice speaks up from behind you. “Imagining yourself playing here? I did that when I first started as a player.”…You turn and see the manager of the club. He looks at you approvingly. “I just wanted to stop in and say personally that I see potential in you. Work hard, and we might get you in the Champions League rounds. Best of luck.”")
  else:
    print("Please select an option.")
print("You’ve been with the team for around a couple of months. You have started to make some substitute appearances in league games, but nothing major. The manager steps in to talk to you.")
option14=input(print("1.AM I GOING IN 2.ITS ABOUT TIME"))
print(f"The manager laughs. “I have seen a lot from you already. You will be starting in the upcoming Champions League game. Don’t let me down.”…You and a couple of teammates are in the rec room, hovering around the TV. You hear the announcer speaking: “-and the team they will be facing in the UCL draw is...{randomuclteam}!” There is a mixture of gasps and cheers around you, but you are determined and resolute. The day will come soon enough.... It is the group stage of the UEFA Champions League. The score is 3-2, and your team is down by one. You have been roughed and beaten up the whole game, but you know that it is now or never. One goal would push it to PKs.The ball gets to your feet. You scan the field quickly.")
option15=input(print("1.1-2 PASS AND MOVE 2.SWITCH THE FIELD"))
if option15=="1":
  print("You play a quick 1-2 pass off your center mid. You get the ball back and dribble up the field, playing a chip ball when a tackle comes in.")
elif option15=="2":
  print("You lob the ball across the midfield and move into space. You shake a defender and sprint down the byline, making a run for the corner flag.")
else:
  print("Please select an option.")
print("As you get open, the ball is played back to you. You are in the final third of the pitch, and you have men open in the box.")
#another example of an option pathway that depends on previous choices.
option16=input(print("1.CROSS 2.CUT INSIDE"))
if option16=="1":
  print("You put in a cross to the far post. One of your attacking midfielders gets up, and heads the ball back. It falls to the center midfielder, who settles the ball, shoots - and scores!!!")
elif option16=="2":
  print("You chop the ball and cut inside, breezing past a defender. The lane opens up nicely for a curler to the left post.")
  option17=input(print("1.SHOOT 2.THROUGH PASS"))
  if option17=="1":
    print("Your foot comes back and makes good contact with the ball, giving it a wicked spin right into the top left corner of the goal - scoring to make it tied at 3-3!!!")
  elif option17=="2":
    print("You split the remaining two defenders, putting a through ball right towards your attacking midfielder, who jumps around the goalkeeper - and scores the equalizer!!!")
  else:
    print("Please select an option.")
else:
  print("Please select an option.")
print("It all comes down to PKs. This will determine whether or not your team will make it into the next round of the Champions League, and will put you permanently in the soccer limelight. The score is 4-4, with {randomuclteam} just missing their last penalty. It’s all up to you.")
option18=input(print("1.CHEEKY PANENKA CHIP SHOT 2.BLAST IT STRAIGHT DOWN THE MIDDLE 3.AIM FOR THE CORNERS"))
if option18=="1":
  print("You step up, run forward and shoot - and it fakes out the goalkeeper! The shot floats easily into the goal as the keeper dives before the trick shot.")
elif option18=="2":
  print("You sprint towards the ball, never slowing down as you put your boot straight through it. You look up and - you’ve scored! The keeper guessed wrong and was too slow to recover from your rocket.")
elif option18=="3":
  print("You run up to the ball, carefully placing your feet and executing a textbook penalty that has the perfect curve, speed, and finesse to place it right in the bottom right-hand corner. It is a perfect penalty, and there was no way the keeper was getting there.")
else:
  print("Please select an option.")
print("You win the Champions League round!! Your teammates lift you above their heads, cheering and shouting, and the whole crowd is screaming your name. As you see the benches empty and the scenes of joy, you know you are exactly where you need to be.")