<p align="center">
  <img src="assets/figures/mega_asr_logo.png" alt="Mega-ASR Logo" width="15%">
</p>


<h1 align="center">Mega-ASR: Towards In-the-Wild^2 Speech Recognition via Scaling Up Real-world Acoustic Simulation</h1>

<div align="center">
  <a href="https://huggingface.co/papers/2605.19833">
    <img src="assets/huggingface_paper_gold_day.svg"/>
  </a>
</div>

We introduce **MEGA-ASR**, the first foundation ASR model to target **full-scenario robust speech recognition in the wild** through systematic training on **7 atomic acoustic conditions** and **54 compound acoustic scenarios**. Built on **2.4M training samples** covering **noise, far-field speech, obstruction, echo and reverberation, recording artifacts, electronic distortion, and transmission dropout**, MEGA-ASR uses **A2S-SFT** and **DG-WGPO based RL** to achieve **up to nearly 30% gains** over leading open and closed source SOTA models in challenging acoustic environments. If you like us, please give us a star✨.

<p align="center"><u><em>You’ll come back to Mega-ASR — after finding the rest fail in the real world.</em></u></p>


<p align="center">
  <a href="https://arxiv.org/abs/2605.19833">Technical Report 📖</a> /
  <a href="https://huggingface.co/datasets/zhifeixie/Voices-in-the-Wild-2M">Voices-in-the-wild-2M 🤗</a> /
  <a href="https://huggingface.co/zhifeixie/Mega-ASR">Mega-ASR Weights 🤗</a> /
  <a href="https://github.com/xzf-thu/Voices-in-the-Wild-Bench">Voices-in-the-Wild-Bench 🏆</a>
</p>

<p align="center">
  <a href="https://github.com/xzf-thu/Mega-ASR/raw/main/assets/wechat.jpg"><img src="https://img.shields.io/badge/WeChat-Join%20Group-07C160?logo=wechat&logoColor=white" alt="WeChat"></a>&nbsp;<a href="https://xzf-thu.github.io/Mega-ASR/"><img src="https://img.shields.io/badge/Project-Page-blue" alt="Project Page"></a>&nbsp;<a href="https://x.com/XieZhifei14110"><img src="https://img.shields.io/badge/X-@XieZhifei14110-black?logo=x&logoColor=white" alt="X"></a>
</p>


<p align="center">
  <img src="/docs/assets/dataset.png" alt="Mega-ASR Logo" width="100%">
</p>

### Comparison with SOTA open-source and closed-source models.

#### Sample 1

<div align="center">
  <video src="https://private-user-images.githubusercontent.com/201621992/594835233-2d847f22-a6d4-4d84-9bec-79a39001f9ca.mp4?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzkyMDU0NDYsIm5iZiI6MTc3OTIwNTE0NiwicGF0aCI6Ii8yMDE2MjE5OTIvNTk0ODM1MjMzLTJkODQ3ZjIyLWE2ZDQtNGQ4NC05YmVjLTc5YTM5MDAxZjljYS5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUxOVQxNTM5MDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mODgyYWRlZGI3OThjZWZmNzg1ZDhmNDRiNDMxZjYzZmE0Njk5OWJjYWJkZTVhZmM0OTM0OTI4MWI3ZmEzMGI0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9dmlkZW8lMkZtcDQifQ.qJS-ALDMknvRYFY73hGYmJ-WLzwtC4LRHJnHXlkpyyU" controls width="300"></video>
</div>


<table>
  <tr>
    <th valign="top">Ground Truth</th>
    <th valign="top">Mega-ASR (Ours)</th>
    <th valign="top">Qwen3-ASR</th>
    <th valign="top">Gemini-3-Pro</th>
    <th valign="top">Seed-ASR</th>
    <th valign="top">Whisper</th>
  </tr>
  <tr>
    <td valign="top">...and said to him let us go and eat some honey. Whose honey? inquired Kobay cautiously. My father's, Soongoora replied. Oh, all right, I'm with you, said the tortoise eagerly, and away they went.<br><br><strong>Reference</strong></td>
    <td valign="top"><span style="color:#ef4444">He</span> said to him <span style="color:#ef4444">let's</span> go and eat some honey. <span style="color:#ef4444">It's</span> honey? inquired <span style="color:#ef4444">very</span> cautiously. My father <span style="color:#ef4444">is Superabundant</span> — oh, all right, <span style="color:#ef4444">I will</span>, said <span style="color:#ef4444">to her</span> eagerly, and away they went.<br><br><strong>WER: <span style="color:#22c55e">47.1</span> ✅</strong></td>
    <td valign="top"><span style="color:#ef4444">&lt;empty&gt;</span><br><br><strong>WER: <span style="color:#ef4444">100.0</span> 🔴</strong></td>
    <td valign="top"><span style="color:#ef4444">But tell me, that's how she met</span> my father<span style="color:#ef4444">'s sister</span>. Oh, all right. <span style="color:#ef4444">I wish... I really...</span><br><br><strong>WER: <span style="color:#ef4444">86.1</span> 🔴</strong></td>
    <td valign="top">My father <span style="color:#ef4444">is</span>. Oh, all right, <span style="color:#ef4444">I wish you can</span>.<br><br><strong>WER: <span style="color:#ef4444">85.3</span> 🔴</strong></td>
    <td valign="top">...to him... some honey... <span style="color:#ef4444">oh yeah</span>...<br><br><strong>WER: <span style="color:#ef4444">92.5</span> 🔴</strong></td>
  </tr>
</table>

<details>
<summary><strong>More examples (Sample 2 – 6)</strong></summary>
