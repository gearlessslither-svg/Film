# 投币口 / 01_AIGC WAV 生成与整轨装配计划 v1

## 输入表

- 对白和语音：`exports/dialogue_voice_assets.csv`
- 音效和音乐：`exports/sound_music_cue_sheet.csv`
- 总轨装配：`exports/audio_assembly_manifest.csv`

## 文件夹

| folder | content |
|---|---|
| `audio/voice_clean/` | clean generated dialogue WAVs |
| `audio/voice_processed/` | phone/system/walla/processed voice WAVs |
| `audio/ambience/` | loopable location beds |
| `audio/sfx/` | foley, hard SFX, transition SFX, designed silence WAVs |
| `audio/music/` | music/source-music stems |
| `audio/mix/` | guide and final assembled WAVs |

## 生成顺序

1. 生成 A 级 dialogue voice WAV。
2. 生成 A 级 ambience/SFX/music WAV。
3. 用 assembly manifest 先做 `coin_slot_audio_guide_v001.wav`。
4. 生成 B 级补充声音。
5. 等视频实际时长确定后输出 `coin_slot_audio_final_v001.wav`。

## 总轨要求

- 采样率建议 48kHz，24-bit 或 float 工作流。
- 台词干声不烘焙音乐。
- 系统声和电话声可以单独处理后再进总轨。
- guide mix 允许粗糙，但时间点必须能对上 MSB 和 Clip。

## 当前已生成 guide 资产

- 本机可用中文 TTS：`Microsoft Huihui Desktop`。已用于生成可对时的 dialogue guide WAV；这不是最终儿童表演级配音。
- 程序化 guide 声音脚本：`tools/build_audio_guide.py`
- 已生成总轨：`audio/mix/coin_slot_audio_guide_v001.wav`
- 总轨规格：48kHz stereo，约 351 秒。
- 后续正式版需要替换：儿童/少年真实表演、游戏厅人群、真实 foley、街机 UI、电话声和音乐 stem。
