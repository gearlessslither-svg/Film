# Director Semantic Shot Plan V1

项目：县城王家卫 / `county-wkw-night-market-mv`  
类型：音乐 MV，弱剧情，强情绪/强视觉  
建议时长：约 75 秒，可剪成 60-90 秒版本  
版本日期：2026-07-08

## 使用原则

这是导演语义版，不是技术硬切版。每个单元代表一个音乐/情绪段落，后续可以再拆成更细的技术镜头。当前优先保留画面功能、运动方向和情绪递进。

全局硬规则：

- 不生成可读歌词、字幕、店招、品牌或水印。
- 画面提示词继续中英双语。
- AIGC 视频提示词必须写明：只要环境声/音效，不要音乐/BGM/配乐。
- 音乐只在最终剪辑里加入，不交给视频生成模型。
- 不要拍成大都会赛博朋克；每段必须有县城真实物件。

## Rhythm Map

| Unit | Time | Music Function | Emotional Function | Visual Anchor |
|---|---:|---|---|---|
| DS01 | 0-5s | Intro ambience | 进入夜市梦境 | LD001 |
| DS02 | 5-10s | First beat | 男孩锚定 | LD002 |
| DS03 | 10-15s | Hook appears | 女孩第一次回头 | LD003 |
| DS04 | 15-20s | Verse movement | 啤酒摊错身 | LD004 |
| DS05 | 20-25s | Pre-chorus lift | 机车启动，灯光拉长 | LD002/LD005 |
| DS06 | 25-31s | Chorus 1 | 小巷低速跟拍 | LD005 |
| DS07 | 31-37s | Chorus 1 continuation | 镜中同框但隔开 | LD006 |
| DS08 | 37-43s | Breath / pause | 女孩被雨布吞没 | LD003/LD006 |
| DS09 | 43-50s | Chorus 2 opens | 批发市场空旷对望 | LD007 |
| DS10 | 50-55s | Detail pulse | 手、灯泡、湿铬、塑料凳碎片 | LD002/LD003/LD004 |
| DS11 | 55-61s | Ride-out | 离开夜市边缘 | LD005/LD007 |
| DS12 | 61-67s | Outro begins | 田野小路，霓虹变远 | LD008 |
| DS13 | 67-72s | Outro fade | 女孩远去 | LD008 |
| DS14 | 72-75s | Last tail | 男孩停住，梦没说完 | LD008 |

## Units

### DS01 - 夜市入口，梦开始

- Time: 0-5s
- Visual: 雨后夜市入口，湿路反射红绿黄 LED，男孩旧机车从左下低速进入，女孩只是远处雨棚下的背影。
- Camera: 低机位缓慢推进，前景塑料雨布和水珠遮挡。
- Movement cue: 车灯在水坑里拉成长线，摊位灯闪烁。
- Mood reference: `LD001_night_market_entrance.png`
- Production note: 正式关键帧可沿用 LD001 方向，保持无字灯箱。

### DS02 - 男孩和旧机车

- Time: 5-10s
- Visual: 男孩停在廉价 LED 雨棚下，半身靠近旧机车，红绿灯管扫过湿夹克和车身。
- Camera: 轻微手持，从雨布边缘绕进。
- Movement cue: 男孩抬眼看向画外，机车怠速震动。
- Mood reference: `LD002_boy_motorcycle_led_awning.png`
- Production note: 这是男孩 hardlock 的主参考；正式生成前需要 boy face/body lock。

### DS03 - 游戏摊后的女孩

- Time: 10-15s
- Visual: 女孩在灯泡、塑料奖品和玻璃柜后回头，男孩只作为水面里的机车灯出现。
- Camera: 从虚焦灯泡找焦到女孩眼睛。
- Movement cue: 女孩目光扫过镜头，立刻移开。
- Mood reference: `LD003_girl_game_booth_bulbs.png`
- Production note: 这是女孩 hardlock 的主参考；保持成人、真实、非性感化。

### DS04 - 啤酒摊错身

- Time: 15-20s
- Visual: 啤酒箱、塑料凳、烧烤烟中，男孩推车经过，女孩在另一侧转身，两人几乎相遇。
- Camera: 长焦偷拍感，前景椅背和人肩遮挡。
- Movement cue: 烟雾掠过两人，中间被雨布切开。
- Mood reference: `LD004_beer_stall_smoke_crossing.png`
- Production note: 这段容易长伪文字和品牌，正式版要把啤酒箱文字压成纯色块。

### DS05 - 机车启动，夜市变成流光

- Time: 20-25s
- Visual: 男孩重新跨上机车，雨棚灯在车镜和湿铬上碎裂，女孩在背景灯泡里短暂出现。
- Camera: 低角度贴近车身，从车灯推到男孩侧脸。
- Movement cue: 车灯亮起，水面反光突然拉长。
- Mood reference: `LD002_boy_motorcycle_led_awning.png`, `LD005_red_green_alley_ride.png`
- Production note: 后续可生成一张细节 keyframe，专门锁定机车头灯、后视镜和湿铬。

