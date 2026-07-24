<!--
  GitHub Profile README
  Repo : https://github.com/Oxgendev/Oxgendev
  File : README.md

  Paste this entire file into Oxgendev/Oxgendev/README.md
-->

<div align="center">

# Hi, I'm Oguzhan Salih
### Merhaba, ben Oğuzhan Salih

**Full-Stack Developer** · Backend-focused · TypeScript · Node.js · React · Next.js

Building production systems where performance, data integrity, and long-term architecture actually matter.  
Performans, veri bütünlüğü ve uzun vadeli mimarinin önemli olduğu production sistemler geliştiriyorum.

📍 Open to relocation — **Sweden / EU** · Taşınmaya açığım — **İsveç / AB**

<br/>

[English](#-about--hakkımda) · [Türkçe](#-hakkımda--about)

<br/>

<a href="https://github.com/Oxgendev">
  <img src="https://img.shields.io/github/followers/Oxgendev?label=Followers&style=for-the-badge&color=0969da" alt="GitHub Followers" />
</a>
<a href="https://www.linkedin.com/in/o%C4%9Fuzhan-salih-622744374/">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="https://oxchi.com">
  <img src="https://img.shields.io/badge/Product-OxChi-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="OxChi" />
</a>
<img src="https://img.shields.io/badge/Open%20to%20Work-Sweden%20%7C%20EU-2ea44f?style=for-the-badge" alt="Open to relocation" />

</div>

---

## About · Hakkımda

<details open>
<summary><strong>🇬🇧 English</strong></summary>

<br/>

I'm a Full-Stack Developer with a strong bias toward **backend engineering**, **database architecture**, and **scalable web platforms**.

I ship systems that stay reliable after launch — not demos that only look good in a screenshot. Most of my recent work lives at the intersection of **Next.js dashboards**, **Node.js APIs**, **PostgreSQL / Redis**, and **real-time Discord / FiveM tooling**.

**What I focus on**
- Clean API & service boundaries
- Data safety under real traffic and failure modes
- Latency reduction without unreadable code
- TypeScript that other engineers can maintain months later

**Looking for**  
Backend / Full-Stack roles in **Sweden** or the **EU** — teams that care about ownership, quality, and measurable product impact.

</details>

<details>
<summary><strong>🇹🇷 Türkçe</strong></summary>

<br/>

**Backend mühendisliği**, **veritabanı mimarisi** ve **ölçeklenebilir web platformları** odaklı bir Full-Stack Developer’ım.

Ekran görüntüsünde güzel duran demolar değil; canlıya çıktıktan sonra da ayakta kalan sistemler üretiyorum. Son dönem işlerimin çoğu **Next.js paneller**, **Node.js API’ler**, **PostgreSQL / Redis** ve **gerçek zamanlı Discord / FiveM araçları** kesişiminde.

**Odaklandığım konular**
- Temiz API ve servis sınırları
- Gerçek trafik ve hata senaryolarında veri güvenliği
- Okunabilirliği bozmadan latency düşürme
- Aylar sonra da bakımı yapılabilir TypeScript

**Aradığım**  
**İsveç** veya **AB**’de Backend / Full-Stack roller — sahiplik, kalite ve ölçülebilir ürün etkisi önemseyen ekipler.

</details>

---

## Currently Building · Şu An Üzerinde Çalıştığım

| Project | What it is | Stack |
|--------|------------|--------|
| **[OxChi](https://oxchi.com)** | Discord bot satış & yönetim platformu — OAuth, billing, canlı bot kontrolü, admin RBAC | Next.js · Node.js · PostgreSQL · MongoDB · Redis · BullMQ · Discord.js |
| **bot-manager** | Windows üzerinde PM2 ile bot lifecycle (start / stop / restart / log / heartbeat) | Node.js · PM2 · Redis · WebSocket |
| **FiveM tooling** | API + Lua tarafında sunucu / performans işleri | TypeScript · Lua · Redis · SQL |

> OxChi monorepo şu an private; ürün canlıda: **[oxchi.com](https://oxchi.com)**

---

## Featured Product · Öne Çıkan Ürün

### OxChi — Discord Bot Commerce & Ops Platform

**[Live](https://oxchi.com)** · Discord bot satış paneli + runtime yönetimi

End-to-end platform: müşteri Discord ile giriş yapar, paket alır, botlarını panelden yönetir; operatör tarafında bot-manager PM2 process’lerini ayağa kaldırır.

| Area | Detail |
|------|--------|
| Auth | Discord OAuth, session cookies, ban / RBAC gates |
| Commerce | Bakiye, paketler, Shopier ödeme dönüşleri |
| Runtime | BullMQ kuyrukları, Redis pub/sub, canlı CPU/RAM/log WebSocket |
| Data | PostgreSQL (users, bots, orders) + MongoDB (ticket stats / transcripts meta) |
| Bot types | Ticket · Guard · Ekip · FiveM · Legal / Shop bot templates |

`Next.js` · `TypeScript` · `PostgreSQL` · `MongoDB` · `Redis` · `BullMQ` · `Discord.js` · `Docker` · `PM2`

<details>
<summary>Türkçe özet</summary>

Discord bot satış ve yönetim platformu. OAuth ile giriş, ödeme / bakiye, bot bazlı ayarlar, admin yetkileri ve Windows sunucuda PM2 ile gerçek process yönetimi. Redis + BullMQ ile kuyruklu start/stop; WebSocket ile canlı log ve metrik.

</details>

---

## Selected Projects · Seçili Projeler

### 1. Admin Dashboard
**SSR dashboard for metrics, roles & operations**

Repo: **[Oxgendev/nextjs-dashboard](https://github.com/Oxgendev/nextjs-dashboard)**

- Next.js App Router + TypeScript
- Role-based access patterns
- Maintainable UI architecture for real admin workflows

`Next.js` · `React` · `TypeScript` · `PostgreSQL`

<details>
<summary>Türkçe</summary>

Metrik ve yönetim için SSR dashboard. App Router, tip güvenliği ve uzun vadede bakımı kolay UI yapısı.

</details>

---

### 2. Database Migrations
**Practical migration patterns for evolving schemas**

Repo: **[Oxgendev/db-migrations-examples](https://github.com/Oxgendev/db-migrations-examples)**

- Safe schema evolution examples
- Patterns usable with Knex / Prisma-style workflows
- Focus on real release safety, not toy scripts

`JavaScript` · `SQL` · `Knex` · `Prisma`

<details>
<summary>Türkçe</summary>

Şema değişimlerinde güvenli migration örnekleri. Release sırasında veri kaybı riskini azaltmaya odaklı pratik kalıplar.

</details>

---

### 3. FiveM API
**TypeScript API layer for FiveM-related services**

Repo: **[Oxgendev/fivem-api](https://github.com/Oxgendev/fivem-api)**

- REST / service boundaries for game-server tooling
- Typed contracts between dashboard, bots, and runtime

`TypeScript` · `Node.js` · `REST`

<details>
<summary>Türkçe</summary>

FiveM ekosistemi için TypeScript API katmanı. Dashboard, bot ve runtime arasında typed kontratlar.

</details>

---

### 4. FiveM Lua
**Performance-sensitive Lua scripts for real-time game servers**

Repo: **[Oxgendev/fivem-lua](https://github.com/Oxgendev/fivem-lua)**

- Client–server validation
- State sync under load
- Tick / latency aware scripting

`Lua` · `SQL` · `Redis`

<details>
<summary>Türkçe</summary>

Gerçek zamanlı sunucular için performans odaklı Lua. Validasyon, state sync ve tick bilinci.

</details>

---

## Measurable Impact · Ölçülebilir Etki

| Area · Alan | Result · Sonuç |
|-------------|----------------|
| Server tick optimization | **6.8ms → 3.1ms** |
| API latency (p95) | **120ms → 70ms** |
| Database load | **~30–35% reduction** |
| Releases | **Zero data loss** across shipped updates |

---

## GitHub Snapshot

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Oxgendev&show_icons=true&theme=radical&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub Stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Oxgendev&layout=compact&theme=radical&hide_border=true&langs_count=8" alt="Top Languages" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Oxgendev&theme=radical&hide_border=true" alt="GitHub Streak" />

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=Oxgendev&theme=react-dark&hide_border=true&area=true" alt="Contribution Graph" width="100%" />

</div>

---

## Core Tech Stack · Teknoloji Yığını

### Languages · Diller
<p>
  <img src="https://skillicons.dev/icons?i=ts,js,python,lua,cpp,c" alt="Languages" />
</p>

| Strength | Detail |
|----------|--------|
| TypeScript / JavaScript | Primary stack — APIs, dashboards, product work |
| Algorithms & DS | Complexity-aware, readable problem solving |
| Lua / C++ / C | Performance-sensitive & systems-adjacent work |

### Frontend
<p>
  <img src="https://skillicons.dev/icons?i=react,nextjs,vue,html,css" alt="Frontend" />
</p>

React · Next.js (App Router, SSR, API routes) · Vue · HTML5 / CSS3

### Backend & Realtime
<p>
  <img src="https://skillicons.dev/icons?i=nodejs,express,discordjs" alt="Backend" />
</p>

- REST API design · AuthN / AuthZ (RBAC, sessions, OAuth)
- Event-driven systems · WebSockets · BullMQ job queues
- Discord bot platforms · FiveM integrations

### Databases & Cache
<p>
  <img src="https://skillicons.dev/icons?i=postgres,mysql,mongodb,redis" alt="Databases" />
</p>

| Tool | Role |
|------|------|
| **PostgreSQL** | Primary relational DB |
| MySQL | Mixed / legacy environments |
| MongoDB | Document workloads (bot stats, transcripts meta) |
| Redis | Cache, pub/sub, queues, heartbeats |
| Prisma · Knex · Mongoose | ORM / query layers |

### DevOps & Tooling
<p>
  <img src="https://skillicons.dev/icons?i=ubuntu,linux,bash,git,github,docker,githubactions" alt="DevOps" />
</p>

Ubuntu / Linux · Bash · Git / GitHub · Docker · GitHub Actions · PM2

---

## Domain Experience · Alan Deneyimi

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Web Platforms  │────▶│  Bot / Realtime  │────▶│  Game Servers   │
│  Next.js panels │     │  Discord.js      │     │  FiveM Lua/API  │
│  Billing / RBAC │     │  WS + queues     │     │  Tick & sync    │
└─────────────────┘     └──────────────────┘     └─────────────────┘
              │                    │                      │
              └──────────── PostgreSQL · Redis · MongoDB ─┘
```

- **SaaS-style commerce panels** — auth, roles, payments, customer self-serve
- **Ops tooling** — process managers, live metrics, safe restarts
- **Realtime / game-adjacent systems** — validation, sync, latency budgets

---

## How I Work · Çalışma Şeklim

| Practice | Why |
|----------|-----|
| `feature/*` · `fix/*` branches | Clear intent, easy review |
| Conventional commits | Readable history & changelogs |
| CI quality gates | Catch issues before merge |
| Semantic versioning | Predictable releases |
| Prefer boring, reliable solutions | Clever code ages badly |

---

## What I'm Exploring · Öğrendiğim / Denediğim

- Deeper **PostgreSQL** performance (indexes, EXPLAIN, connection pooling)
- **Queue / worker** patterns at scale (BullMQ, idempotency, retries)
- Cleaner **multi-tenant** bot/platform isolation
- Stronger **observability** (structured logs, health checks, heartbeats)

---

## Currently Open To · Açık Olduğum Fırsatlar

**EN**
- Backend Engineer / Full-Stack roles
- Teams shipping real products to real users
- Relocation to **Sweden** or elsewhere in the **EU**
- Environments that value ownership, code quality, and measurable impact

**TR**
- Backend / Full-Stack roller
- Gerçek kullanıcıya ürün çıkaran ekipler
- **İsveç** veya **AB**’ye taşınma
- Sahiplik, kod kalitesi ve ölçülebilir etki odaklı ortamlar

---

## Contact · İletişim

| | |
|---|---|
| Product | [oxchi.com](https://oxchi.com) |
| GitHub | [github.com/Oxgendev](https://github.com/Oxgendev) |
| LinkedIn | [Oğuzhan Salih](https://www.linkedin.com/in/o%C4%9Fuzhan-salih-622744374/) |
| Email | [brenfrank827@gmail.com](mailto:brenfrank827@gmail.com) |
| Discord | `oxgendev` |

---

<div align="center">

### Quick links · Hızlı linkler

[OxChi](https://oxchi.com) ·
[nextjs-dashboard](https://github.com/Oxgendev/nextjs-dashboard) ·
[db-migrations-examples](https://github.com/Oxgendev/db-migrations-examples) ·
[fivem-api](https://github.com/Oxgendev/fivem-api) ·
[fivem-lua](https://github.com/Oxgendev/fivem-lua)

<br/>

<sub>
Thanks for stopping by — always happy to talk about backend systems, databases, Discord platforms, or building products that scale.
<br/>
Uğradığın için teşekkürler — backend, veritabanı, Discord platformları veya ölçeklenen ürünler hakkında konuşmaya her zaman açığım.
</sub>

</div>
