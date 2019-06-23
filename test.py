import lol_gamepedia as LG
import lol_gamepedia_Extention as LGE
import pubg_esports_gamepedia as PG
import pubg_esports_gamepedia_Exception as PGE
import toornamentOW as TO
import toornamentOW

a = input()
if a == '1':
    LG.parse()
elif a == '1.5':
    print(LGE.parse(
        'https://lol.gamepedia.com/Liga_Master_Fibertel/2019_Season/Closing_Season'))
elif a == '2':
    PG.parse()
elif a == '2.5':
    print(PGE.parse(
        'https://pubg-esports.gamepedia.com/PUBG_Master_League/2019_Season/Phase_1/Finals'))
elif a == '3':
    TO.parse()
