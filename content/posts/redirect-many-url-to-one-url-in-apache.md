---
title: "Redirect Many URL to One URL in Apache"
date: 2009-02-13T00:00:00+08:00
tags: [apache, redirect, web, webserver]
draft: false
---

I recently faced a situation wherein I have to permanently redirect a list of URLs to a single URL. I'm used to doing it for 1 to 1 redirects(1 url to another) but this is the first time I did it for a lot of URL. 

Example:
* http://www.example.com/oldschool/index.php?i=1
* http://www.example.com/oldschool/index.cfm?i=55
* http://www.example.com/oldschool/SchoolOfRock.html
* http://www.example.com/oldschool/School-of-Knocks.htm

will need to be redirected to:
* http://www.example.com/university

The solution? Use the [RedirectMatch](https://httpd.apache.org/docs/2.4/mod/mod_alias.html#redirectmatch) directive in Apache.
It's so easy to use. Use the syntax:

```
RedirectMatch [status] regex URL
```

where status is 301(permanent redirect) or if not used will 302(temporary redirect) which can be used in you Apache's server config, virtual host, directory or .htaccess context.

In the above example, the exact RedirectMatch is:

```
RedirectMatch 301 ^/oldschool/(.*) http://www.example.com/university
```

###### NOTE: First published in my [now defunct blog](https://web.archive.org/web/20100927055819/http://www.buggedtech.com:80/).
