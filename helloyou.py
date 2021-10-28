import time


print("Welkom bij mijn beroeps opdracht. In dit spel is het de bedoeling dat je vlucht van je land zonder dood te gaan. Veel speel plezier!")

time.sleep(3)

def vraag0(): 
    vraag0 = input("Wil je het spel starten? \n A) ja \n b) nee ") 
    if vraag0.lower() == "a":
        vraag1()
    elif vraag0.lower() == "b":
        print("ok")
        

def vraag1():
    vraag1 = input("Er breekt oorlog uit in je land wat doe je? \n A) Je blijft \n B) Je vertrekt naar het buiteland \n C) Je sluit je aan bij een groep rebellen ") 
    if vraag1.lower() == "a":
        vraag2()
    elif vraag1.lower() == "b":
        vraag10()
    elif vraag1.lower() == "c":
        vraag14()


def vraag2(): 
    vraag2 = input("Blijf je in bed liggen of poets je je tanden? \n A) Je gaat verder met slapen \n B) Je poets je tanden ") 
    if vraag2.lower() == "a":
        vraag3()
    elif vraag2.lower() == "b":
        vraag3()


def vraag3(): 
    vraag3 = input("Je hoort een hard geluid en er klopt iemand op je deur wat nu? \n A) Je doet de deur open \n B) Je verstopt je ") 
    if vraag3.lower() == "a":
        vraag4()
    elif vraag3.lower() == "b":
        vraag9()

def vraag4(): 
    vraag4 = input("Er staat een taliban voor je deur. Werk je mee of probeer je weg te rennen. \n A) Werk mee \n B) Ren weg ") 
    if vraag4.lower() == "a":
        vraag5()
    elif vraag4.lower() == "b":
        print("Dat was misschien niet zo slim, je hebt dood geschoten.")
        vraag3()

def vraag5(): 
    vraag5 = input("Je komt erachter dat je elkaar kent van de basischool en hij wilt je helpen met vluchten. Hij vraagt waar je heen wilt. \n A) Duitsland \n B) Nederland ") 
    if vraag5.lower() == "a":
        print("Hij zegt dat Nederland beter is voor vluchtelingen en raad het daardoor aan, je vind het een goed idee.")
        vraag6()
    elif vraag5.lower() == "b":
        vraag6()

def vraag6(): 
    vraag6 = input("Hij vind het een goed idee en en geeft je een telefoon met een sim kaart. Ook geeft hij je een vliegticket en een vervalsd paspoort. Hij vraagt waar wil je in nederland gaan wonen. \n A) Zuiden \n B) Noorden ") 
    if vraag6.lower() == "a":
        vraag7()
    elif vraag6.lower() == "b":
        vraag7()

def vraag7(): 
    vraag7 = input("Hij vind het een goede keuze. Je gaat naar bed en de volgende dag stap je op het vliegtuig en zwaait hem gedag. Je vertelt de duane dat je een vervalsd paspoort hebt. Ze vragen je om een van hun te volgen naar een kantoor kamertje. Ze geven je een kop koffie en vragen in welke gemeente je wilt wonen. \n A) Gemeente Noord-Holland \n B) Gemeente Braband ") 
    if vraag7.lower() == "a":
        vraag8()
    elif vraag7.lower() == "b":
        vraag8()

def vraag8(): 
    vraag8 = input("Ze vertelen je dat je over 3 dagen naar een kantoor in Den haag moet komen op verdere afspraak, en dat dan geregeld word dat je een nederlands paspoort krijgt, en alles geregeld word. Je wacht de 3 dagen op een station waar je van de bakker wat broodjes en water krijgt. Je komt op het kantoor aan en ze geven je de keuze tussen werk sectoren waar ze een baan voor je kunnen regelen. \n A) Kantoor werk \n B) Groen werk ") 
    if vraag8.lower() == "a":
        print("Je bent aangenomen. Het is nu 3 jaar later en je hebt je eigen apartement en leeft nu een vrolijk leven in Nederland ")
        restart()
    elif vraag8.lower() == "b":
        print("Je bent aangenomen. Het is nu 3 jaar later en je hebt je eigen apartement en leeft nu een vrolijk leven in Nederland ")
        restart()

def vraag9(): 
    vraag9 = input("Waar wil je verstoppen? \n A) Onder je deken \n B) Onder je bed \n C) In je kledingskast ") 
    if vraag9.lower() == "a":
        print("Ze kunnen je niet vinden en gaan weer weg.")
        vraag10()
    elif vraag9.lower() == "b":
        print("Ze kunnen je niet vinden en gaan weer weg.")
        vraag10()
    elif vraag9.lower() == "c":
        print("Dat was niet de beste plek. Ze hebben je gevonden en nemen je mee ")
        vraag5()

def vraag10(): 
    vraag10 = input("Waar wil je heen vluchten? \n A) Europa \n B) Amerika ") 
    if vraag10.lower() == "a":
        vraag11()
    elif vraag10.lower() == "b":
        vraag11()

def vraag11(): 
    vraag11 = input("Je vraagt je af hoe je erheen wilt gaan? Je ziet een bus met wat lijkt op illegale smokelaars ga je met ze mee? \n A) ja \n B) nee ") 
    if vraag11.lower() == "a":
        vraag12()
    elif vraag11.lower() == "b":
        vraag17()

