---
title: Notes to editors
---

You can use the [editor on GitHub](https://github.com/ua-astro-grads/code-coffee/edit/master/README.md) to maintain and preview the content for this website in [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/) files.

If you prefer to work locally, `git clone https://github.com/ua-astro-grads/code-coffee.git` to get a local copy in `code-coffee`. You may need to install Jekyll, if you haven't used it before: `gem install jekyll bundler`. Once that's done, you can preview your site at http://127.0.0.1:4000/ with `bundle exec jekyll serve`.

Whenever you commit and push to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

## Posting your talk materials

To make a new post, you will need to [fork](https://github.com/ua-astro-grads/code-coffee/fork) a copy of `ua-astro-grads/code-coffee` to your GitHub account, clone it, commit and push your changes with `git`, and [open a pull request](https://help.github.com/articles/creating-a-pull-request/). Ask any of the organizers if you want help!

### Writing your post

Create a new [Markdown](https://guides.github.com/features/mastering-markdown/) file in the `_posts` directory. It should be named following this format: `YYYY-MM-DD-title-without-spaces.md` (where `YYYY-MM-DD` are the year, month, and day of your presentation).

The post can contain any content you wish, as long as it begins with front-matter giving the full title and your name:

```
---
author: Annie Jump Cannon
title: "Stellar classification"
---
```

### Attaching your slides or notebooks

There is a `downloads` folder in the root of the repository with subfolders for academic years (e.g. `2017-18`). If you place your file in there, you can link to it from your post with this syntax:

```
[link text]({{ site.url }}/downloads/2017-18/filename.pdf)
```

### Publishing your post

  1. Verify which files have been added or modified: `git status`
  2. Add them to the commit staging area: `git add _posts/YYYY-MM-DD-title-without-spaces.md downloads/2017-18/filename.pdf`
  3. Commit with a descriptive message: `git commit -m "Added Annie Cannon's talk about stellar classification"`
  4. Push: `git push origin master` (or a different branch besides `master`, if you prefer)
  5. [Create a pull request](https://github.com/ua-astro-grads/code-coffee/compare) on the main shared repository

Once it is merged by one of the organizers, the changes should go live on https://ua-astro-grads.github.io/code-coffee/ within a few minutes.
