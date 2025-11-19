# Hi, I'm Oguzhan 👋

I'm a Full‑Stack developer building game server scripts (FiveM/Lua) and modern web/admin panels (JavaScript, React, Vue, Next.js). On the database side, I design schemas and manage migrations/rollbacks, indexing, and performance tuning across SQL, MySQL, PostgreSQL, and MongoDB. My goal: fast, reliable, and maintainable systems.

## 🚀 Featured Projects
- fivem-personal-scripts — Modular, low‑tick script set for QBCore/ESX. Easy setup, clean structure, solid docs.
- fivem-api — REST API for server stats, whitelist, and user management. Node.js + Express, PostgreSQL/MongoDB, Redis caching.
- nextjs-dashboard — Management panel for metrics, whitelist, and script control. Next.js + Tailwind + Prisma/Knex.

## 🧰 Tech Stack
`Lua` `Python` `JavaScript` `TypeScript` `React` `Vue` `Next.js` `Node.js` `Express`  
`SQL` `MySQL` `PostgreSQL` `MongoDB` `Redis` `Prisma` `Knex` `Mongoose`  
`Docker` `GitHub Actions`

## 📈 Measurable Results
- Tick optimization: average ms 6.8 → 3.1 (lower resource usage in FiveM scripts)
- Redis caching + proper indexing: API p95 120ms → 70ms
- Migration/rollback discipline: zero data loss during releases; DB load −30–35% with pool tuning

## 🗂 Database & Migration Approach
- Schema Design: clear relations, unique/index on critical fields (e.g., `steamHex`), audit fields (`createdAt`).
- Migrations/Rollback: versioned flows with Prisma or Knex; automated in CI; safe rollback scenarios.
- Indexing & Query Plans: validate with `EXPLAIN/EXPLAIN ANALYZE`; btree/unique combos; avoid N+1 and full scans.
- Seed & Backups: minimal but meaningful seed; `pg_dump/mysqldump/mongodump` with release tags.
- Pooling & Cache: pool `max`/timeouts; read‑heavy caching layer; invalidation strategies.

## 🧪 Quality & Process
- Tests & CI: lint, test, build automation (luacheck for Lua; lint/test for Node/Next).
- Documentation: clear README with setup, config, and example scenarios.
- Versioning: semantic versioning with concise release notes.

## 📫 Contact
- LinkedIn: https://www.linkedin.com/in/o%C4%9Fuzhan-salih-622744374/
- GitHub: https://github.com/Oxgendev
- Email: brenfrank827@gmail.com
- Discord: oxgendev
