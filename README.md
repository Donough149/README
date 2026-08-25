# Groove Radio

A serverless radio discovery app: one static page (`index.html`), no backend, no build step.
It talks directly to the free, open [Radio Browser API](https://api.radio-browser.info)
(~50k community-listed stations) and keeps all personal data — favorites, listening
history, retention stats — in your browser's `localStorage`.

## Use it on your iPhone (anywhere, Wi-Fi or 5G)

It's a PWA. Host the repo anywhere static (GitHub Pages is free: repo Settings →
Pages → deploy from branch), open the URL in Safari, then **Share → Add to Home
Screen**. It installs as an app icon, runs full-screen, and works wherever you have
signal — there is no server of ours involved, your phone talks straight to the
Radio Browser mirrors. Lock-screen play/pause/skip controls work via the Media
Session API.

For a quick local try: `python3 -m http.server` in the repo folder, or just open
`index.html` in a browser.

## Always live

Every browse list is fetched fresh from the API — nothing is baked in. Visible
lists re-poll every 2 minutes, re-poll immediately when the app returns to the
foreground, and each view has a manual ↻ Refresh. Playing a station registers a
click upstream, and ♥ Like casts a real vote on Radio Browser — you feed the same
signals the discovery modes mine.

## Discovery modes

- **Hidden Gems** — low listens, abnormally high likes (votes-per-click ranking).
- **Rising, not risen** — listen counts accelerating but still small.
- **New with traction** — added in the last 90 days, already collecting votes.
- **Geographic outliers** — pick a genre; the countries with the fewest stations in it come first.
- **3am gems** — stations where it's prime-time evening locally right now, but not for you.
- **Rare tag combos** — unusual tag pairs drawn from your favorites.
- **Deep cuts** — well-liked stations with zero mainstream/chart tags.
- **Your keepers** — your own retention signal: stations you stayed on longest.
- **Roulette** — one random station with guardrails (alive, ≥96 kbps, some likes).
- **Faded giants** — high all-time love, drifting audience.
- **Favorites** — everything you've ♥-ed, with live status.

Plus the player's **⏭ Skip (same groove)**: skipping hops to another live, small
station matching the current station's rarest tags, skips what you've already
heard, and logs the skip as a negative signal for *Your keepers*. The steer box
in the player bar jumps the groove to any tag you type.
