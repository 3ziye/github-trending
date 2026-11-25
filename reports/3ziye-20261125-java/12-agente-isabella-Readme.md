<!-- 🌐 REPO PÚBLICO · agente-isabella · versión para redes, SIN llaves ni datos privados. El laboratorio privado de trabajo es otro repositorio. -->

<picture>
  <source media="(max-width: 767px)" srcset="https://raw.githubusercontent.com/viajatech/agente-isabella/main/docs/img/presentacion/hero-movil.svg">
  <img alt="Agente Isabella — la IA que hace llamadas reales desde tu propio Android. Creado por David Ruiz Duarte (viajatech)." src="docs/img/presentacion/hero.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.youtube.com/shorts/oSUbPbwd6TY"><img src="docs/img/presentacion/btn-video.svg" height="44" alt="Ver el video"></a>
  <a href="#instalar"><img src="docs/img/presentacion/btn-instalar.svg" height="44" alt="Instalar"></a>
  <a href="#como-funciona"><img src="docs/img/presentacion/btn-como.svg" height="44" alt="Cómo funciona"></a>
  <a href="docs/BOOT_RECOVERY.md"><img src="docs/img/presentacion/btn-rescate.svg" height="44" alt="Si no arranca"></a>
</p>

<h3 align="center">Tu celular. Tu SIM. Tu llamada. La voz es de Isabella.</h3>

<p align="center">
  Una app Android que marca desde <b>tu propia línea</b> y conversa en tiempo real con la voz en vivo de <b>Google Gemini</b>.<br>
  Sin Twilio, sin números rentados, sin VoIP de terceros.
</p>

<p align="center">
  <img alt="Android 14+" src="https://img.shields.io/badge/Android-14%2B-1FE03C?style=for-the-badge&logo=android&logoColor=white&labelColor=0E0D14">
  <img alt="Gemini Live, voz Zephyr" src="https://img.shields.io/badge/Gemini_Live-voz_Zephyr-FF2A6D?style=for-the-badge&logo=googlegemini&logoColor=white&labelColor=0E0D14">
  <img alt="Root con Magisk" src="https://img.shields.io/badge/root-Magisk-6C5CFF?style=for-the-badge&labelColor=0E0D14">
  <img alt="Cloudflare Workers" src="https://img.shields.io/badge/Cloudflare-Workers-F38020?style=for-the-badge&logo=cloudflare&logoColor=white&labelColor=0E0D14">
</p>

> **🌐 Repositorio público y limpio** — sin llaves, sin tokens y sin datos privados.
> Para que funcione, **tú pones tus propias llaves** (se explica paso a paso).

## 📞 ¿Qué es esto?

**Isabella Llamadas** es una app Android que marca un número desde **tu propia línea** y conversa en tiempo real con
la persona que contesta, usando la voz en vivo de **Google Gemini**.

La voz de Isabella entra **digitalmente** al canal de la llamada (no por la bocina), así que se oye limpia y sin eco.
Para eso el celular necesita **root con Magisk**: Android no deja que una app normal meta audio a una llamada.

<p align="center">
  <img alt="Ejemplo de llamada de prueba: Isabella saluda diciendo que es una inteligencia artificial, platica y cuelga sola." src="docs/img/presentacion/llamada.svg" width="340">
</p>
<p align="center"><sub>Ejemplo de una llamada de prueba. La primera frase de Isabella <b>siempre</b> dice que es una inteligencia artificial.</sub></p>

| Lo que hace | Cómo |
|---|---|
| 🗣️ Conversa en vivo por teléfono | Gemini Live por WebSocket, audio PCM 16/24 kHz |
| 🔐 Tus llaves nunca viven en el cel | Un Worker de Cloudflare (gratis) entrega tokens efímeros de un solo uso |
| 🤖 Se presenta SIEMPRE como IA | Primera frase obligatoria: «Soy una inteligencia artificial…» |
| ⏱️ No gasta de más | 8 fusibles: techo por llamada, topes por minuto/día, cuelga en silencio, nunca reconecta… |
| 📵 Contra toques accidentales | Confirmación de 3 s antes de marcar |
| 🎚️ Audio afinable | Volumen TTS, pre-énfasis, filtro de graves, soft-clip |
| 💬 Modo sin llamada | Platica con Isabella por el micrófono y la bocina del cel (no requiere root) |
| 🧪 Pruebas sin gastar | Gemini falso y Worker local para probar todo en la Mac |

## 🎬 Míralo en acción

<p align="center">
  <a href="https://www.youtube.com/shorts/oSUbPbwd6TY"><img alt="Ver el video «Agentes autónomos que marcan por ti» en YouTube Shorts" src="docs/img/presentacion/video.svg" width="100%"></a>
</p>

<a id="como-funciona"></a>

## ⚙️ Cómo funciona

<picture>
  <source media="(max-width: 767px)" srcset="https://raw.githubusercontent.com/viajatech/agente-isabella/main/docs/img/presentacion/como-funciona-movil.svg">
  <img alt="Diagrama: tu Worker de Cloudflare guarda la llave y entrega tokens de un solo uso; el celular conversa con Gemini Live y mete la voz de Isabella a la llamada VoLTE por tu SIM; la Mac solo compila, instala y configura." src="docs/img/presentacion/como-funciona.svg" width="100%">
</picture>

1. **La app pide un token a tu Worker de Cloudflare.** El Worker revisa el secreto del aparato y los topes (3 por minuto,
   30 por día). Tu llave de Gemini vive **solo** ahí.
2. **Google entrega un token efímero de un solo uso**, con la voz y la persona ya amarradas: desde el cel no se pueden cambiar.
3. **El celular abre Gemini Live** con ese token: audio en vivo, voz «Zephyr».
4. **La voz de Isabella entra digital a la llamada** por los mezcladores de audio del celular (root con Magisk): tu SIM, tu línea.

La Mac solo compila, instala y configura. El detalle técnico e