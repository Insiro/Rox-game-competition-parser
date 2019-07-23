import pubg_esports_gamepedia
import lol_gamepedia
import toornamentOW
import LOL_uploader
print('pubg gamepedia parsing')
pubg_esports_gamepedia.parse()
print('lol gamepedia parsing')
lol_gamepedia.parse()
print('toornament OW parsing')
toornamentOW.parse()
print('upload')
LOL_uploader.upload()
