# Visual-Novel-Editor
A derivative of my Dialogue Editor. It's purely a visual novel style

It's based on pygame.

You can change npc image and bg.

I love this project. I add a command system in that. So it can easily process the act or line I want.

dialogue format(p or n can represent player and npcs):
---

'talker:line' to make system know who is talked now and can using right text color, text font and text size.

Now only has player and npc two type talker. Custom talker type will be update in the future version.

Every talkers' text style can be changed in future edition.

commands(all using @ forehead. and p or n can represent player and npcs):
---

'@p.img=n' -> player's head image changed to npc's image.

'@bg=bg' -> change background image to certain image.

'@copy' -> if you using add line with this command you can copy select line to the bottom of select line.

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
```
