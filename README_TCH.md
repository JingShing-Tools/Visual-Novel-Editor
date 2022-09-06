
# Manual

# Visual-Novel-Editor

[English](https://github.com/JingShing/Visual-Novel-Editor/blob/main/README.md) | 繁體中文

一個自我[對話編輯器](https://github.com/JingShing/Pygame-Dialogue-Editor)衍生的作品。 遊戲小說風格。

你可以在 Itch.io 取得打包好的版本 : https://jingshing.itch.io/visualnovelmaker

一款樣板遊戲可以在 itch.io 取得 : https://jingshing.itch.io/crt-prison

RainyCity雨都 使用這款工具開發，可以在 itch.io 取得 : https://jingshing.itch.io/raincity

根據pygame開發。

你可以更改角色頭像。

我愛這個專案，我增加了指令系統。它可以讓你更簡單的運行每一行指令和操作。

按 'T' 說話

按 'enter' 繼續對話

按 'F' 全屏

按 '0' 更改濾鏡 -> 目前有CRT電視濾鏡、掃描線和沒有濾鏡。

備注： 如果你想使用這工具，但不知道怎麼寫指令，可以參考我的腳本 : https://github.com/JingShing/Visual-Novel-Scripts


## 對話格式(p 和 n 可以表示 player玩家 和 npcs非玩家角色):
---

'講者:對話' 讓系統知道是誰在說話。

現在能讓玩家和非玩家角色對話，更多自定義內容請等待更新。

每個講者的字體將在未來版本可自定義。


## 指令系統(所有指令都使用 @ 作為開頭語句。 且 p 或 n 可以表示 player玩家 或 npcs非玩家角色):
---

如果你使用編輯器自帶的edit，而編輯框中是空格，將觸發特殊效果：如果你選中了對話列表的台詞，將會刪除此台詞；如果沒有選中特定台詞則會刷新台詞列表。

- '@p.img=n' -> 玩家頭像替換成npc頭像。

- '@bg=img' -> 更改背景成特定圖片。

- '@get' -> 如果在編輯框輸入這指令，並點擊edit，則可以得到當前選中對話列表的對話。

- '@copy' -> 如果編輯框輸入這指令，並點擊add line，可以把選中行複製到選中行的下一行。

- '@bgm=bgm_name' -> 更改bgm到 assets/audio/bgm/bgm_name.mp3

- '@player=name' -> 增加一個角色到玩家角色清單。可以使用這指令增加角色。

- 備注： 你可能需要使用 'name.img=p' 來給自定義角色一張頭像。

- '@player=clear' -> 清空玩家列表。

- '@npc=name' -> 增加角色到npc列表

- 備注： 你可能需要使用 'name.img=n' 給它一個頭像。

- '@npc=clear' -> 清空npc清單

- '@end' -> 使用這個在腳本結尾處，告訴系統這邊結束。

- '@sceneX' -> 你需要在X放數字，放在劇本中，和編輯器說哪裡是場景幾。

- '@delay=X' -> 你需要把 X 放個數字告訴編輯器延遲多少。預設是 35。

- ':@' -> 如果你想在對話印出 '@' 只需要在前面加個 ':'。

## Update更新

### ver 0.2

- 新增編輯框指令
  現在有一個指令 ':' 可以知道哪個角色說話。
  範例:
  玩家:台詞
  npc:台詞
- 你可以用縮寫:
  p:台詞
  n:台詞
- 如果你不使用 ':' 來指定角色。 系統會預設為npc說的話。
  現在npc用黑色說話，玩家用紅色。
- 新增台詞機制升級。台詞會新增在選定台詞的後面。
- 更改台詞系統更新。
  範例-> 'n:hello'
  如果只打 'p:' : 台詞只會更改講者 -> 'p:hello'
  如果只打 'line' : 只有台詞會被更新 -> 'n:line'
  如果輸入 'p:line' : 整行會被更改 -> 'p:line'

### ver0.3

- 可以更改圖片了.
  使用 '@' 指令:

範例->

```
'@n.img=p' -> 更改 npc 的圖片為玩家的圖片
'@npc.img=player' -> 和上行同理
新增多重背景控制
```

- 新增 '@bg=name' 指令
  可以使用 @bg=name 更改為同名的背景圖片。
- 新增 '@copy' 指令
  如果你輸入 @copy 到編輯框然後點擊add line按扭。 它會複製你選中的行到選中行的下一行。
- 新增 '@get' 指令
  輸入到編輯框，然後點擊edit line，可以得到選中行的文字。

### ver0.4

- 新增 '@bgm=bgm_name' 指令

- '@bgm=bgm_name' 可以把bgm更改成audio/bgm資料夾中的bgm

### ver0.5

- 新增多語言切換功能
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

