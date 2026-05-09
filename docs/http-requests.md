# HTTP Requests in Python

**Relevant script:** [`scripts/fetch_git_api.py`](../scripts/fetch_git_api.py)

## What is `requests`?

`requests` is a third-party Python library for making HTTP calls. It is the standard choice for fetching data from APIs and web pages.

If you're coming from JavaScript, the mental model maps cleanly:

| JavaScript | Python |
|---|---|
| `urllib` (built-in) | `fetch` (built-in) |
| `requests` (third-party) | `axios` (third-party) |

Python's built-in `urllib` works but is verbose — you have to manually encode params, decode responses, and handle errors in detail. `requests` wraps all of that with a clean, readable API, which is why it became the de-facto standard.

## Basic usage

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)  # 200 means OK
print(response.json())       # parses the JSON response body
```

## Common patterns

```python
# POST with a JSON body
response = requests.post("https://api.example.com/users", json={"name": "Aayush"})

# Pass query params (appended to the URL automatically)
response = requests.get("https://api.example.com/search", params={"q": "python"})

# Add headers (e.g. for auth)
response = requests.get(url, headers={"Authorization": "Bearer <token>"})
```

## Key difference from JavaScript

`requests` is **synchronous by default** — it blocks until the full response arrives. There is no `await`. For async HTTP in Python, `httpx` is the modern alternative, but `requests` covers the vast majority of use cases in this course.

## Installing

```
uv add requests
```
