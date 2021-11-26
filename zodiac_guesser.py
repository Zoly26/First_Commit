zodii = ['berbec', 'taur', 'gemeni', 'rac', 'leu', 'fecioara', 'balanta', 'scorpion', 'sagetator', 'capricorn', 'varsator', 'pesti']
dates = input("In ce zi te-ai nascut? ")
month = input("\nIn ce luna te-ai nascut? ")

if month == 'martie' and dates >= '21' and dates <= '31' or month == 'aprilie' and dates >= '1' and dates <= '20':
    print("Esti in zodia " + zodii[0].title() + '.')

elif month =='aprilie' and dates >= '21' and dates <= '30' or month == 'mai' and dates >= '1' and dates <= '21':
    print("Esti in zodia " + zodii[1].title() + '.')

elif month == 'mai' and dates >= '22' and dates <= '31' or month == 'iunie' and dates >= '1' and dates <= '21':
    print("Esti in zodia " + zodii[2].title() + '.')

elif month == 'iunie' and dates >= '22' and dates <= '30' or month == 'iulie' and dates >= '1' and dates <= '22':
    print("Esti in zodia " + zodii[3].title() + '.')

elif month == 'iulie' and dates >= '23' and dates <= '31' or month == 'august' and dates >= '1' and dates <= '22':
    print("Esti in zodia " + zodii[4].title() + '.')

elif month == 'august' and dates >= '23' and dates <= '31' or month == 'septembrie' and dates >= '1' and dates <= '21':
    print("Esti in zodia " + zodii[5].title() + '.')

elif month == 'septembrie' and dates >= '22' and dates <= '30' or month == 'octombrie' and dates >= '1' and dates <= '22':
    print("Esti in zodia " + zodii[6].title() + '.')

elif month == 'octombrie' and dates >= '23' and dates <= '31' or month == 'noembrie' and dates >= '1' and dates <= '21':
    print("Esti in zodia " + zodii[7].title() + '.')

elif month == 'noembrie' and dates >= '22' and dates <= '30' or month == 'decembrie' and dates >='1' and dates <= '20':
    print("Esti in zodia " + zodii[8].title() + '.')

elif month == 'decembrie' and dates >= '21' and dates <= '31' or month == 'ianuarie' and dates >= '1' and dates <= '19':
    print("Esti in zodia " + zodii[9].title() + '.')

elif month == 'ianuarie' and dates >= '20' and dates <= '31' or month == 'februarie' and dates >= '1'  and dates <= '18':
    print("Esti in zodia " + zodii[10].title() + '.')

elif month == 'februarie' and dates >= '19' and dates <= '28' or month == 'martie' and dates >= '1' and dates <= '20':
    print("Esti in zodia " + zodii[11].title() + '.')

else:
    print(" ?!? ")
