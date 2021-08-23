# Contributing to Code-Soup
This project is a community effort, and everyone is welcome to contribute! Feel free to join the [Slack Workspace](https://join.slack.com/t/ssoc2021/shared_invite/zt-u4eefbut-aX7TYc1WoQWgylPydivUlg)

If you are interested in contributing to code-soup, there are many ways to help out. Your contributions may fall
into the following categories:

1. It helps us very much if you could
    - Report issues you’re facing
    - Give a :+1:  on issues that others reported and that are relevant to you
    - Spread a word about the project or simply :star: to say "I use it"

2. Answering queries on the issue tracker, investigating bugs and reviewing other developers’ pull requests are
very valuable contributions that decrease the burden on the project maintainers.

3. You would like to propose a new feature and implement it
    - Post about your intended feature, and we shall discuss the design and
    implementation. Once we agree that the plan looks good, go ahead and implement it.
4. You would like to implement a feature or bug-fix for an outstanding issue
    - Look at the issues labelled as ["good first issue"](https://github.com/Adversarial-Deep-Learning)
    - Pick an issue and comment on the task that you want to work on this feature.
    - If you need more context on a particular issue, please ask and we shall provide.


# Directory Structure
The website is structured like a book as shown below:
```bash
.code-soup-website/
+-- adl/ #main package
|	+-- chapter-x/ #Front Matter for a particular chapter 
|	|	+--{Name_of_Page}.md #There can be any number of pages for every chapter
|	|	+--index.md #Contains brief summary of the chapter as well as config for navigation
+-- assets/ #Display files for the website
|	+-- chapter-x/ #Assets for a particular chapter
+-- _site/ #Auto Generated Site that can be used for deployment
```
Note that each chapter in the frontend matter will contain a compulsory ```index.md``` file. Each of these files contain metadata that will help populate the navigation panel as well as the search box. 
```markdown
layout: default
title: Chapter X
parent: Adversarial Deep Learning
has_children: true
```
More details about how the navigation panel is populated can be understood further with: [Just The Docs](https://pmarsceill.github.io/just-the-docs/)

## Resources
To learn more about jekyll you can:
1. Go through the [official tutorial blog](https://jekyllrb.com/tutorials/home/) on Jekyll
2. Watch a [youtube crash course](https://www.youtube.com/watch?v=T1itpPvFWHI&list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB) on jekyll. 

Contributors can keep adding to this list for links they find useful.

#### Send a PR

If everything is OK, please send a Pull Request to <https://github.com/Adversarial-Deep-Learning>

If you are not familiar with creating a Pull Request, here are some guides:
- <http://stackoverflow.com/questions/14680711/how-to-do-a-github-pull-request>
- <https://help.github.com/articles/creating-a-pull-request>
