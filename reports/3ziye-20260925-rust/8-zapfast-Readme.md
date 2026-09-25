# ZapFast

**WhatsApp, native and fast.** ZapFast is a WhatsApp client written in Rust
with [egui](https://github.com/emilk/egui). It uses
[whatsapp-rust](https://github.com/oxidezap/whatsapp-rust) for the WhatsApp Web
protocol. It runs on Linux, macOS, and Windows, links to your phone as a
companion device, and has no browser engine. In our Linux test, it opens in
under a second and uses about 200 MB of idle RAM, compared with 1.13 GB for
WhatsApp Web and its Chromium processes. [See the measurements](https://zapfast.rocks/benchmarks/).

ZapFast is a sibling of [Spotifast](https://spotifast.rocks),
with the same native UI for a different service.

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshot-light.png">
  <img src="docs/screenshot.png" alt="ZapFast showing a conversation with an attachment, voice messages, reactions, a quoted reply, and a link preview">
</picture>

See **[zapfast.rocks](https://zapfast.rocks)** for downloads and guides.

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshot-group-light.png">
  <img src="docs/screenshot-group.png" alt="A titled group chat with participant names, reactions, a quoted mention, and a poll">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/screenshot-link-light.png">
  <img src="docs/screenshot-link.png" alt="The linking screen with the QR code">
</picture>

## What it does

- **Links to your phone.** Scan a QR code or link with your phone number.
  Recent history is copied to this computer after linking and stored here.
- **Chats.** See pinned, unread, muted, and archived chats, typing indicators,
  and message status. Search chats, saved messages, and contacts. The
  **Search** icon in a chat's header (or **Ctrl+F**) opens a pane beside the
  chat, as in WhatsApp Desktop, listing its matches newest first with the time
  and the line that matched. The calendar narrows them to one day, or lists
  that day's messages when the field is empty. Clicking a result, or reaching
  it with the arrow keys and pressing Enter, brings it into view with a brief
  flash; Escape closes the calendar, then the pane. The pane can be dragged
  wider, and in a narrow window it lies over the conversation instead of
  squeezing it. The newest 80 matches are listed, and the pane says when there
  are more. Right-click a group or a followed channel and choose **Leave group**
  or **Leave channel** to leave it, with the option to archive it in the same
  step; the local history stays on this computer and the chat keeps its
  messages.
  Filter the list to unread, private (one-to-one), favorites, or group chats
  with the chips under the search bar; a chip with unread chats shows how many
  it has. Right-click a chat and choose **Add to favorites** to mark it.
  Favorites sync with your phone both ways, and the **Favorites** chip lists
  them in the phone's order below any pinned chats. A chat added here goes to
  the end of the list; channels cannot be favorites.
  Followed channels have their own **Channels** chip and stay out of the other
  filters; right-click it to mute or unmute every channel at once. **Archived**
  opens the archived chats. Right-click a chat and choose **Mark as unread**
  to put an empty dot on it, as on the phone; the mark syncs with your phone
  both ways, and opening the chat or a new message clears it. Opening a chat with
  unread messages scrolls to an "unread messages" divider above the first one.
  Pinned chats stay in pin order (most recently pinned first), regardless of
  new messages. Like on the phone, you can pin up to three chats. Chat and contact name searches ignore accents, so `Angel`
  finds `Ángel`.
  The filters stay on one row and scroll horizontally in narrow sidebars.
  Unnamed groups use a shared participant summary for their title and subtitle;
  repeated first names appear as `Andrea ×3`, with your own entry shown as `You`.
  Incomplete group metadata preserves known names and retries with backoff;
  an empty cached subject remains eligible for recovery.
  Typing indicators show other participants, excluding your own linked devices.
  Newsletter channels are read-only; publishing channel posts is not supported.
- **Account privacy.** Settings, Privacy shows who can see your last seen,
  online status, profile photo, and About, who can add you to groups, your
  account read receipts, and whether unknown callers are silenced, and
  changes them on your phone, so a change applies on every linked device. A
  category set to **My contacts except** shows as such; the people it excludes
  are chosen on the phone. The values are read when ZapFast connects and when
  Settings opens; without a connection they cannot be changed.
- **Read state across devices.** Reading a chat syncs its unread badge with
  your phone and other linked devices, including when read receipts are off.
  Replies from another device clear preceding unread messages. The read-re