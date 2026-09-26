---
author: "Vikram Manikantan, Noah Franz"
title: "How to Develop with StewarXiv"
---

Vikram and Noah walked through [StewarXiv](https://github.com/ua-astro-grads/arxiv-mailer), the daily mailer that matches new arXiv postings with Steward researchers.

[Slides](https://docs.google.com/presentation/d/1_gfUgGdv_6dz3RN6UfoAwF5uOhrcWt_tKQH0YixlmS4/edit?usp=sharing) (Google Slides)

## Code Coffee Reboot

First we discussed the purpose of Code Coffee moving forward. Code Coffee is an informal, community-driven meeting to discuss common coding tools and concepts in astronomy/astrophysics. We encourage hands-on tutorials.We're always looking for volunteers to lead sessions. You can suggest topics or sign up to lead one on the [spreadsheet](https://tinyurl.com/stewardcode).

## How StewarXiv works

1. Pull the daily arXiv RSS feeds
2. Build a directory of names from the Steward website
3. Crossmatch Steward names with arXiv author lists (approximate name matching plus affiliation checks in the LaTeX source)
4. Render the email with Jinja2 and send it to the mailing list

Each step has room for improvement. See the [open issues](https://github.com/ua-astro-grads/arxiv-mailer/issues) if you'd like to contribute.

## Deployment workflow

1. Develop locally
2. Open a PR and merge to `main`
3. Build a new Docker image and push it to Docker Hub
4. The new image is pulled and run automatically

## Running it locally

```
git clone https://github.com/ua-astro-grads/arxiv-mailer.git
cd arxiv-mailer
python3 -m venv mailer_env
source mailer_env/bin/activate
python3 -m pip install -r requirements.txt
```

Or run the Docker image, which needs mail credentials (your CatMail secondary password and SMTP settings):

```
mkdir logs
docker run -e MAIL_USERNAME=<username> -e MAIL_PASSWORD=<password> \
  -v logs:/arxiv-mailer/logs noahfranz13/stewarxiv:v0.1
```

During the session, we demo'ed how to pull the repo, run the code, and generate the HTML email without sending it. See the [README](https://github.com/ua-astro-grads/arxiv-mailer) for details.
