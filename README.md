# Clio Astra — Git & Cloud Run Workshop

A small Flask service used to teach a team the basic **Git/GitHub collaboration flow** (clone → commit → push → pull request), and to demonstrate deploying a containerized app to **Google Cloud Run**.

The app does one thing: it reads `COLABORADORES.md` and serves it over HTTP. The point isn't the app — it's that every collaborator had to go through a real branch-and-PR cycle to get their name onto the page.

## How it works

```
COLABORADORES.md  ──read──>  app.py (Flask)  ──serves──>  GET /
                                  │
                                  └── Docker ──> Cloud Run (port 8080)
```

`app.py` listens on `0.0.0.0` and reads the `PORT` environment variable (defaulting to 8080), which is what Cloud Run requires.

## Run locally

```bash
pip install -r requirements.txt
python app.py
# http://localhost:8080
```

## Run with Docker

```bash
docker build -t clio-astra .
docker run -p 8080:8080 clio-astra
```

## Contributing (the exercise)

1. Clone the repository
2. Add your name, role and an interest to `COLABORADORES.md`
3. `git add COLABORADORES.md && git commit -m "Agrego mi nombre a la lista"`
4. `git push` and open a pull request

## Tech

`Python 3.9` · `Flask` · `Docker` · `Google Cloud Run`
