# Visual-Novel-Editor
A derivative of my Dialogue Editor. It's purely a visual novel style

A game based on this editor is available on itch.io : https://jingshing.itch.io/crt-prison

It's based on pygame.

You can change npc image and bg.

I love this project. I add a command system in that. So it can easily process the act or line I want.

press 'T' to talk.

press 'enter' to continue dialogue.

press 'F' to fullscreen.

press '0' to change filter. -> now has crt tv, scan line and no filter.

p.s. If you want to use this visual novel maker and don't know how to write a dialogue script with command. can look my scripts
on here : https://github.com/JingShing/Visual-Novel-Scripts

dialogue format(p or n can represent player and npcs):
---

'talker:line' to make system know who is talked now and can using right text color, text font and text size.

Now only has player and npc two type talker. Custom talker type will be update in the future version.

Every talkers' text style can be changed in future edition.

commands(all using @ forehead. and p or n can represent player and npcs):
---

if you use edit and text box is empty will trigger special effect.

if you select line with this action will delete line. And if you didn't select line will refresh line list.

'@p.img=n' -> player's head image changed to npc's image.

'@bg=bg' -> change background image to certain image.

'@get' -> if you using edit line with this command you can get select line on text box.

'@copy' -> if you using add line with this command you can copy select line to the bottom of select line.

'@bgm=bgm_name' -> change bgm to the assets/audio/bgm/bgm_name.mp3

'@player=name' -> add a character to player name list. You can use it to create your own character and use it in script.

'@player=clear' -> clear player name list.

'@npc=name' -> add a character to npc name list.

'@npc=clear' -> clear npc name list.

'@end' -> use it in script to tell editor read to where to end reading.

'@sceneX' -> you need to put number in X to tell editor what scene is it.

'@delay=X' -> you need to put X a number to tell editor what conversation delay should be. Default is 35.

':@' -> if you want to print '@' in dialogue just add ':' in line.

```
ver 0.2
add command system in input line.
now has one command ':' which can refered which line is what character say.
sample:
player:line
npc:line

you can also use short way:
p:line
n:line

if you don't use ':' to refered character. system will default as npc say.
now npc use black text color. player use red.

and now add line system upgrade. line will add next to the line you chose
in text list box.

edit line system changed.
example-> 'n:hello'
If you only text 'p:' : the line will only change talker -> 'p:hello'
If you only text 'line' : the line will only change text -> 'n:line'
If you text 'p:line' : the line will all change -> 'p:line'

ver0.3
can change img now.
using '@' command:
examples->
'@n.img=p' -> change npc's image to player
'@npc.img=player' -> change npc's image to player
add multi bg control

add '@bg=name' command
can use @bg=name to change bg to the name level had bg name.

add '@copy' command
if you type @same and click add line button. It will copy the line
you select in list. and add same line under it.

add '@get' command
use edit line to get the line select

ver0.4
add '@bgm=bgm_name' command
'@bgm=bgm_name' will change bgm into bgm in audio folder.

ver0.5
add multilang change function.
add new function in level -> change_line_script(self, script_name) :
can import script and multilangs script into game

ver0.6
add custom player name and custom npc name
bug:edit line feature kinda broke
fixed:level.language_change func init the lines

add new command in script : 
'@player=name' and '@npc=name' will add name to list and can refer as character name.
example -> '@player=JingShing' character will named JingShing.
and you need to use custom name to write lines
name:line instead of player:line

'@player=clear' or '@npc=clear' will clear name list

add multi character icon system. It will add a new key to dict
to recognize what custom name should be used what image.
In default if you create a new name. default will set image to 'none'.
you need to use '@name.img=p' to change img.

add flag feature. You can now write all scene in one script.
You just need to add '@end' to note the end of scene.
And use '@stage name' to add flag to different stages.

add flag feature. You can now write all scene in one script.
You just need to add '@end' to note the end of scene.
And use '@stage name' to add flag to different stages.

add new way to add images. If you want to add a new image for your game.
Just put image into 'assets/graphics/characters/' or 'assets/graphics/stages/'
System will automatically sort into dict for you. Now can only differ 'png' and 'png' format.
it will be like 'image.png' -> dict = {'image' : surface('image.png')}
```
