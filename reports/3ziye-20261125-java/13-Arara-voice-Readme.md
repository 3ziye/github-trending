<div align="center">

# Arara

**Ditado por voz grátis, open source e 100% local para português do Brasil.**<br>
Aperte <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Espaço</kbd>, fale, e o texto aparece onde está o cursor.

<img src="docs/midia/arara-demo.gif" width="720" alt="O pop-up do Arara ouvindo e mostrando o texto ao vivo, a arara batendo as asas no &quot;Colado!&quot; e o prompt colado inteiro no terminal do Claude Code">

[![Baixar para Windows](https://img.shields.io/badge/Baixar_para-Windows_10_e_11-1C72CF?style=for-the-badge&logo=windows&logoColor=white)](https://github.com/davimatosms/Arara-voice/releases/latest/download/Arara-Setup.exe)
[![Baixar para Mac Apple Silicon](https://img.shields.io/badge/Baixar_para-Mac_(M1_a_M4)-6CC93A?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/davimatosms/Arara-voice/releases/latest/download/Arara-Mac-AppleSilicon.dmg)
[![Baixar para Mac Intel](https://img.shields.io/badge/Baixar_para-Mac_Intel-6CC93A?style=for-the-badge&logo=apple&logoColor=white)](https://github.com/davimatosms/Arara-voice/releases/latest/download/Arara-Mac-Intel.dmg)

[Site](https://arara-voice.vercel.app) · [Todas as versões](https://github.com/davimatosms/Arara-voice/releases) · [Licença MIT](LICENSE)

</div>

> **In English:** Arara is a free, open-source (MIT) voice dictation app for Windows and macOS, built for Brazilian
> Portuguese. It runs OpenAI's Whisper locally through whisper.cpp: no cloud, no account, no telemetry. Press
> <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Space</kbd>, speak, and the text is pasted wherever your cursor is, with a live
> preview while you talk. Made for dictating prompts to AI coding agents (Claude Code, Codex, Cursor...), but it
> works in any app. Downloads above; the rest of this page is in Portuguese.

## Por que o Arara

- **Grátis e sem conta.** Sem assinatura, sem limite de minutos, sem cadastro. Código aberto sob MIT.
- **Sua voz não sai do computador.** O Whisper roda na sua máquina (whisper.cpp). Nada de nuvem, nada de telemetria.
- **Português de verdade.** Feito para o português do Brasil: sotaque, gíria, termo técnico, acento e pontuação.
- **Funciona em qualquer janela.** Terminal, IDE, navegador, chat, editor de texto. O texto é colado inteiro, de uma vez.
- **Feito para conversar com agentes de IA.** Explique em voz alta o que você quer, do jeito que falaria com um colega,
  e mande o prompt pronto para o Claude Code, o Codex, o Cursor ou o ChatGPT.

## Recursos

- Atalho global (padrão <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Espaço</kbd>, dá para trocar). Aperte uma vez para
  começar a ouvir e de novo para colar. <kbd>Esc</kbd> cancela.
- **Texto ao vivo** no pop-up enquanto você fala: a prévia aparece em cinza e fica branca quando o trecho é confirmado.
- Cola onde está o cursor, sem digitar letra por letra.
- Três modelos de voz, baixados na primeira vez: leve (`base`, 148 MB), equilibrado (`small`) e preciso
  (`large-v3-turbo`, o padrão). Aceleração por GPU opcional (Vulkan).
- **Dicionário** para nomes, siglas e termos que o Whisper erra.
- **Histórico** dos ditados, salvo só no seu computador.
- **Temas com 5 araras brasileiras** (canindé, azul, vermelha, de-lear e maracanã), em modo claro e escuro. Se quiser, o
  ícone do app (janela e bandeja) segue a arara do tema.
- Primeira execução guiada: baixa o modelo, testa o microfone e o atalho e faz o primeiro ditado com você.
- Avisa quando sai versão nova e se atualiza com um clique (conferindo o SHA-256).

## Telas

<img src="docs/midia/janela-inicio.png" width="720" alt="Janela do Arara na tela Início: pronto para ditar, o atalho Ctrl + Shift + Espaço e o estado do modelo, do microfone e do histórico">

O pop-up de gravação nas 5 araras, no modo escuro e no claro:

<img src="docs/midia/temas.png" width="720" alt="O pop-up &quot;Ouvindo&quot; com o texto ao vivo nos temas canindé, azul, vermelha, de-lear e maracanã, cada um no modo escuro e no claro">

## Como usar

1. **Instale** pelo botão do seu sistema lá em cima e abra o Arara. Na primeira vez ele baixa o modelo de voz e testa o
   microfone com você.
2. **Clique onde o texto deve entrar** (o prompt do agente, um e-mail, uma mensagem) e aperte
   <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>Espaço</kbd>.
3. **Fale** e aperte o atalho de novo. O texto aparece inteiro onde está o cursor. É só enviar.

## Privacidade

O Arara não manda áudio, texto nem telemetria para lugar nenhum. A transcrição acontece toda no seu computador.
Ele só usa a internet para duas coisas:

- baixar o modelo de voz da Hugging Face, na primeira vez (ou quando você troca de modelo);
- consultar o `versao.json` do site para saber se há versão nova (dá para desligar em Configurações; o instalador só
  é baixado se você aceitar).

Configurações, histórico e modelos ficam em `%APPDATA%\Arara` no Windows. Detalhes na
[política de privacidade e de assinatura de código](https://arara-voice.vercel.app/politica.html).

## Perguntas frequentes

**O W