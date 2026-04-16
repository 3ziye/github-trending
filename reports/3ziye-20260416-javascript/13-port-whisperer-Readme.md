# port-whisperer

**A beautiful CLI tool to see what's running on your ports.**

Stop guessing which process is hogging port 3000. `port-whisperer` gives you a color-coded table of every dev server, database, and background process listening on your machine -- with framework detection, Docker container identification, and interactive process management.

## What it looks like

```
$ ports

 ┌─────────────────────────────────────┐
 │  Port Whisperer                     │
 │  listening to your ports...         │
 └─────────────────────────────────────┘

┌───────┬─────────┬───────┬──────────────────────┬────────────┬────────┬───────────┐
│ PORT  │ PROCESS │ PID   │ PROJECT              │ FRAMEWORK  │ UPTIME │ STATUS    │
├───────┼─────────┼───────┼──────────────────────┼────────────┼────────┼───────────┤
│ :3000 │ node    │ 42872 │ frontend             │ Next.js    │ 1d 9h  │ ● healthy │
├───────┼─────────┼───────┼──────────────────────┼────────────┼────────┼───────────┤
│ :3001 │ node    │ 95380 │ preview-app          │ Next.js    │ 2h 40m │ ● healthy │
├───────┼─────────┼───────┼──────────────────────┼────────────┼────────┼───────────┤
│ :4566 │ docker  │ 58351 │ backend-localstack-1 │ LocalStack │ 10d 3h │ ● healthy │
├───────┼─────────┼───────┼──────────────────────┼────────────┼────────┼───────────┤
│ :5432 │ docker  │ 58351 │ backend-postgres-1   │ PostgreSQL │ 10d 3h │ ● healthy │
├───────┼─────────┼───────┼──────────────────────┼────────────┼────────┼───────────┤
│ :6379 │ docker  │ 58351 │ backend-redis-1      │ Redis      │ 10d 3h │ ● healthy │
└───────┴─────────┴───────┴──────────────────────┴────────────┴────────┴───────────┘

  5 ports active  ·  Run ports <number> for details  ·  --all to show everything
```

Colors: green = healthy, yellow = orphaned, red = zombie.

## Install

```bash
npm install -g port-whisperer
```

Or run it directly without installing:

```bash
npx port-whisperer
```

### Or let Claude Code install it for you

If you use [Claude Code](https://claude.ai/code), you can ask it to `npm install -g port-whisperer` and start using `ports` right away -- no setup steps needed.

## Usage

### Show dev server ports

```bash
ports
```

Shows dev servers, Docker containers, and databases. System apps (Spotify, Raycast, etc.) are filtered out by default.

### Show all listening ports

```bash
ports --all
```

Includes system services, desktop apps, and everything else listening on your machine.

### Inspect a specific port

```bash
ports 3000
# or
whoisonport 3000
```

Detailed view: full process tree, repository path, current git branch, memory usage, and an interactive prompt to kill the process.

### Kill a process

```bash
ports kill 3000                # kill by port
ports kill 3000 5173 8080      # kill multiple
ports kill 3000-3010           # kill a port range
ports kill 42872               # kill by PID
ports kill -f 3000             # force kill (SIGKILL)
```

Resolves port to process automatically. Falls back to PID if no listener matches. Use `-f` when a process won't die gracefully.

Port ranges expand into individual kills -- empty ports are silently skipped and shown as a summary:

```
$ ports kill 3000-3005

  Killing :3000 — node (PID 42872)
  ✓ Sent SIGTERM to :3000 — node (PID 42872)
  Killing :3001 — node (PID 95380)
  ✓ Sent SIGTERM to :3001 — node (PID 95380)

  Range summary: 2 killed, 4 empty
```

### View process logs

```bash
ports logs 3000               # show last 50 lines and exit
ports logs 3000 -f            # follow (stream new lines)
ports logs 3000 --lines 10    # show last 10 lines
ports logs 3000 --lines 10 -f # show last 10 then follow
ports logs 3000 --err         # stderr only
```

Discovers log files automatically using `lsof` file descriptor detection. If stdout/stderr is redirected to a file, it finds and tails it. Falls back to system log (`log show` on macOS, `journalctl` on Linux) when no log files are found.

```
$ ports logs 3000 --lines 5

  Port Whisperer — logs for :3000 (node, PID 42872)

  ▸ Tailing stdout: /tmp/next-dev.output

  ▲ Next.js 16.2.3 (Turbopack)
  - Local: http://localhost:3000
  ✓ Ready in 195ms
   GET / 200 in 990ms
   GET /api/auth/session 200 in 6ms
```

### Show all dev processes

```bash
ports ps
```

A beautiful `ps aux` for developers. Shows all running dev processes (not just port-bound ones) with CPU%, memory, framework detection, and a smart description column. Docker processes are collapsed into a single summary row.

```
$ ports ps

┌───────┬─────────┬──────┬──────────┬──────────┬───────────┬─────────┬────────────────────────────────┐
│ PID   │ PROCESS │ CPU% │ MEM      │ PROJECT  │ FRAMEWORK │ UPTIME  │ WHAT                           │
├───────┼─────────┼──────┼──────────┼──────────┼───────────┼─────────┼────────────────────────────────┤
│ 592   │ Docker  │ 1.3  │ 735.5 MB │ —        │ Docker    │ 13d 12h │ 14 processes                   │
├───────┼─────────┼──────┼──────────┼──────────┼───────────┼────────