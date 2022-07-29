---
title: "SHCF: Shell Scripting Dev't Kit and Coding Framework"
date: 2022-07-28T21:32:00+08:00
tags: [shcf, open source]
draft: false
---

# WHAT'S SHCF?

If you've used the previous version of SHCF, now you would use it even more. SHCF is no longer just a Shell Coding Framework but a Shell Scripting Development Kit as well. Where before you used to get one for free, now you'll get two and still for free!

Ok, enough of the convincing lines. Seriously, I wrote this tool as I needed it myself and I've noticed that there's practically nothing that satisfies my definition of light and simple framework for shell scripting. I'm sharing this with you so that hopefully, it would help you create shell scripts faster and with focus on your scripting and not on how this framework works.

A little disclaimer though: we only support **bash** at the moment.

Anyway, as I've already told you, this is no longer just a shell coding framework. This is a scripting development kit and you generate the coding framework out of it. I'll show you how it works.

# QUICK USAGE GUIDE

1. Create a new shcf-based shell script
```
~$ git clone https://github.com/shsdk/shcf.git
~$ ./shcf/core/bin/shcf_cli init
~$ shcf_cli new hello_world
```

2. Add basic logic, say the greeter() function
```
~$ shcf_cli lib hello_world greeter
```

3. Modify `hello_world/lib/greeter.bash.inc` to say **hello world**

4. Update main script `hello_world/bin/hello_world` so it calls `greeter`

   TIP: Add it to `autoload_functions` line

5. For additional scripts into your project say `whoami`:
```
~$ shcf_cli hello_world whoami
```

6. Further usage, help is available. Just run:
```
~$ shcf_cli help
```

# DETAILED USAGE GUIDE

1. Clone the shcf project:
```
~$ git clone https://github.com/shsdk/shcf.git
```

2. Initialize the environment
```
~$ ./shcf/init.sh
   Platform environment has been set. See below:
     SHCF_PLATFORM_ROOT=/home/your_username/shcf/core
```

At this point, you can use `shcf_cli` from any path so long as you don't use `exit`.

3. Now, create a new project. Example, `hello_world`
```
~$ shcf_cli new your_project_dir/hello_world
```

A successful creation should be something like below:
```
~$ shcf_cli new your_project_dir/hello_world
   template script created in your_project_dir/hello_world/bin/hello_world
   Successful creation of your_project_dir/hello_world
```

4. Make the template binary in **bin** executable
```
~$ chmod u+x ./your_project_dir/bin/hello_world
```

5. Template script is not yet ready. If you insist on running it like below:
```
~$ ./hello_world
```

Expect to see the following error:
```
/home/your_username/your_project_dir/hello_world/lib/autoload_functions.bash.inc: line 26: /home/your_username/your_project_dir/hello_world/lib/rename_function1.bash.inc: No such file or directory
 ERROR: Missing required rename_function1
 /home/your_username/your_project_dir/hello_world/lib/autoload_functions.bash.inc: line 26: /home/your_username/your_project_dir/hello_world/lib/rename_function2.bash.inc: No such file or directory
 ERROR: Missing required rename_function2
 /home/your_username/your_project_dir/hello_world/lib/autoload_functions.bash.inc: line 26: /home/your_username/your_project_dir/hello_world/lib/rename_functionX.bash.inc: No such file or directory
 ERROR: Missing required rename_functionX
```

Template **View** (see MVC pattern in **INSPIRATION** section below) included 3 functions that where meant to be replaced or removed, hence the error. 
To fix the problem, go to the **Model** (or `lib` directory) and create a function named 'greeter()' (as file greeter.bash.inc) with contents below:

```
greeter() {
	   local message=$1
	   echo "$message!"
	}
```

TIP: Another approach is to create a template file using command
```
~$ shcf_cli lib hello_world greeter
```

In `bin/hello_world`, remove the 3 template functions namely:
```
 rename_function1
 rename_function2
 rename_functionX
```

and replace it with `greeter`.

Below, the comment block:

```
 ## ..............................
 ## main utility tool starts below
 ## ..............................
```

add the line:
```
 greeter "Hello, World"
```

Of course, save the file.
Re-run:
```
~$ ./hello_world
```

If you followed the instructions correctly, you should see the greeting:
```
~$ ./hello_world
    Hello, World!
```

6. Now, if you want to add additional script to your project, that is easy. Let's assume you want to create `whoami`. Just run the command:
```
~$ shcf_cli bin hello_world whoami
```

Same instructions as above, put the logic, make it executable and you're on. 

7. For other usage, help is available. Just run:
```
~$ shcf_cli help
```

# PACKAGE BUILDS

For people who are more comfortable with the usual package installation, SHCF is now available for the two major Linux packages: **rpm** and **deb**.

To install rpm, run the following:
```
~$ curl -s https://packagecloud.io/install/repositories/icasimpan/shcf/script.rpm.sh | sudo bash
```

For deb installation, run:
```
~$ curl -s https://packagecloud.io/install/repositories/icasimpan/shcf/script.deb.sh | sudo bash
```

Package hosting generously provided [PackageCloud.io](https://packagecloud.io)

# INSPIRATIONS

1. **Model-View-Controller(MVC) pattern** I am not fully sure if I understand the MVC pattern correctly, but in my own understanding:

* **Model** is the business logic or the *"how"* of this framework. It is the one that bears the burden on how a specific functionality is to be carried out. 
  In this framework, you can see the 'model' inside "lib", like `sqlQuery.bash.inc`

* **View** is the frontliner, the one that faces the demanding customer, the end-user. Up to this point, there are no example 'view' yet but it the near future, it is the script
  that uses this framework which can be considered as the 'view'

* **Controller** is the mediator/middle-man directing the requests of the demanding customer(via 'View') to the corresponding 'model'.
  For instance, we have a script that does an SQL query. The script(also called the 'view'), having been asked by the demanding customer to do
  an SQL query, would look up through the 'controller' if an sql-query 'model' can be found. Controller then knows how to locate such 'model'. 
  In this framework, controller is called *etc/controller.bash.inc* which should be included in every scripts that uses this framework.  


2. auto-loading in PHP Having seen a lot of shell scripts with functions being duplicated across scripts made me realize how it is a maintenance nightmare. A slight change in functionality on the main tool it is supporting would mean changing a lot of scripts. So I made a roughly similar functionality in this framework so that only one function would be made and will simply be called in each script that needs it. Maintenance would be easily done quickly. In this framework, it can be seen in lib/autoload_functions.bash.inc and will be called in script something like

```
autoload_functions "func1 func2 func3 etc"
```

The above way to call autoload_function means that functions is directly accessible from lib and NOT inside directories within lib. To reference a function stored in a directory within lib prefix it with the directory relative to lib. For example to use sqlQuery function which is stored in lib/db/sql/mysql and ishost_up located in lib/box_mgt you will call autoload_function like
```
autoload_functions "lib/db/sql/mysql/sqlQuery box_mgt/ishost_up"
```

In short, calling stays relatively the same, only that you have to prefix each function with directory name in which it is stored.

