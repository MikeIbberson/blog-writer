# blog-writer

Static site for the essays in `catalogue/`, built with [Eleventy](https://www.11ty.dev/) and deployed to GitHub Pages at `/blog-writer`.

## Local preview

```bash
npm install
npm start
```

Open the URL Eleventy prints (typically `http://localhost:8080/blog-writer/`). The path prefix matches production so links and assets behave the same way.

## Build

```bash
npm run build
```

Output lands in `_site/`.

## Deploy

1. Create a GitHub repository named `blog-writer` and push this project to `main`.
2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Push to `main` (or run the **Deploy to GitHub Pages** workflow manually). The site will be at `https://<username>.github.io/blog-writer/`.

Essays are read from `catalogue/*.md`; images from `catalogue/assets/`. Add a new numbered markdown file there and it will appear on the home page after the next build.
