# PropertyGuard Frontend — Final Backend Integration

## Status

This frontend has been aligned to the verified PropertyGuard backend contract.

Backend checkpoint supplied for integration:
- Alembic: clean (`No new upgrade operations detected`)
- Backend tests: 126 passed, 0 failures, 0 errors
- Backend warnings: 2 non-blocking dependency warnings

## Major changes

### Authentication
- Removed demo login and hardcoded demo credentials.
- Login uses `POST /api/v1/auth/login` and `GET /api/v1/auth/me`.
- Registration uses the backend role contract.
- Public self-registration exposes Builder and Buyer only; Admin is not offered as a self-service role.
- Builder registration does not imply project-creation authorization. The UI reads the Builder verification profile and only enables project creation when the backend reports `VERIFIED`.

### Projects
- Project list uses `GET /api/v1/projects`.
- Project creation uses `POST /api/v1/projects`.
- Project deletion uses the backend deletion endpoint and is presented as a soft-delete/history-preserving action.
- Placeholder project records and fake local fallback projects were removed.
- Fake compliance scores were removed. A score is displayed only if the backend supplies a real value; otherwise the UI says `Not calculated`.

### Documents
- Document requirements are loaded from `GET /api/v1/projects/required-documents`.
- Upload flow is now:
  1. Backend file validation
  2. Document upload to the backend/MinIO flow
  3. Latest version retrieval
  4. Asynchronous processing request
  5. Backend document-status polling
- Client-side fallback validation and synthetic verification were removed.
- Documents remain PRIVATE in the upload flow.

### Compliance
- Evaluation uses the backend deterministic engine.
- Evaluation history and persisted results are displayed from the API.
- PASS / FAIL / NEEDS_REVIEW outcomes are shown as returned by the backend.
- No frontend-generated compliance result or regulatory conclusion is created.

### Findings
- Findings are retrieved from the backend.
- Finding status changes are sent through the real PATCH endpoint.
- Local-only finding simulations were removed.

### Landing page
- Removed fabricated audit metrics, fake properties, fake risk scores, fake regulatory findings, and the client-side bylaw calculator.
- Replaced them with an architecture/trust-boundary explanation that does not represent unimplemented regulatory logic as production functionality.

## Files added/changed

- `src/api/client.ts`
- `src/api/types.ts`
- `src/context/AuthContext.tsx`
- `src/types/auth.ts`
- `src/pages/auth/LoginPage.tsx`
- `src/pages/auth/RegisterPage.tsx`
- `src/pages/dashboard/DashboardPage.tsx`
- `src/pages/LandingPage.tsx`
- `src/components/layout/Navbar.tsx`

## Run locally

From the frontend directory:

```powershell
npm ci
npm run build
npm run lint
npm run dev
```

Set the backend URL if required:

```env
VITE_API_BASE_URL=http://127.0.0.1:8000
```

Do not commit production secrets into `.env`.

## Important backend constraints reflected in the UI

- Builder project creation requires a verified Builder profile.
- Builder-owned document APIs are restricted to the owning Builder by the backend.
- Compliance is deterministic and evidence-backed; AI is not treated as the regulatory authority.
- Compliance scoring is not shown until a real backend scoring layer exists.
- Risk/ML is not simulated by the frontend.

## Validation note

The source was statically checked for TypeScript/TSX syntax in this environment. A full Vite build could not be executed here because the uploaded frontend ZIP did not include `node_modules` and the environment could not retrieve the required npm packages. Run `npm ci`, `npm run build`, and `npm run lint` on the development machine as the final local validation step.

## Project Modify/Delete Controls

The project workspace now exposes project-management controls only after a project is selected:

- BUILDER: **Modify project** and **Delete project** for projects owned by that Builder.
- ADMIN / SUPER_ADMIN: **Modify project** and **Delete project** for accessible projects.
- BUYER: no Modify/Delete controls and no project-management API access.

Modify updates project name, description, property type, and address through `PATCH /api/v1/projects/{project_id}`.
Delete uses the existing soft-delete endpoint `DELETE /api/v1/projects/{project_id}` so historical records remain preserved.
