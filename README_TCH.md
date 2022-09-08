
# Manual

# Visual-Novel-Editor

[English](https://github.com/JingShing/Visual-Novel-Editor/blob/main/README.md) | 繁體中文

一個自我[對話編輯器](https://github.com/JingShing/Pygame-Dialogue-Editor)衍生的作品。 遊戲小說風格。

打包好的[視覺小說製作大師](https://jingshing.itch.io/visualnovelmaker)

使用這個工具開發的遊戲
* [CRT監獄(樣品)](https://jingshing.itch.io/crt-prison)

* [RainyCity雨都](https://jingshing.itch.io/raincity)

根據pygame開發。

你可以更改角色頭像。

我愛這個專案，我增加了指令系統。它可以讓你更簡單的運行每一行指令和操作。

按 'T' 說話

按 'enter' 繼續對話

按 'F' 全屏

按 '0' 更改濾鏡 -> 目前有CRT電視濾鏡、掃描線和沒有濾鏡。

備注： 如果你想使用這工具，但不知道怎麼寫指令，可以參考[我的腳本](https://github.com/JingShing/Visual-Novel-Scripts)


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
- 在 level 腳本新增函數 -> change_line_script(self, script_name) :
  可以導入不同腳本到遊戲中

### ver0.6

- 新增自訂玩家和NPC名字功能。
- bug:edit line 功能損壞
- fixed:level.language_change func init the lines
- 在腳本編寫處新增指令 : 
  '@player=name' 和 '@npc=name' 會把名字加到對應的清單中
  範例 -> '@player=JingShing' 玩家清單中會添加名為 JingShing 的角色
  之後要直接用角色名寫對話
  * -> name:line 而不是 player:line

- '@player=clear' 和 '@npc=clear' 會把名字清單清除

- 新增角色頭像管理系統。會添加鍵值到字典
  * 用以紀錄角色名和對應頭像
  預設你創建角色，角色頭像會設為：'none'
  你需要用 '@name.img=p' 以更改圖像

- 新增 Flag標誌 功能。可以增加標誌到腳本中，讓同一個腳本有不同的場景搭配
  你只需要在場景最後添加 '@end' 作為標記場景結尾
  並在開頭加上 '@scene name' 做為不同場景的標記

- 新增導入圖片的方法。如果想添加新的圖片素材
  只要把圖片放在 'assets/graphics/characters/' 和 'assets/graphics/stages/'
  系統會幫你自動分類成字典。現在只能分辨 'png' 和 'png' 格式
  運作原理類似： 'image.png' -> dict = {'image' : surface('image.png')}

- fixed : @bg 指令更換背景順序較慢問題修復

- 新增自動分類BGM系統

- 現在角色可以說出 '@' 字符了

- 新增 '@delay' 指令，控制對話速度

- to do: 新增自定義場景標誌，而不是舊方法 'scene num'


### ver 0.7

- bug: 沒有腳本於資料夾報錯
  fixed 已修復
- 新憎 '@name.color=color' 指令，用以編輯對話顏色
  現在更換角色會刷新對話

- 新增 config配置 檔案可以自訂 helper window, title screen text標題文字 和腳本名稱預設

- 可以不用在每一句開頭增加講者名稱，而是沿用上一位提及的講者。

範例->

```
n:text
text
text
```

等同於

```
n:text
n:text
n:text
```

### ver 0.8

- 現在更換角色會清空對話框

- 新增 config配置 系統:
  - need_help=True
  - // 編輯視窗開啟與否
  - title_screen_text=Game
  - // 設定遊戲開頭標題
  - window_caption=Still_loading:
  - // 設定視窗標題
  - dialogue_file_name=default
  - // 預設腳本檔案名稱
  - shader_default=2
  - // shader取色器，預設: 0, 無濾鏡. 1 crt 濾鏡. 2 掃描線.
  - default_lang=english
  - // 現在可選的語言 english, schinese, tchinese
  - ending=Nothing there
  - // 結尾語句
- config 是 空格敏感的(space-sensitive)

### ver 0.9

- 於設置檔新增螢幕解析度和視窗大小屬性
- 於設置檔新增對話框透明度設定
- 去除切換角色清空對話框功能
- 新增腳本指令 '@refresh' 清空對話框

- 新增 '@textbox.alpha=X' 指令，更改對話框透明度
- 新增 '@textbox.color=X,X,X' 指令，用以指定RGB
- 新增 '@color' 指令新模式：你可以使用顏色名或RGB數值更改顏色


- 新增配置檔案屬性:
  - resolution=800,600
  - // 解析度
  - window_size=800,600
  - // 視窗尺寸
  - allow_img_format=png,jpg,bmp
  - // 允許的圖片格式
  - text_frame_alpha=255
  - // 對話框透明度
  - text_frame_color=255,255,255
  - // 對話框顏色(RGB)

### ver 0.91

修復 '@refresh' 指令的錯誤

### ver 0.92

- 現在可以透過按 'shift' 加速對話

- 修復對話框透明度範圍問題

- 新增 '@jump tag' 指令，可以跳到指定標記
  需要先使用 '@tag' 製造標記

- 按 'U' 切換渲染方式(GPU或CPU)

### ver 0.93

- 按 'shift' 加速

- 新增 '@jump file tag'

- 更新音效系統，可以自動偵測音檔並分類

- 你可以在腳本中使用 '#' 來編寫註解

- \# 無法同時把jump和refresh指令放在一起，因為兩者都有清空對話框功能，所以互斥
  \# 已修復，可以同時放jump和refresh

- 如果需要旁白，可以調用 'none:' 來進行說明

- 現在對話框不再閃爍

### ver 0.94

- 新增配置檔屬性: ending_bg 和 ending_bgm
- 在清框對話框時增加間隔時間(可以使用 shift 來加速)
- 修復 : '@jump tag' 和 '@scene' 功能無法使用在其他語言。已修復。
- 新增 '@optionX=text' 指令，作為對話選項的功能，可以提供不同對話分支
  現在可以使用 '@option.text=text', '@option.command=command', '@option.clear'
- 更改 : '@option.command' == '@option.com' -> '@option.com=command' 他會把command
  中埔全 '@'
- 已修復 : jump 會吃掉指令

- 移除大部分 crt_shader.render 函數避免閃爍。只保留在主模塊和對話模塊更新畫面。
- bug : 無法在refresh後放台詞和對話分支
- 修復 : 使用add line修復bug
- 修復 : jump 失敗後導致台詞出現在奇怪的地方
- 修復 : save_file.txt bug 修復
- 新增選項選單 -> 可以透過選單更改語言和渲染方式

### ver0.95

- 可在配置中自定義可用語言
- 所有角色頭像朝右，只有npc頭像會水平翻轉
- 優化 取色器 模塊

## Up to do 日後待定

- [ ] 存檔功能
- [ ] 角色動畫
- [ ] 手柄支持
- [ ] 移植

## Done

- [x] 多分支
- [x] 選項指令
- [x] JUMP指令
- [x] config 增加 hint, menu, intro_bgm 屬性
- [x] 自訂音效
- [x] typing時的音效
- [x] character.voice=voice
- [x] jump指令會吃掉指令
- [x] 選項閃爍問題
- [x] 修復長句子會把選項弄壞
- [x] 文字閃爍問題

