<p align="center"><img src="port/packaging/icon/infamous-icon-1024.png" width="160" alt=""></p>

<h1 align="center">inFAMOUS Second Son — port nativo para PC</h1>

<p align="center"><a href="https://buymeacoffee.com/hayatog"><img src="https://img.shields.io/badge/Buy_me_a_coffee-Apoie_o_projeto-FFDD00?logo=buymeacoffee&amp;logoColor=000000" alt="Apoie com um café / Buy me a coffee"></a></p>

<p align="center">
  <a href="#english"><b>English below</b></a> ·
  <a href="https://github.com/HayatoG/iss_pc/releases/latest">Download</a> ·
  <a href="https://www.youtube.com/@hayatog-dev">YouTube</a> ·
  <a href="https://discord.gg/UMkdMYZh9g">Discord</a>
</p>

<p align="center"><a href="https://github.com/sponsors/HayatoG"><img src="https://img.shields.io/badge/Sponsor-HayatoG-ea4aaa?logo=githubsponsors&logoColor=white" alt="Sponsor HayatoG on GitHub"></a></p>

<p align="center"><a href="https://github.com/HayatoG/iss_pc/actions/workflows/build.yml"><img src="https://github.com/HayatoG/iss_pc/actions/workflows/build.yml/badge.svg" alt="Build"></a></p>

> **Jogável, em desenvolvimento.** O jogo inicia, chega ao gameplay e passa pelos primeiros capítulos, mas o desempenho ainda é instável (20–30 FPS típicos numa RTX 2060) e há falhas de imagem conhecidas. Veja o [Status](#status).

**inFAMOUS Second Son** (PS4, CUSA00223, jogo base 1.00 + update 1.07) rodando no PC sem emulador de CPU: o código original do jogo roda nativo no processador, o sistema do PS4 é reimplementado e a GPU é traduzida para Vulkan. Usa o mesmo núcleo dos ports de [The Last Guardian](https://github.com/HayatoG/tlg_pc) e [Gravity Rush 2](https://github.com/HayatoG/gr2_pc).

> **Nenhum arquivo do jogo vem com este projeto.** Para jogar, você precisa da sua própria cópia, tirada do seu PS4.

Por **HayatoG** · YouTube [@hayatog-dev](https://www.youtube.com/@hayatog-dev) · Discord [discord.gg/UMkdMYZh9g](https://discord.gg/UMkdMYZh9g)

| | |
|---|---|
| ![Delsin diante do outdoor, com o pedido de virar o controle de lado](docs/screenshots/01-grafite-sensor.jpg) | ![Delsin no galpão do cais](docs/screenshots/02-galpao.jpg) |
| ![Na cerca do cais](docs/screenshots/03-cerca.jpg) | ![Correndo pela praia ao pôr do sol](docs/screenshots/04-praia.jpg) |

![Escalando as rochas acima da vila](docs/screenshots/05-escalada.jpg)

<sub>Capturas na resolução nativa (1920×1080, reduzidas para 1280), direto da GPU, no Linux com uma RTX 2060.</sub>

## Contribuidores / Contributors

<p align="center">
  <a href="https://github.com/HayatoG"><img src="https://avatars.githubusercontent.com/u/22659047?v=4" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/intemerated"><img src="https://avatars.githubusercontent.com/u/343755099?v=4" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/Andretuta"><img src="https://avatars.githubusercontent.com/u/219594641?v=4" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/Playdbunny"><img src="https://avatars.githubusercontent.com/u/70190491?v=4" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/EdouardSence"><img src="https://avatars.githubusercontent.com/u/103503538?v=4" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/HayatoG/iss_pc/graphs/contributors"><img src="https://github.com/identicons/guilherme-oliveira.png" width="72" alt="Avatar de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/batuhankiskac"><img src="https://github.com/batuhankiskac.png" width="72" alt="Foto de perfil de contribuidor"></a>&nbsp;&nbsp;
  <a href="https://github.com/sapoguruoficial-cmd"><img src="https://github.com/sapoguruoficial-cmd.png" width="72" alt="Foto de perfil de contribuidor"></a>
</p>

## Novidades

- **Launcher novo (Qt Quick), agora o padrão:** com 10 telas, incluindo **Mods / Cheats** e **Avançado**, interface em português e inglês e o idioma do jogo seguindo o do sistema por padrão. O launcher antigo (Tk) continua no pacote como **inFAMOUS Second Son (classic)**, de reserva. Veja [O launcher](#o-launcher).
- **Saves e dados:** pasta de dados configurável, backup antes de cada partida, exportar/importar `.zip`, duplicar e excluir saves, e a busca de saves de outras instalações. Resolve o "perdi meu save depois de atualizar". Veja [Saves e dados](#saves-e-dados).
- **Faróis piscando e brilho que atravessava personagens: corrigido.** O contador de oclusão que o jogo lê para saber quanto de uma luz está visível era falso; o novo modo 3 (o padrão) devolve contagem zero, e isso corrigiu o problema, **confirmado no Windows e no Linux**. Veja [Luzes e oclusão](#luzes-e-oclusão).
- **Correções experimentais BP01–BP12:** doze correções trazidas de outros ports de PS4 e do shadPS4, com chave individual, perfil Recomendado e o "Como a release anterior" para comparar. Veja [Correções experimentais](#correções-experiment