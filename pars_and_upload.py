import pubg_esports_gamepedia
import lol_gamepedia
import toornamentOW
import wcs_starcraft
import LOL_uploader
import OW_uploader
import PUBG_uploader
print('pubg gamepedia parsing')
pubg_esports_gamepedia.parse()
print('lol gamepedia parsing')
lol_gamepedia.parse()
print('toornament OW parsing')
toornamentOW.parse()
print('wcs_starcraft parsing')
wcs_starcraft.parse()
print('LOL upload')
LOL_uploader.upload()
print('OW upload')
OW_uploader.upload()
print('pubg upload')
PUBG_uploader.upload()
