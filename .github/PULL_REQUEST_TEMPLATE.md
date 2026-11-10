## What this changes

<!-- One or two sentences. What is different after this PR? -->

## Why

<!-- The problem this solves. Link the issue: Closes #123 -->

## How it was verified

<!-- Exact commands or manual steps. Paste CI-relevant output. -->

```bash
# Backend
npm run build
npm test -- --runInBand

# Frontend
npm run type-check
npm test
npm run build
```

- [ ] Backend build passes
- [ ] Backend tests pass
- [ ] Frontend type-check passes
- [ ] Frontend tests pass
- [ ] Frontend build passes
- [ ] No secrets, credentials or `.env` values in the diff
- [ ] Schema changes include a Prisma migration
- [ ] New behaviour is covered by a test
- [ ] Docs updated if public behaviour changed

## Notes for the reviewer

<!-- Anything unusual: trade-offs, follow-ups, areas you want scrutinised. -->
