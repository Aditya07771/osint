# LTCOE Q3 — Git Forensics (public redacted demo)

This repository hosts the **generated challenge artifact** for a git-archaeology
CTF. It is a demo instance with the final flag redacted.

## Branches

| branch | contents |
|--------|----------|
| `main` | challenge tooling `.gitignore` only |
| `challenge-main` | 10,026 commits, the primary history |
| `challenge-nightly` | the short `nightly` line, 8 commits |
| `challenge-archive-leak-scrub` | normally-dangling commit holding `SECURITY_NOTE.md` |
| `challenge-archive-typo` | normally-dangling commit holding a decoy |

Tags `v0.9.0`, `v1.0.0`, `v1.1.0`, `v2.0.0` are present.

The two `archive/*` branches exist because those commits are unreachable from any
real ref. Without them a clone would be missing the artifact stage 10 depends on.

## Getting the artifact

```bash
git clone https://github.com/Aditya07771/osint.git
cd osint
git checkout challenge-main
git log --oneline | wc -l     # 10024
git branch -a
git tag
```

10,028 commits are reachable across all branches; 10,024 sit on `challenge-main`.

## Redaction — read this before using it as a challenge

The audit sample that stage 11 points at reads:

```
LTCOE{redacted_public_demo}
```

**Stages 1 through 10 are fully solvable in this instance.** Stage 11's mechanical
step works — you will find the tag, read the file, and see the placeholder above.
The live flag is not in this repository, in any of its objects, or in any commit
message. Verified by scanning all 52,238 objects in the object database before
publication.

There are also three planted decoys, all present here:
`LTCOE{almost_had_it}`, `LTCOE{nice_try_docker_layer}`, `LTCOE{not_this_one}`.

If you want to run this as a real challenge, generate your own instance from the
builder rather than cloning this one — see the tooling repo. Setting the flag is a
build-time environment variable.

## SHAs do not match the private writeup

The redacted audit blob changes the root commit's tree, so every SHA after it
differs from the writeup for the private instance. The puzzle structure, stage
titles and intended techniques are identical; only the hashes are different. Any
SHA-based answer key must be regenerated from this tree.

## Layout

The challenge project root (`challenge-repo/`, builder, verifier, solution key,
writeup) is **not** in this repository. The artifact was published as loose refs
into a clean repo so that no solution material could be committed by accident.