def vraag12(): 
    vraag12 = input("Ze nemen je mee naar een obekende locatie en zetten je in een klein bootje met veel andere. Je vraagt hun \n A) Hoelang duurt de reis? \n B) Waar gaan we heen? ") 
    if vraag12.lower() == "a":
        vraag13()
    elif vraag12.lower() == "b":
        vraag13()

def vraag13(): 
    vraag13 = input("Hij wilt niet vertellen waar je heen gaat, hij zegt alleen dan we er over een paar dagen zijn. Na 2 zware dagen word je gedropt op een plek. Je vraagt je af waar je bent. \n  A) Je zoekt een bord \n B) Je vraagt het aan de mensen om je heen ") 
    if vraag13.lower() == "a":
        print("Je komt erachter dat je in urk bent. Je zit hier je hele leven vast.")
        restart()
    elif vraag13.lower() == "b":
        print("Je komt erachter dat je in urk bent. Je zit hier je hele leven vast.")
        restart()

def vraag14(): 
    vraag14 = input("je bent nu bij een groep rebellen aangesloten. Wat voor training wil je? \n A) Schiet cursus \n B) Medische cursus ") 
    if vraag14.lower() == "a":
        vraag15()
    elif vraag14.lower() == "b":
        vraag16()

def vraag15(): 
    vraag15 = input("In de afgelopen 3 weken heb je een schutters course gedaan. Je word nu op missie gestuurd. Een van jouw troepen is ondervuur. \n A) Laat hem aan ze lot over. \n B) Probeer hem te redden. ") 
    if vraag15.lower() == "a":
        print("Je laat hem aan ze lot over en jij rent weg. Je word gevangen door de taliban en ze martelen je tot je dood. ")
        vraag14()
    elif vraag15.lower() == "b":
        print("Tijdens het redden word je in je borstkast geschoten. Je hebt hem wel gered. je gaat terug naar het kamp")
        vraag16()

def vraag16(): 
    vraag16 = input("Je hebt de afgelopen 2 weken een medisch course gedaan. na een paar mensen geholpen te hebben bied iemand je aan om te vluchten, omdat de oorlog verloren lijkt te zijn. \n A) Je weigert zijn aanbod \n B) Je accepteerd zijn aanbod ") 
    if vraag16.lower() == "a":
        print("Je blijft je kamp word overgenomen en je word bruut doodgeschoten.")
        vraag15()
    elif vraag16.lower() == "b":
        print("Je vlucht met hem mee naar nederland, je woont in bij zijn familie todat je zelf een huis kan kopen en een gezin start.")
        restart()

def vraag17(): 
    vraag17 = input("Je besluit niet mee te gaan, je hebt veel honger. Ga je zelf eten maken of haal je het ergens \n A) halen \n B) zelf maken ") 
    if vraag17.lower() == "a":
        vraag18()
    elif vraag17.lower() == "b":
        vraag19()

def vraag18(): 
    vraag18 = input("Wat wil je maken? \n A) Eitje op brood \n B) Pannekoeken ") 
    if vraag18.lower() == "a":
        print("Je hebt je eten op en je wilt verder gaan met vluchten. Je pakt de bus naar het strand. Je komt de smokelaars weer tegen en besluit toch met ze mee te gaan. ")
        vraag12()
    elif vraag18.lower() == "b":
        vraag12()

def vraag19(): 
    vraag19 = input("Wat wil je halen? \n A) patat \n B) pizza ") 
    if vraag19.lower() == "a":
        vraag20()
    elif vraag19.lower() == "b":
        vraag21()

def vraag20(): 
    vraag20 = input("Welke saus wil je erbij? \n A) mayo \n B) ketchup") 
    if vraag20.lower() == "a":
        print("Je hebt je eten op en je wilt verder gaan met vluchten. Je pakt de bus naar het strand. Je komt de smokelaars weer tegen en besluit toch met ze mee te gaan. ")
        vraag12()
    elif vraag20.lower() == "b":
        print("Je hebt je eten op en je wilt verder gaan met vluchten. Je pakt de bus naar het strand. Je komt de smokelaars weer tegen en besluit toch met ze mee te gaan. ")
        vraag12()

def vraag21(): 
    vraag21 = input("Wat voor pizza wil je halen? \n A) pizza salami \n B) pizza margherita ") 
    if vraag21.lower() == "a":
        print("Je hebt je eten op en je wilt verder gaan met vluchten. Je pakt de bus naar het strand. Je komt de smokelaars weer tegen en besluit toch met ze mee te gaan. ")
        vraag12()
    elif vraag21.lower() == "b":
        print("Je hebt je eten op en je wilt verder gaan met vluchten. Je pakt de bus naar het strand. Je komt de smokelaars weer tegen en besluit toch met ze mee te gaan. ")
        vraag12()

def restart():
    restart = input("Wil je nog een keer spelen? \n A) ja \n B) nee ") 
    if restart.lower() == "a":
        vraag1()
    elif restart.lower() == "b":
        print("doei!")

vraag1()