# Error Handling

Define a stable error model.

For each error:
- HTTP status
- application error code
- safe user-facing message
- internal logging detail
- retryability
- frontend behavior

Never leak stack traces, SQL details, tokens, secrets or sensitive internals to clients.
