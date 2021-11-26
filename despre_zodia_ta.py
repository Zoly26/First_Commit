
# un program folosind variabile, conditii, functii


zodia_ta = ['berbec', 'taur', 'gemeni', 'rac', 'leu', 'fecioara', 'balanta', 'scorpion', 'sagetator', 'capricorn', 'varsator', 'pesti']

name = input("Care este zodia ta: ")

while name in zodia_ta:
    if name == 'berbec':
        print("Berbecul este nascut sub semnul celor curajosi, dinamici, plini de initiativa si spirit de combativitate.")
        break
    elif name == 'taur':
        print("Taurul are un puternic simt al securitatii materiale, fiind stabil din fire, cu picioarele pe pamant, armonios, afectuos si loial.")
        break
    elif name == 'gemeni':
        print("Gemenii au o minte ascutita si o inteligenta sclipitoare, in permanenta activitate mentala. Sunt fericiti numai cand sunt coplesiti de activitati diverse si cand acumuleaza mereu cunostinte si informatii noi.")
        break
    elif name == 'rac':
        print("Racul are o fire timida, sensibila, emotiva, care se bazeaza exclusiv pe emotii si sentimente. Este o persoana vulnerabila, influentabila, cautand adapost intr-o carapace in care se ascunde de unul singur.")
        break
    elif name == 'leu':
        print("Leul este puternic, activ, mereu deschis pentru orice activitate si intotdeauna cu zambetul pe buze cand toate ii merg bine.")
        break
    elif name == 'fecioara':
        print("Fecioara abordeaza viata din punct de vedere practic, cu obiectivitate si spirit analitic. Are o fire modesta, tacuta, constiincioasa, chiar pasiva uneori, incat s-ar putea sa nu i se ofere intotdeauna toata increderea pe care o merita.")
        break
    elif name == 'balanta':
        print("Balanta este diplomata, amabila, sociabila si prietenoasa. Are un dezvoltat simt de fair-play, incat nu va rani niciodata pe nimeni, ci va incerca sa impace pe toata lumea.")
        break
    elif name =='scorpion':
        print("Personalitatea Scorpionului este magnetica, misterioasa, carismatica, atragandu-i pe toti in jurul sau ca un magnet.")
        break
    elif name == 'sagetator':
        print("Sagetatorul nu este o fire facila, tocmai pentru ca este un individ cu o personalitate puternica, independenta, greu de supus, in permanenta miscare si activitate.")
        break
    elif name == 'capricorn':
        print("Zodia Capricorn reprezinta intelepciunea si maturitatea, este semnul telului greu de atins si al ambitiei. Cel nascut in Capricorn are un aer sobru, trist uneori, dand impresia ca ar fi o persoana cu multa experienta de viata.")
        break
    elif name == 'varsator':
        print("Varsatorul este creativ, independent si detasat, detinator a nenumarate calitati deosebite. Este inteligent si, in multe privinte, un excentric, pentru ca nimic din ceea ce face nu este obisnuit.")
        break
    elif name == 'pesti':
        print("Pestii sunt idealisti, cu o sensibilitate exagerata, romantici si visatori, mereu in cautarea unui sfat de la cineva, deoarece le lipseste increderea si siguranta in fortele proprii.")   
        break    
    
else:
    print("Aceasta zodie nu exista pe planeta noastra. . . . . . . ")