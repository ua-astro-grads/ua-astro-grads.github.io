---
title: How to edit this site
---

Whenever new commits are added to https://github.com/ua-astro-grads/ua-astro-grads.github.io, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in the site from the content in the repository.

## Posting your talk materials

**The short version:** To make a new post, you will need to
fork a copy of `ua-astro-grads/ua-astro-grads.github.io` to your GitHub account, clone it, commit and push your changes with `git`, and open a pull request.

The steps are described here, but you can always ask any of the organizers if you want help!

### Forking and cloning

Make sure you are logged in to GitHub. The page for this repository is [https://github.com/ua-astro-grads/ua-astro-grads.github.io](https://github.com/ua-astro-grads/ua-astro-grads.github.io), and there is a button labeled "Fork" at the upper left. (You can also go directly to <a href="https://github.com/ua-astro-grads/ua-astro-grads.github.io/fork" target="_blank">https://github.com/ua-astro-grads/ua-astro-grads.github.io/fork</a>.) Choose to fork the repository to your own account.

After the fork is made, you will see a copy of the repository at `your-user-name/ua-astro-grads.github.io`. Click the green _Clone_ button, copy the URL shown, and open a terminal. To create a local copy of the site, open a terminal and `git clone` using the URL (e.g. `git clone https://github.com/your-user-name/ua-astro-grads.github.io.git`).

### Writing your post

Change into the `_posts` subdirectory the `git clone` just created:

```
cd ua-astro-grads.github.io/_posts
```

Copy the example post, changing the date and title for your own (and dropping the `.example`):

```
cp YYYY-MM-DD-blog-post.md.example 2017-09-13-achieving-maximum-website.md
```

Edit the new file to your living using [Markdown](https://guides.github.com/features/mastering-markdown/) syntax. The post can contain any content you wish, as long as it begins with front-matter giving the full title and your name.

### Attaching your slides or notebooks

There is a `downloads` folder in the root of the repository with subfolders by year to keep things organized (e.g. `downloads/2017/`). If you place your file in there, you can link to it from your post with this syntax:

    [link text](/downloads/2017/filename.pdf)


### Previewing your post

It's a good idea to preview your post before publishing. You may need to install Jekyll, if you haven't used it before: `gem install jekyll bundler`. Once that's done, you can preview your post at http://127.0.0.1:4000/ with `bundle exec jekyll serve` (run in the `ua-astro-grads.github.io` directory).

### Pushing your changes

  1. Verify which files have been added or modified: `git status`
  2. Add them to the commit staging area: `git add _posts/YYYY-MM-DD-title-without-spaces.md downloads/2017/filename.pdf` (Note that you must list any files you placed in `downloads/` as well as the post itself.)
  3. Commit with a descriptive message: `git commit -m "Added Annie Cannon's talk about stellar classification"`
  4. Push: `git push origin master` (or a different branch besides `master`, if you prefer)

### Creating a pull request

Once you have pushed your changes, visit the page for your clone on GitHub. You will see an indicator showing your changes are "ahead of ua-astro-grads:master" and a link to create a pull request.

![Screenshot of GitHub pull request link](/assets/create_pull_request.png)

Fill out the resulting form to propose your changes, and GitHub will alert the organizers. Once it is merged by one of the organizers, the changes should go live on https://ua-astro-grads.github.io/ within a few minutes.
