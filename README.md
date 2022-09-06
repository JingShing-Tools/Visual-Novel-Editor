# Manual

# Visual-Novel-Editor

English | [繁體中文](https://github.com/JingShing/Visual-Novel-Editor/blob/main/README_TCH.md)

A derivative of my Dialogue Editor. It's purely a visual novel style

You can get this editor exe now on Itch.io : https://jingshing.itch.io/visualnovelmaker

A sample game based on this editor is available on itch.io : https://jingshing.itch.io/crt-prison

RainyCity based on this tool now available on itch.io : https://jingshing.itch.io/raincity

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

- '@p.img=n' -> player's head image changed to npc's image.

- '@bg=bg' -> change background image to certain image.

- '@get' -> if you using edit line with this command you can get select line on text box.

- '@copy' -> if you using add line with this command you can copy select line to the bottom of select line.

- '@bgm=bgm_name' -> change bgm to the assets/audio/bgm/bgm_name.mp3

- '@player=name' -> add a character to player name list. You can use it to create your own character and use it in script.

- p.s. You may need to use 'name.img=p' to give it a image.

- '@player=clear' -> clear player name list.

- '@npc=name' -> add a character to npc name list.

- p.s. You may need to use 'name.img=n' to give it a image.

- '@npc=clear' -> clear npc name list.

- '@end' -> use it in script to tell editor read to where to end reading.

- '@sceneX' -> you need to put number in X to tell editor what scene is it.

- '@delay=X' -> you need to put X a number to tell editor what conversation delay should be. Default is 35.

- ':@' -> if you want to print '@' in dialogue just add ':' in line.

## Update

### ver 0.2

- add command system in input line.
  now has one command ':' which can refered which line is what character say.
  sample:
  player:line
  npc:line
- you can also use short way:
  p:line
  n:line
- if you don't use ':' to refered character. system will default as npc say.
  now npc use black text color. player use red.
- and now add line system upgrade. line will add next to the line you chose
  in text list box.
- edit line system changed.
  example-> 'n:hello'
  If you only text 'p:' : the line will only change talker -> 'p:hello'
  If you only text 'line' : the line will only change text -> 'n:line'
  If you text 'p:line' : the line will all change -> 'p:line'

### ver0.3

- can change img now.
  using '@' command:

examples->

```
'@n.img=p' -> change npc's image to player
'@npc.img=player' -> change npc's image to player
add multi bg control
```

- add '@bg=name' command
  can use @bg=name to change bg to the name level had bg name.
- add '@copy' command
  if you type @same and click add line button. It will copy the line
  you select in list. and add same line under it.

- add '@get' command
  use edit line to get the line select

### ver0.4

- add '@bgm=bgm_name' command

- '@bgm=bgm_name' will change bgm into bgm in audio folder.

### ver0.5

- add multilang change function.
- add new function in level -> change_line_script(self, script_name) :
  can import script and multilangs script into game

### ver0.6

- add custom player name and custom npc name
- bug:edit line feature kinda broke
- fixed:level.language_change func init the lines
- add new command in script : 
  '@player=name' and '@npc=name' will add name to list and can refer as character name.
  example -> '@player=JingShing' character will named JingShing.
  and you need to use custom name to write lines
  name:line instead of player:line

- '@player=clear' or '@npc=clear' will clear name list

- add multi character icon system. It will add a new key to dict
  to recognize what custom name should be used what image.
  In default if you create a new name. default will set image to 'none'.
  you need to use '@name.img=p' to change img.

- add flag feature. You can now write all scene in one script.
  You just need to add '@end' to note the end of scene.
  And use '@scene name' to add flag to different stages.

- add new way to add images. If you want to add a new image for your game.
  Just put image into 'assets/graphics/characters/' or 'assets/graphics/stages/'
  System will automatically sort into dict for you. Now can only differ 'png' and 'png' format.
  it will be like 'image.png' -> dict = {'image' : surface('image.png')}

- fixed : @bg command change bg slower than command order

- add auto classify bgm system

- now can make people say '@'

- add '@delay' command to control dialogues speed.

- to do: add custom flag instead of 'scene num'


### ver 0.7

- bug: no dialogue in folder fault
  fixed
- add '@name.color=color' command to change text color
  now switching character will refresh text.

- add a config file can modify helper window, title screen text and dialogue file name default.

- add new feature you can now just define talker name onece than just add text.

example->

```
n:text
text
text
```

same as

```
n:text
n:text
n:text
```

### ver 0.8

- now switching character will refresh text page.


- add config system:
  - need_help=True
  - // open window or not
  - title_screen_text=Game
  - // set game title
  - window_caption=Still_loading:
  - // set game caption
  - dialogue_file_name=default
  - // default dialogue file name
  - shader_default=2
  - // shader default: 0, no shader. 1 crt shader. 2 scanline.
  - default_lang=english
  - // now has english, schinese, tchinese
  - ending=Nothing there
  - // ending line

### ver 0.9

- add resolution and window size in config
- add text frame alpha in config
- remove switching character refresh text box
- add new command '@refresh' to refresh textbox

- add '@textbox.alpha=X' command to change alpha value of textbox
- add '@textbox.color=X,X,X' command to change color
- add new mode of '@color' command you can use color name or rgb value


- add attribute to config:
  - resolution=800,600
  - window_size=800,600
  - allow_img_format=png,jpg,bmp
  - text_frame_alpha=255
  - text_frame_color=255,255,255

### ver 0.91

fixed '@refresh' command bug

### ver 0.92

- now can use shift to speed coversation

- fixed textbox alpha range problem

- add '@jump tag' command
  you need to use '@tag' first

- press 'U' to switch cpu render or gpu render


### ver 0.93

- press 'shift' to speed up

- add '@jump file tag'

- update sound system now can auto detect sound effect

- you can now using '#' in dialogues script to make comment

- \# can't put jump after refresh since jump has refresh func
  \# fixed. refresh and jump command conflit fixed.

- if you need narration you can use 'none:' to talk

- now textbox no longer fliker

### ver 0.94

- add config: ending_bg and ending_bgm
- add delay between refresh(you can use shift to speed up)
- fixed:'@jump tag' and '@scene' feature can't use in other language. fixed.
- add '@optionX=text' command
  you can use '@option.text=text', '@option.command=command', '@option.clear' now
- edit:'@option.command' == '@option.com' -> '@option.com=command' it would
  put @ in command
- fixed: jump will eat command.

- removed most crt_shader.render to avoid flicker. only keep main and dialog.
  to update screen.
- bug:can't put select and lines after refresh
- fixed:use add line to fix bug
- fixed:jump failed add weird line in wrong place
- fixed:save_file.txt bug fixed.
- add option menu -> can edit render mode and language by gui now.


### ver0.95

- custom available languages in config
- now every chracter image only need facing right. NPC type will flip.
- update shader class

## Up to do

- [ ] 存檔功能
- [ ] 角色動畫
- [ ] 手柄支持
- [ ] 移植

## Done

- [x] 多分支
- [x] 選項指令
- [x] JUMP指令
- [x] config hint, menu, intro_bgm
- [x] 自訂音效
- [x] typing時的音效
- [x] character.voice=voice
- [x] fix jump will eat command
- [x] option flicker problem
- [x] long sentence will broke select
- [x] need to fix text flicker problem

