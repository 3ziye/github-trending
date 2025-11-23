# Step-Audio-EditX
<p align="center">
  <img src="assets/logo.png"  height=100>
</p>

<div align="center">
    <a href="https://stepaudiollm.github.io/step-audio-editx/"><img src="https://img.shields.io/static/v1?label=Demo%20Page&message=Web&color=green"></a> &ensp;
  <a href="https://arxiv.org/abs/2511.03601"><img src="https://img.shields.io/static/v1?label=Tech%20Report&message=Arxiv&color=red"></a> &ensp;
  <a href="https://huggingface.co/stepfun-ai/Step-Audio-EditX"><img src="https://img.shields.io/static/v1?label=Step-Audio-EditX&message=HuggingFace&color=yellow"></a> &ensp;
    <a href="https://modelscope.cn/models/stepfun-ai/Step-Audio-EditX"><img src="https://img.shields.io/static/v1?label=Step-Audio-EditX&message=ModelScope&color=blue"></a> &ensp;
  <a href="https://huggingface.co/spaces/stepfun-ai/Step-Audio-EditX"><img src="https://img.shields.io/static/v1?label=Space%20Playground&message=HuggingFace&color=yellow"></a> &ensp;
</div>

## 🔥🔥🔥 News!!
* Nov 19, 2025: ⚙️ We release a **new version** of our model, which **supports polyphonic pronunciation control** and improves the performance of emotion, speaking style, and paralinguistic editing.
* Nov 12, 2025: 📦 We release the **optimized inference code** and **model weights** of **Step-Audio-EditX** ([HuggingFace](https://huggingface.co/stepfun-ai/Step-Audio-EditX);  [ModelScope](https://modelscope.cn/models/stepfun-ai/Step-Audio-EditX)) and **Step-Audio-Tokenizer**([HuggingFace](https://huggingface.co/stepfun-ai/Step-Audio-Tokenizer);  [ModelScope](https://modelscope.cn/models/stepfun-ai/Step-Audio-Tokenizer))
* Nov 07, 2025: ✨ [Demo Page](https://stepaudiollm.github.io/step-audio-editx/) ; 🎮  [HF Space Playground](https://huggingface.co/spaces/stepfun-ai/Step-Audio-EditX)
* Nov 06, 2025: 👋 We release the technical report of [Step-Audio-EditX](https://arxiv.org/abs/2511.03601).

## Introduction
We are open-sourcing Step-Audio-EditX, a powerful **3B-parameter** LLM-based **Reinforcement Learning** audio model specialized in expressive and iterative audio editing. It excels at editing emotion, speaking style, and paralinguistics, and also features robust zero-shot text-to-speech (TTS) capabilities. 

## 📑 Open-source Plan
- [x] Inference Code
- [x] Online demo (Gradio)
- [ ] Step-Audio-Edit-Benchmark
- [x] Model Checkpoints
  - [x] Step-Audio-Tokenizer
  - [x] Step-Audio-EditX
  - [ ] Step-Audio-EditX-Int4
- [ ] Training Code
  - [ ] SFT training
  - [ ] PPO training
- [ ] ⏳ Feature Support Plan
  - [ ] Editing
    - [x] Polyphone pronunciation control
    - [ ] More paralinguistic tags ([Cough, Crying, Stress, etc.])
    - [ ] Filler word removal
  - [ ] Other Languages
    - [ ] Japanese, Korean, Arabic, French, Russian, Spanish, etc.
  
## Features
- **Zero-Shot TTS**
  - Excellent zero-shot TTS cloning for Mandarin, English, Sichuanese, and Cantonese.
  - To use a dialect, just add a **[Sichuanese]** or **[Cantonese]** tag before your text.
  - 🔥 Polyphone pronunciation control, all you need to do is replace the polyphonic characters with pinyin.
    - **[我也想过过过儿过过的生活]** -> **[我也想guo4guo4guo1儿guo4guo4的生活]**
 
    
- **Emotion and Speaking Style Editing**
  - Remarkably effective iterative control over emotions and styles, supporting **dozens** of options for editing.
    - Emotion Editing : [ *Angry*, *Happy*, *Sad*, *Excited*, *Fearful*, *Surprised*, *Disgusted*, etc. ]
    - Speaking Style Editing: [ *Act_coy*, *Older*, *Child*, *Whisper*, *Serious*, *Generous*, *Exaggerated*, etc.]
    - Editing with more emotion and more speaking styles is on the way. **Get Ready!** 🚀
    

- **Paralinguistic Editing**
  -  Precise control over 10 types of paralinguistic features for more natural, human-like, and expressive synthetic audio.
  - Supporting Tags:
    - [ *Breathing*, *Laughter*, *Suprise-oh*, *Confirmation-en*, *Uhm*, *Suprise-ah*, *Suprise-wa*, *Sigh*, *Question-ei*, *Dissatisfaction-hnn* ]

- **Available Tags**
<table>
  <tr>
    <td rowspan="8" style="vertical-align: middle; text-align:center;" align="center">emotion</td>
    <td align="center"><b>happy</b></td>
    <td align="center">Expressing happiness</td>
    <td align="center"><b>angry</b></td>
    <td align="center">Expressing anger</td>
  </tr>
  <tr>
    <td align="center"><b>sad</b></td>
    <td align="center">Expressing sadness</td>
    <td align="center"><b>fear</b></td>
    <td align="center">Expressing fear</td>
  </tr>
  <tr>
    <td align="center"><b>surprised</b></td>
    <td align="center">Expressing surprise</td>
    <td align="center"><b>confusion</b></td>
    <td align="center">Expressing confusion</td>
  </tr>
  <tr>
    <td align="center"><b>empathy</b></td>
    <td align="center">Expressing empathy and understanding</td>
    <td align="center"><b>embarrass</b></td>
    <td align="center">Expressing embarrassment</td>
  </tr>
  <tr>
    <td align="center"><b>excited</b></td>
    <td align="center">Expressing excitement and enthusiasm</td>
    <td align="center"><b>d