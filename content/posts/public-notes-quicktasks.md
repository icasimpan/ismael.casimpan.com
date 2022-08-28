--- 
date: 2022-08-28T19:40:13+08:00
title: "Public Notes: Quicktasks"
tags: [quicktasks]
draft: false
--- 

As you can see, I only had a a handful of blog posts since. 

Writing for the sake of it isn’t my forte but focused and a quick one is.

Quick notes is how I’ve done it since about 2010. I still remember the first internal documentation I made for the sparsely documented tool our Team was using. I called it SEA (for Slightly Explored Areas).

After I moved to another company, I copied the same idea into an internal confluence pages as quick notes, separated per technology like:

* quicktasks - AWS
* quicktasks - Drupal
* quicktasks - Ansible
* quicktasks - Acquia
* quicktasks - Git

The above are a sample but I had about 19 major categories.

I document things that aren’t obvious (at least to me and the Team). Then I discovered Hugo and that’s how I started porting the internal confluence pages to GitHub with each repos. 
Since my site was hosted in GitHub Pages back then, I created a TravisCI automation to compile the the Hugo site to static and push it as ghpages branch. With that, a virtual subfolder for my site is created for each category like:

* ismael.casimpan.com/quicktasks-aws
* ismael.casimpan.com/quicktasks-drupal
* ismael.casimpan.com/quicktasks-ansible
* ismael.casimpan.com/quicktasks-acquia
* ismael.casimpan.com/quicktasks-git

And the main link at https://ismael.casimpan.com/quicktasks lists all those quick tasks.

Then I created a tool to manage creating “new quick tasks”. 

BUT as you can see, maintenance increases as the number of quick tasks grows. So I consolidated it.

Then came the time when I was adding a lot of entries that my free allocation for Travis got exhausted…and GitHub pages for some reason fails to load my site. So I moved the main site and it’s now in Cloudflare Pages and the quicktask site in Netlify.

And yes, if you’re interested to get all the quick task I have so far, it’s public so you can git clone it:

* https://github.com/icasimpan/quicktasks.ismael.casimpan.com

Enjoy!
