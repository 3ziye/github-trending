<p align="center"><img src="port/packaging/icon/tlg-icon-1024.png" width="160" alt=""></p>

<h1 align="center">The Last Guardian — port nativo para PC</h1>

<p align="center"><a href="https://buymeacoffee.com/hayatog"><img src="https://img.shields.io/badge/Buy_me_a_coffee-Apoie_o_projeto-FFDD00?logo=buymeacoffee&amp;logoColor=000000" alt="Apoie com um café / Buy me a coffee"></a></p>

<p align="center">
  <a href="#english"><b>English below</b></a> ·
  <a href="https://github.com/HayatoG/tlg_pc/releases/latest">Download</a> ·
  <a href="https://www.youtube.com/@hayatog-dev">YouTube</a> ·
  <a href="https://discord.gg/UMkdMYZh9g">Discord</a>
</p>

<p align="center"><a href="https://github.com/sponsors/HayatoG"><img src="https://img.shields.io/badge/Sponsor-HayatoG-ea4aaa?logo=githubsponsors&logoColor=white" alt="Sponsor HayatoG on GitHub"></a></p>

<p align="center"><a href="https://github.com/HayatoG/tlg_pc/actions/workflows/build.yml"><img src="https://github.com/HayatoG/tlg_pc/actions/workflows/build.yml/badge.svg" alt="Build"></a></p>

<p align="center"><a href="https://youtu.be/F5sD_HCGCWo"><img src="docs/screenshots/video-tutorial.jpg" width="640" alt="Como portar jogos de PS4 — vídeo no YouTube"></a></p>

<p align="center">▶️ <a href="https://youtu.be/F5sD_HCGCWo"><b>Vídeo tutorial:</b> como portar jogos de PS4 para o PC</a></p>

**The Last Guardian** (PS4, CUSA03627 US / CUSA03745 UE, update 01.03) rodando no PC com imagem, som, controle, mouse e teclado e saves, a 30 FPS estáveis (60 FPS e FPS livre opcionais, experimentais) e sem emulador de CPU. O código original do jogo roda nativo no processador. O sistema do PS4 é reimplementado, e a GPU é traduzida para Vulkan.

> **Nenhum arquivo do jogo vem com este projeto.** Para jogar, você precisa da sua própria cópia, tirada do seu PS4.

Por **HayatoG** · YouTube [@hayatog-dev](https://www.youtube.com/@hayatog-dev) · Discord [discord.gg/UMkdMYZh9g](https://discord.gg/UMkdMYZh9g)

| | |
|---|---|
| ![Menu inicial](docs/screenshots/01-menu.jpg) | ![O menino desperta na caverna](docs/screenshots/02-despertar.jpg) |
| ![O menino e o Trico](docs/screenshots/03-trico.jpg) | ![Ruínas](docs/screenshots/04-ruinas.jpg) |

<sub>Capturas na resolução nativa (1920×1080), direto da GPU, no Linux com uma RTX 2060.</sub>

## Novidades

- **60 FPS e FPS livre (experimental):** launcher → Vídeo → "Taxa de quadros (experimental)", ou `TLG_FPS=30|60|unlocked`. O padrão continua 30 FPS, como no PS4. Detalhes em [`docs/60fps.md`](docs/60fps.md) ([#5](https://github.com/HayatoG/tlg_pc/issues/5)).
- **Filtros de imagem:** anti-aliasing SMAA, nitidez RCAS (FSR 1) ou CAS (AMD) e ajustes de cor (brilho, contraste, saturação, gama), no launcher e ao vivo no menu do jogo (Insert → Imagem) ([#2](https://github.com/HayatoG/tlg_pc/issues/2)).
- **Mouse e teclado:** o mouse gira a câmera (sensibilidade e eixo Y invertido no launcher) e as teclas e botões do mouse podem ser remapeados ([#8](https://github.com/HayatoG/tlg_pc/issues/8)).
- **Sensor de movimento:** o giroscópio do DualShock 4/DualSense funciona direto. Em controles sem sensor, um toque em Share (ou L3+R3) liga o "modo sensor": o analógico esquerdo inclina o controle e X/A sacode. No teclado, T/G inclinam e Y sacode.
- **Brilho e luzes como no PS4:** a exposição automática do jogo agora lê o valor certo da GPU, e as cenas ao ar livre não estouram mais em branco (`TLG_READBACK_LINEAR=1`, ligado por padrão; `0` volta ao comportamento antigo) ([#38](https://github.com/HayatoG/tlg_pc/issues/38), [#40](https://github.com/HayatoG/tlg_pc/issues/40)).
- **Acesso direto à memória (shaders):** opção nova no launcher (Gráficos → GPU), **desligada por padrão** (`TLG_DIRECT_MEMORY_ACCESS=1`). Os shaders leem constantes direto da memória do jogo: corrige algumas cenas com problema, mas o jogo fica mais lento. Os shaders dela ficam num cache próprio e são compilados de novo na primeira vez.
- **Analógicos:** zona morta de 10% contra drift (`TLG_STICK_DEADZONE`), e o último controle usado é o que vale.
- **Touchpad sem touchpad:** segure View/Select (ou Tab) e mova o analógico direito (ou as setas) para deslizar o dedo; um toque rápido continua sendo clique.
- **Desempenho:** o FPS não cai mais com o tempo (as variantes de shader agora se repetem), e transições parciais de imagem repetidas são puladas.
- **Cache de shaders automático:** fica em `user/cache/`, junto dos saves (em Linux e Windows; o cache antigo de `~/.local/share/shadPS4` ou `user/user/` é trazido sozinho na primeira partida). A pasta leva a versão do tradutor de shaders, e o cache antigo é apagado sozinho depois de uma atualização. Para recompilar tudo, o launcher tem o botão **Limpar cache de shaders** (ou `./run_tlg.sh --clear-shader-cache`); ele apaga só os shaders compilados deste jogo, nunca saves ou configurações.

## Status

| Área | Estado |
|---|---|
| Boot, menu, intro e gameplay | ✅ Funciona; sessões de 10+ minutos sem falhas |
| Imagem | ✅ Nativa, 1080p, sem tr