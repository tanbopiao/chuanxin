# AgentGPT Revival

**A community revival of [reworkd/AgentGPT](https://github.com/reworkd/AgentGPT) — where the community's fixes finally merge.**

> The upstream collected 1,082 pull requests and 469 issues. The last merge was **2025-04-29**. Even the founder's own PRs sat unmerged. This fork exists to land them.

## Why this fork

AgentGPT was one of the fastest-growing open-source projects of 2023 (36k+ stars) — an autonomous AI agent you assemble and deploy in your browser. Then the maintainers moved on. The community kept filing fixes: broken Docker builds, database config errors, crash fixes, dependency security bumps — 87 pull requests waiting, some for over two years.

This revival fork picks up where upstream stopped:

| What's stuck upstream | What we do here |
| --- | --- |
| Docker build broken since the Debian base image deprecation (#1689) | Fix the build first — the project must run again |
| Poetry/Python package conflicts (#1666) | Restore a working install path |
| 10 real bug fixes unmerged (#1663 #1653 #1602 #1601 #1551 #1335 #1063 #1039 …) | Absorb with full attribution |
| 51 stale dependency bumps (15 superseded) | One modernization pass, credited per package |
| Founder PRs unmerged (#971 #1053) | Landed with priority, as a matter of respect |
| 418 contributors unacknowledged | Full credit roll in [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md) |

## Governance

- **[Triage matrix](docs/TRIAGE-MATRIX.md)** — all 87 open upstream PRs dispositioned: fixes, features, docs, deps, rejects. Only-increase, never overwrite.
- **[Absorption ledger](docs/ABSORPTION-LEDGER.md)** — every landed change mapped to its upstream source.
- **[ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md)** — all 418 contributors credited by name.
- **License**: GPL-3.0, unchanged from upstream (see [LICENSE](LICENSE), [NOTICE](NOTICE)).

## Contributing

Were your PRs or issues stuck upstream? They're dispositioned here. Open an issue referencing your upstream PR number and we'll prioritize it. See [CONTRIBUTING guide](docs/developers/README.md) for setup.

## What is AgentGPT?

🤖 Assemble, configure, and deploy autonomous AI agents in your browser. See the [original README](docs/README-upstream.md) and the [multilingual docs](docs/README.zh-HANS.md).

---

*This fork is not affiliated with or endorsed by reworkd. Original copyright preserved.*
