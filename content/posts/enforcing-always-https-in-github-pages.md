--- 
date: 2020-08-21T10:58:44+08:00
title: "Enforcing Always HTTPS in Github Pages"
tags: [enforced-https, always-https]
draft: false
--- 

For those who knows how to look, this personal site of mine is hosted in Github Pages.

I have my notes in https://ismael.casimpan.com/quicktasks. Each individual quicktask is a repo (e.g https://github.com/icasimpan/quicktasks-drupal.git) with TravisCI integration that builds it.

However, I noticed that some of my quicktasks are not always https or is not redirected automatically.
Look at the http headers for (QuickTask for Postfix)[ismael.casimpan.com/quicktasks-postfix] when accessing it without the protocol:

![Visit Quicktask Postfix without protocol - before enforced https](/images/githubpage_after_enforcedhttps.png)

I never mind those before, but today, I was curious as to why. I know now...

There is this option in github repo settings called "Enforce HTTPS".
![Settings to Enforce HTTPS](/images/githubpages_setting_enforcedhttps.png)
Just tick it and the github pages always gets redirected to https.

After cache is cleared by github pages, here's the same visit via curl:
![Visit Quicktask Postfix without protocol - after enforced https ](/images/githubpage_no_enforcedhttps.png)

More details in (Github's Documentation for enforced https)[https://docs.github.com/en/github/working-with-github-pages/securing-your-github-pages-site-with-https]