### DS06 - 小巷低速跟拍

- Time: 25-31s
- Visual: 湿小巷红绿反光，男孩载着女孩或女孩贴近画面边缘跟上，速度低，像逃离又像兜风。
- Camera: 低机位跟拍，墙面反光从左向右滑。
- Movement cue: 轮胎压过水，小巷灯牌只保留无字色块。
- Mood reference: `LD005_red_green_alley_ride.png`
- Production note: 第一版 LD005 曾出现可读 `KTV`，正式提示词必须写“无任何字母/汉字”。

### DS07 - 修车铺镜中同框

- Time: 31-37s
- Visual: 修车铺镜子或车窗里，男孩停车，女孩站在匿名彩色灯箱边，两人同在反射里但被红灯分开。
- Camera: 横移穿过镜面/车窗，真实空间和反射空间叠在一起。
- Movement cue: 红霓虹线滑过两人之间。
- Mood reference: `LD006_ktv_repair_shop_reflection.png`
- Production note: 这是全片最适合做“暧昧但不说破”的视觉语法。

### DS08 - 雨布吞没女孩

- Time: 37-43s
- Visual: 女孩从彩灯边走开，被透明雨布、玻璃反射和烟遮住，男孩只能在反光里看到她。
- Camera: 固定或慢推，前景雨布占画面大部分。
- Movement cue: 人影从清晰变成色块，灯泡虚焦。
- Mood reference: `LD003_girl_game_booth_bulbs.png`, `LD006_ktv_repair_shop_reflection.png`
- Production note: 可生成新 keyframe，作为从热闹到空旷的过渡。

### DS09 - 批发市场空旷对望

- Time: 43-50s
- Visual: 空旷批发市场门头，卷帘门关闭，男孩和女孩隔着湿地面站在不同灯色里，机车停在中间。
- Camera: 固定长焦，留大面积湿地反光。
- Movement cue: 灯箱轻闪，人物几乎不动。
- Mood reference: `LD007_wholesale_market_gate.png`
- Production note: 适合作为第二段副歌后的情绪落点。

### DS10 - 记忆碎片

- Time: 50-55s
- Visual: 一组可剪切的细节：湿车镜、手指碰到雨布、灯泡晃动、塑料凳拖过水、啤酒箱反光、女孩侧脸闪过。
- Camera: 快慢混合的特写组，浅景深。
- Movement cue: 跟音乐节奏切，但每个生成视频只做环境声。
- Mood reference: `LD002`, `LD003`, `LD004`
- Production note: 后续可拆成 4-6 张插入 keyframes，不必每张都有完整人物。

### DS11 - 离开夜市边缘

- Time: 55-61s
- Visual: 机车从批发市场/小巷边缘驶出，夜市灯光在后面变成小块，前方变暗。
- Camera: 后跟或侧跟，低速，不要飙车。
- Movement cue: 红绿反光逐渐减少，路灯和蓝黑晨色接管。
- Mood reference: `LD005_red_green_alley_ride.png`, `LD007_wholesale_market_gate.png`
- Production note: 这是从县城人造光到田野晨光的转换段。

### DS12 - 田野小路

- Time: 61-67s
- Visual: 县城外田野小路，湿水泥路、低路灯、水田/玉米地，男孩和旧机车停在路边。
- Camera: 安静长镜头，远处县城霓虹缩成小点。
- Movement cue: 风吹过田野，车身冷却，人物不急。
- Mood reference: `LD008_field_road_before_dawn.png`
- Production note: 这段要压住戏剧化，不拥抱、不喊话。

### DS13 - 女孩远去

- Time: 67-72s
- Visual: 女孩在远处路口或小公交站变成轮廓，慢慢小下去；男孩留在路边。
- Camera: 长焦固定，人物间距变成情绪。
- Movement cue: 女孩轮廓离开一盏路灯光圈。
- Mood reference: `LD008_field_road_before_dawn.png`
- Production note: 适合用非常少的动作，避免模型做大幅表演。

### DS14 - 梦没说完

- Time: 72-75s
- Visual: 男孩背影和旧机车，天色微亮，湿路还留一点县城灯的残光。
- Camera: 固定，留空。
- Movement cue: 男孩没有追，只是停住。
- Mood reference: `LD008_field_road_before_dawn.png`
- Production note: 不要黑屏字幕；结尾靠空镜、背影和环境声收。

## Next Production Needs

Before formal keyframe generation:

1. Generate dedicated boy hardlock sheet.
2. Generate dedicated girl hardlock sheet.
3. Generate dedicated motorcycle hardlock sheet.
4. Convert this director semantic plan into a formal keyframe queue.
5. Only after keyframes are approved, write bilingual image-to-video prompts for each unit.
