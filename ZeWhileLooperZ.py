print('Hey, in this game to practice while loops in Python, you will be answering questions about the rapper, Zelooperz.')

respuesta_uno = str(input('What US City is ZelooperZ from?'))
while respuesta_uno != 'Detroit':
    print('Incorrect, please try again my g.')
    respuesta_uno = str(input('What US City is ZelooperZ from?'))
if respuesta_uno == 'Detroit':
    respuesta_dos = str(input)
while respuesta_dos != 'Bruiser Brigade':
    respuesta_dos = str(input('Question 2: What is the name of the hip hop collective he is part of?'))
if respuesta_dos == 'Bruiser Brigade':
    print('Muy fuego, nice job.')
respuesta_tres = int(input('Question 3: In what year was his first album "Help" released?'))
while respuesta_tres != 2014:
    print('Try again.')
    respuesta_tres = int(input('Question 3: In what year was his first album "Help" released?'))
if respuesta_tres == 2014:
    print('Wow you know a lot about ZelooperZ.')
    respuesta_cuatro = str(input("Question 4: Which famous artist's left ear is his latest album named after?"))
while respuesta_cuatro != 'Van Gogh':
    print('Give it another go!')
    respuesta_cuatro = str(input("Question 4: Which famous artist's left ear is his latest album named after?"))
if respuesta_cuatro == 'Van Gogh':
    print('Alright, good knowledge bruh bruh. For the last one, please complete the lyric:')
respuesta_cinco = str(input('Visions hard to see me like ___________'))
while respuesta_cinco != 'white on rice':
    print('Try once more fam.')
    respuesta_cinco = str(input('Visions hard to see me like ___________'))
if respuesta_cinco == 'white on rice':
    print('Good stuff. You finished the ZelooperZ game!')
