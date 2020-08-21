--- 
date: 2020-08-21T10:58:44+08:00
title: "Enforcing Always HTTPS in Github Pages"
tags: [enforced-https, always-https]
draft: false
--- 

For those who knows how to look, this personal site of mine is hosted in Github Pages.

I have my notes in https://ismael.casimpan.com/quicktasks. Each individual quicktask is a repo (e.g https://github.com/icasimpan/quicktasks-drupal.git) with TravisCI integration that builds it.

However, I noticed that some of my quicktasks are not always https or is not redirected automatically.
I never mind those before, but today, I was curious as to why. I know now...

There is this option in github repo settings called "Enforce HTTPS". 
Just tick it and the github pages always gets redirected to https.
