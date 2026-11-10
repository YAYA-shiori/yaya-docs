# GETENV
**Category:** システム情報

## Signature
```
GETENV( name )
```

## Parameters
| Parameter | Description |
|-----------|-------------|
| name | The name of the environment variable to retrieve (string) |

## Returns
- On success: The contents of the environment variable (string)
- On failure: An empty string

## Description
Gets an OS environment variable by name. Returns an empty string if the specified environment variable does not exist. The argument cannot be omitted; if it is omitted, a warning (W0008) is issued and an empty string is returned.

There are currently no plans to implement a function for setting environment variables, since changing them carelessly can be dangerous.

## Compatibility
- YAYA: Tc552-1 and later
