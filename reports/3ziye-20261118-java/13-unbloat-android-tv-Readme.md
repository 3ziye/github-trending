# Kit TV Android : rendez votre TV rapide et belle

**🇫🇷 Français** · [🇬🇧 English version](README-en.md)

Votre TV Android rame, affiche des pubs partout, et le son se décale pendant les films ? Ce kit l'allège en quelques minutes depuis un PC Windows, un Mac ou un PC Linux. Il installe aussi **Zen Home**, un écran d'accueil minimaliste façon Apple TV.

> [!TIP]
> **Téléchargez l'application, c'est le plus simple :** rendez-vous dans **[Releases](https://github.com/xMazaki/unbloat-android-tv/releases/latest)** (dans la colonne de droite de cette page) et prenez la version pour votre ordinateur : Windows, macOS ou Linux. Elle trouve votre TV toute seule et vous guide pas à pas. [Détails ci-dessous](#en-bref).

<table>
  <tr>
    <th align="center">Avant</th>
    <th align="center">Après</th>
  </tr>
  <tr>
    <td><img src="docs/avant.jpg" alt="TV TCL avant : accueil Google TV chargé de pubs et d'applis" width="400"></td>
    <td><img src="docs/apres.jpg" alt="TV TCL après : écran d'accueil Zen Home avec photo de paysage et dock" width="400"></td>
  </tr>
  <tr>
    <td align="center"><sub>Accueil d'origine : pubs, applis promo, lenteurs</sub></td>
    <td align="center"><sub>Zen Home : photo de paysage, l'heure et vos applis</sub></td>
  </tr>
</table>

<sub>Photos réelles d'une TCL de 2019. Le titre affiché en haut à gauche est personnalisable.</sub>

> [!WARNING]
> **Projet personnel partagé tel quel, sans aucune garantie.** Je ne suis pas responsable des problèmes que son utilisation pourrait causer à votre TV, à vos appareils ou à vos données. Chaque TV est différente : lisez la section [Avant d'utiliser le kit sur votre TV](#avant-dutiliser-le-kit-sur-votre-tv).

---

## Sommaire

1. [En bref](#en-bref)
2. [Ce que fait le kit](#ce-que-fait-le-kit)
3. [Compatibilité](#compatibilité)
4. [Avant d'utiliser le kit sur votre TV](#avant-dutiliser-le-kit-sur-votre-tv)
5. [Préparer la TV (5 minutes)](#préparer-la-tv-5-minutes)
6. [Utilisation](#utilisation)
7. [Personnaliser Zen Home](#personnaliser-zen-home)
8. [Sécurité et retour en arrière](#sécurité-et-retour-en-arrière)
9. [Dépannage](#dépannage)
10. [Contenu du dossier](#contenu-du-dossier)
11. [Responsabilité](#responsabilité)
12. [Crédits et licence](#crédits-et-licence)

---

## En bref

**Le plus simple : l'application.** Téléchargez la version pour votre ordinateur dans les [Releases](https://github.com/xMazaki/unbloat-android-tv/releases/latest), lancez-la : elle trouve votre TV sur le réseau, vous guide pour activer le débogage, et tout se fait en quelques clics.

| Système | Fichier | Premier lancement |
|---|---|---|
| Windows 10 / 11 | `KitTVAndroid-…-windows-x64.exe` | Si Windows affiche « Windows a protégé votre ordinateur » : **Informations complémentaires → Exécuter quand même**. Une petite fenêtre noire s'ouvre avec l'interface : laissez-la ouverte. |
| macOS (Apple M1 et plus récents) | `KitTVAndroid-…-macos-apple-silicon.zip` | Ouvrez le zip, puis double-cliquez sur **Kit TV Android** dans le dossier : le Terminal s'ouvre, puis l'interface. Si macOS refuse : **Réglages Système → Confidentialité et sécurité → Ouvrir quand même**, puis relancez. Autorisez l'accès au **réseau local** pour le Terminal. macOS 12 ou plus récent ; sinon, utilisez les scripts ci-dessous. |
| macOS (processeur Intel) | `KitTVAndroid-…-macos-intel.zip` | Pareil que ci-dessus. |
| Linux | `KitTVAndroid-…-linux-x64.tar.gz` (ou `arm64`) | Décompressez, puis lancez `kit-tv-android`. |

L'application s'ouvre dans votre navigateur et se ferme quand vous fermez l'onglet. Elle fait exactement la même chose que les scripts ci-dessous, avec les mêmes sécurités. Les applications ne sont pas signées (un certificat est payant), d'où l'avertissement au premier lancement. Si un antivirus signale l'exe, c'est une fausse alerte fréquente pour les petits programmes non signés : le code source est dans ce dépôt, et vous pouvez comparer l'empreinte du fichier avec `SHA256SUMS.txt` de la release.

**Avec les scripts** (sans rien télécharger d'autre que le kit) :

1. Activez le mode développeur et le débogage sur la TV ([voir comment](#préparer-la-tv-5-minutes)).
2. Double-cliquez sur **`LANCER.bat`** (Windows) ou **`LANCER.command`** (macOS), ou lancez **`./LANCER.sh`** (Linux), puis tapez l'adresse IP de la TV.
3. Acceptez « Autoriser le débogage » sur la TV.
4. Faites dans l'ordre les options **1** (sauvegarde), **2** (allègement) et **3** (écran d'accueil).
5. Si quelque chose ne vous plaît pas, l'option **6** remet tout comme avant.

## Ce que fait le kit

| Option du menu | Ce qu'elle fait | Modifie la TV ? |
|---|---|---|
| **1. Diagnostic + sauvegarde** | Relève la version d'Android, la mémoire, le processeur et le Wi-Fi. Sauvegarde la liste des applis et des réglages, avec une capture de l'écran. | Non |
| **2. Alléger** | Désactive les pubs, la télémétrie et les services inutiles connus (Google, TCL, Sony, Xiaomi…). Pour les fonctions que vous utilisez peut-être (Chromecast, A