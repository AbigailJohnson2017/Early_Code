print('How "college" is your bedroom?')
print('Youre in the mood to redecorate, so you go Amazon Priming for...')
print('1. A tastefully framed abstract print that will look perfect in my "at home, bored" Instagrams')
print('2. Something fun under $30. Maybe one of those marquee signs?')
print('3. Well, this tapestry takes up a lot of room, so IDK if I need new stuff.')
one=input('1 Which option do you choose?')
one=int(one)
print('Whats your headboard situation?')
print('1. I got a tufted one at West Elm as soon as I got a raise')
print('2. I mean, I bought it off the girl who lived here before me... but its actually nice')
print('3. Nonexistent.')
two=input('2 Which option do you choose?')
two=int(two)
print('IYO, Christmas lights should be used for...')
print('1. Trees?')
print('2. Glowing up my windows! Their light is like an IRL filter!')
print('3. Shoving into empty wine bottles and plugging them in when guests come over, obviously')
three=input('3 Which option do you choose?')
three=int(three)
print('Whats your stance on hampers?')
print('1. Pro. I have a wicker one in the corner. Best $40 I ever spent')
print('2. I have the collapsible one from my freshman year. It will outlive me and my future children')
print('3. I use a designated chair. It counts.')
four=input('4 Which option do you choose?')
four=int(four)
print('Its a Sunday morning. Youre currently snuggling up in...')
print('1. A pile of throw pillows *and* an accent blanket')
print('2. My fluffy-ass duvet and the pillows I sleep on')
print('3. My stuffed animals and some fuzzy white pillows - or maybe my fuzzy white rug if Im hung over')
five=input('5 Which option do you choose?')
five=int(five)
print('Hey: Wheres the towel you showered with this morning?')
print('1. On the wooden rack I installed myself, tyvm')
print('2. I have one of those metal hangy things on my door')
print('3. Goooooood Q. The floor? Maybe?')
six=input('6 Which option do you choose?')
six=int(six)
result=one+two+three+four+five+six
if 10 <= result <= 11:
    print('Your bedroom is *actually* Apartment Porn. Age appropriate? Sure. Sophisticated? Kinda. Not embarassing if anyone visits at 2am? Def. Give any of your friends who got 3s on this quiz an assist.')
if 12==result:
    print('Youve officially started to dabble in the decor arts, and thats great. Youre, like, one non-poster piece of art away from truly calling yourself a Grown')
if result >=13:
    print('Somebody call Bobby Berk, because your setup screams "eternally 21." If youre legit 21, cool. If not, please see every 1 answer in this quiz and visit your nearest laptop to order renters-insurance-worthy accessories.')
