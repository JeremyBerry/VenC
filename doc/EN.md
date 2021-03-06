![VenC](https://download.tuxfamily.org/dsalem/img/2017_-_Denis_Salem_-_CC_By_SA_-_VenC-logo.svg "VenC")

# Version 1.2.0

1. [Presentation](#presentation)
2. [Installing](#installing)
3. [Uninstalling](#uninstalling)
4. [Taking your marks](#taking-your-marks)
	1. [File Tree](#file-tree)
	2. [Files structure](#files-structure)
		1. [Main config file](#main-config-file)
		2. [Templates](#templates)
		3. [Publications](#publications)
		4. [Themes](#themes)
	3. [Pattern Processor](#pattern-processor)
		1. [Templates Patterns](#templates-patterns)
		2. [Over Global Patterns](#over-gloabal-patterns)
		3. [Publications Patterns](#publications-patterns)
		4. [Special Patterns](#special-patterns)
	4. [Environment variables](#environment-variables)
		1. [blog_configuration.yaml](#blog_configurationyaml)
		2. [Pattern variables](#pattern-variables)
5. [Commands](#commands)
	1. [Print VenC's version](#print-vencs-version)
	2. [New Blog](#new-blog)
	3. [New publication](#new-publication)
	4. [Display available themes](#display-available-themes)
	5. [Exporting the blog](#exporting-the-blog)
	6. [Remote copy](#remote-copy)
	7. [Exporting the blog online](#exporting-the-blog-online)
	8. [Edit a file on the blog and recompile automatically the blog](#edit-a-file-on-the-blog-and-recompile-automatically-the-blog)
	9. [Install theme](#install theme)
9. [Installer theme](#install-theme)
6. [Themes](#themes-1)
	1. [Installing](#installing-1)
	2. [Plugins](#plugins)
		1. [Infinite scrolling](#infinite-scrolling)
		2. [Clientside search engine](#clientside-search-engine)

# Presentation

VenC is a python application written for linux and similar to [Octopress](http://octopress.org)/[Jekyll](http://jekyllrb.com) to create and administrate your static blogs using the commandline. Using VenC, everything is text file, no database. Every blog's configuration is based on one unique and small Yaml file, themes consist in a handful of HTML templates to modify or to create yourself, on publications' side, they have one YAML part and one Markdown part.

Static blogs are fully adapted for darknets or for those who want a full control on their website without having to deal with heavy and potentially vulnerables CMS in security matter. Moreover, the extreme simplicity of the organisation of blogs' sources outcome from VenC guaranties a fast and efficient handling.

Also, here is what VenC has to offer:

- From version 1.0.0
 - Creation of static blog (HTML/CSS).
 - Simple page layout that you can directly personalize using HTML/CSS.
 - Ability to create an arrangement in an arbitrary number of columns.
 - Infinite scrolling module simple and easy to setup.
 - Publications can be organised by categories and sub-categories.
 - Publications can be organised by date periods.
 - Up or down chronologic publicating.
 - RSS feeds for every publications thread.
 - Permalinks.
 - Managing and editing the blog entirely via the commandline.
 - VenC is designed to run on GNU/Linux specifically.
 - Publication's redaction in markdown.

- Since version 1.1.0
 - Blog exportation via ftp.
 - Syntax coloration.
 - Recursive patterns detection.
 - Using variables containing weight and number of publications, ideal to make tags clouds.
 - Added a command to edit a file on the blog and recompile it automatically.
 - Detection of missing variables in the blog's config file.
 - The IfInThread pattern behaves as a conditional If/Else structure.

- Since version 1.2.0
  - You can attach a specific CSS stylesheet to single entries.
  - Markdown parser is now optional.
  - Remote copy of your blog is available.
  - Add some nice themes.
  - Install via pip
  - More verbosity on errors.
  - English langage is now supported.
  - Add a reminder command 

# Installing

Since the version 1.2.0 you install VenC with [pip](https://pypi.python.org/pypi/pip) which is awesome because it's way more easier!
Careful by the way, VenC rely on python 3, so be sure to use the right pip version. On debian like system you must use pip3. 

> pip install venc --user

Don't forget to add _--user_ argument so VenC is installed in the user environment of python instead of your system, which is strongly advised.

Also you can upgrade VenC with

> pip install --upgrade venc

It might be possible  you face some _unknown command_ error while using VenC. If so check out this specific part of the [FAQ](faqEN.md)

# Uninstalling

Easy as pie, but still sad! You can uninstall VenC with

> pip uninstall venc

That's it!

# Taking your marks

1. [File Tree](#file-tree)
2. [Files structure](#files-structure)
3. [Pattern Processor](#pattern-processor)
4. [Environmen Variables](#environment-variables)

## File Tree

When you create a new project, VenC creates a certain amount of directories. The project's root takes the name of the blog, for example, "MooFooBar". This directory contains five others.

* __blog__: The folder where is exported the blog.
* __extra__: A folder containing whatever ressources copied to __blog/__ when exportating.
* __entries__: Contains every publication in the form of numbered and dated text files.
* __theme__: Contains html templates, stylesheets and optionally JS scripts.
* __templates__: Contains blank publication models.


## Files structure

1. [Main config file](#main-config-file)
2. [Templates](#templates)
3. [Publications](#publications)
4. [Themes](#themes)

### Main config file

__blog_configuration.yaml__

It is a Yaml document in the project's root which defines blog's properties, such as it's title, it's author name, or functionnal details such as the number of by page publications or the printing order of those. Immediately after creating your blog, it will probably be the first file you'll edit. After fulfilling those fields (detailed below), you normally won't have to touch it again.


* __blog_name__ : Obviously your blog's name.
* __textEditor__ : Chosen text editor to edit your publications.
* __date_format__ : "%A %d. %B %Y" by default. Defines the date format used within the blog. The date format is in fact the one used by Python. Learn more on this format [here](http://strftime.org)
* __author_name__: Name of the administrator or author of the blog.
* __ftp_host__ : Your ftp hostname
* __blog_description__ : A quick summary of what your site's about.
* __blog_keywords__ : Keywords associated to the website.
* __author_description__ : A short text about the author.
* __license__ : Your content's license.
* __blog_url__ : Blog's URL. Can be left blank depending on the theme used.
* __blog_language__ : Blog's language.
* __author_email__ : Your e-mail address.
* __entries_per_pages__ : "10" by default. Obviously defines the per page publications number.
* __columns__ : "1" by default. This field defines the number of columns in a page.
* __rss_thread_lenght__ : "5" by default. Defines the number of publications to print in the RSS feed.
* __thread_order__ : "latest first" by default. Defines the order of publications. Oldest to newest, or the other way around. This field can be set to "oldest first", or "latest first".
* __path__ : A variable containing various paths, you normally shouldn't need to touch it. Those paths list is detailed below.
 * __index_file_name__ : "index{page_number}.html" by default. Main thread of publications' fomratted filename. Should always contain the variable {page_number}.
 * __category_directory_name__ : "{category}" by default. Defines the directory where will be exported a publication thread specific to a category of publication. This field should always contain the variable {category}.
 * __dates_directory_name__ : "%Y-%m" by default. Defines the date format used for directories' names of publications threads associated to dates. The date format is in fact the one used by Python. Learn more on this format [here](http://strftime.org)
 * __entry_file_name__ : "entry{entry_id}.html" by default. Defines the filename of a unique publication. This field should always contain the variable {entry_id}.
 * __rss_file_name__ : "feed.xml" by default. Defines the rss feed's filename.
 * __ftp__ : The absolute path for your destination directory on your ftp server

### Templates

A template actually is a blank publication which has been preformatted to contain information informations often used for which we don't want to lose time to rewrite or to shape. So a template file contains [patterns](#templates-patterns)
which can be called. There is no template by default, it up to the user to create theirs. When no template is used VenC creates a fully blank publication.

### Publications

A publication is a file similar to a template but which the purpose is to be filled by the user manually by redacting the desired content.
It can be a mood note, a documented article, an image galery, etc. To ease the edition of your blog with VenC you are strongly encouraged to use
templates.

A publication contains a firts part in [Yaml](http://yaml.org) format contening publication's metadatas, An another one in [Markdown](https://daringfireball.net/projects/markdown/) format which will contain the said publication.

Finaly a blank publication looks like this:

  authors: ''
  categories: ''
  entry_name: name of the entry
  tags: ''

So we have five fields to complete, or not.

- __authors__ : It's the list of the publication's authors, separated by a coma. For example _Denis Salem, Aaron Swartz, Richard Stallman_.
- __categories__ : The list of the publication's categories, separated by a coma. You can also have sub-categories for a publication which will then define a categories tree. To define a sub-category one has to separate the parent category from the sub-category by ' > '. This can be repeated as many times as necessary. For example _Metal > Copper, Metal > Steel > Properties, Materials_.
- __entry_name__ : It's your publication's name as you defined it when creating the publication using `venc -ne <title of the publication>`.
- __tags__ : The list of the publication's keywords, separated by a coma. For example _Libre, Open-source, Linux_.
- __doNotUseMarkDown__ : Optionnal, since version *1.2.0*. Tell to VenC if content of the current entry must be parsed as [Markdown](https://daringfireball.net/projects/markdown/) or not. This field does not need any particular value. By default VenC use [Markdown](https://daringfireball.net/projects/markdown/).

Both parts are separated by three dashes (the ones of the six). On the screenshot, the part containing the Markdown syntax is blank. So we are really talking about a blank publication.

Also, let's note that a publication's file name is formatted in a particular way.

`<id>__<month>-<day>-<year>-<hour>-<minute>__<title>`

To create a new publication it's [here](#new-publication)

### Themes

A theme is the assembly of all fragments which will be joined together and interpreted by VenC to form your blog, it's in a theme that will be defined your website's page layout.
Typically, a theme is a directory containing at leat one folder, the __chunks__ folder and another, optional __assets__.

- __assets__ : Contains the necessary ressources for the page layout or the blog's operation. This can be images, CSS style sheets or JS scripts. You can also put there librairies like JQuery or bootstrap.

- __chunks__ : Must contain the following files
  - header.html
  - entry.html
  - footer.html
  - rssHeader.html
  - rssEntry.html
  - rssFooter.html

As you may have understood, VenC puts together the pieces of your blog by formatting the header (header.html) and by repeating a certain amount of times the operation which consists on formatting the piece which defines a publication (entry.html) for the current publication. The the current page is finished by adding the footer piece (footer.html) also formatted.

It's exactly the same principle for the RSS feed which is constructed identically.

It is not necessarily easy to create a theme from scratch and may want to avoid loosing too much time testing the fuctioning of all this. The best way to create a theme by yourself is to take a look at the [dummy](../src/share/themes/dummy) theme. This theme, as is, is not usable, but it is a solid base to create yours. The CSS style is to define, and you may want to reorganize the elements in the page. If you have already installed VenC on your system you will find that theme in 

	~/.local/share/VenC/themes/dummy

Another approach is to look at how are constructed other themes. These ones will be added gradually on the github repository of VenC.

You can also help yourself with the [Tutorial](howtoEN.md) part in which are described various techniques to realise really specific page layouts and for which the usage may be a little bit obscure of VenC's patterns will be illustrated.

## Pattern Processor

1. [Template Patterns](#template-patterns)
2. [Super Global Patterns](#super-global-patterns)
3. [Publications Patterns](#publications-patterns)
4. [Special Patterns](#special-patterns)

VenC uses a pattern recognition engine allowing an easy and automated page layout setup. This system should allow in futur versions to use external modules. Plugin's creation and usage will be detailed in another part.

_Patterns which can be recognised are depending on the context in which they are found._

Patterns are defined like so in VenC

* Every pattern begins with '.:'
* Every pattern ends with ':.'
* The separator(s) within a pattern are represented with '::'

A pattern is a function which can take parametres. The objective is to replace a pattern by a formatted character string. Typically, patterns allow accessing to the blog's data or editing the page layout to do, say, a drop-down menu, or a navigation bar.

### Templates patterns

For more info on templates, it's [here](#templates)
A template can contain a few patterns that VenC can interprete.

* __.:Get::EntryID:.__ : Returns the unique publication's ID.
* __.:Get::EntryName:.__ : Returns the publication's name.
* __.:Get::EntryMonth:.__ : Returns the month of the publication's creation.
* __.:Get::EntryYear:.__ : Returns the year of the publication's creation.
* __.:Get::EntryDay:.__ : Returns the day of the publication's creation.
* __.:Get::EntryHour:.__ : Returns the hour of the publication's creation.
* __.:Get::EntryMinute:.__ : Returns the minute of the publication's creation.

To those patterns, add the super globals which are generally available in any context.

### Super Global Patterns

Those patterns are generally available in any context and are defined in [blog_configuration.yaml](#main-config-file).

* __.:Get::AuthorName:.__ : Returns the blog's author's name.
* __.:Get::BlogName:.__ : Returns the blog's title.
* __.:Get::BlogDescription:.__ : Returns the blog's description.
* __.:Get::BlogKeywords:.__ : Returns the blog's keywords.
* __.:Get::AuthorDescription:.__ : Returns the blog's author's description.
* __.:Get::License:.__ : Returns the blog's content's license.
* __.:Get::BlogUrl:.__ : Returns the blog's URL.
* __.:Get::BlogLanguage:.__ : Returns the blog's language.
* __.:Get::AuthorEmail:.__ : Returns the blog's author's email.
* __.:Get::RelativeOrigin:.__ : Returns the blog's root's relative path.
* __.:Get::RelativeLocation:.__ : Returns the current directory relatively to the blog's root.

You can also define your own variables by adding extra fields in [blog_configuration.yaml](#main-config-file). For exemple

	Banner: 'myBanner.jpg'

You can then get the value of _Banner_ with

	.:Get::Banner:.

### Publications Patterns

A publication can contain the same patterns as the ones of a template. Also, add:

* __.:Get::EntryUrl:.__ : Returns the publication's permalinks.
* __.:Get::EntryContent:.__ : Returns the publication's body.
* __.:Get::EntryDate:.__ : Returns the formatted publication's date.
* __.:Get::EntryDateUrl:.__ : Returns the publication's date period's path.

### Special Patterns

It is possible in some cases to access some data iteratively, when these ones are as a list or as a tree

* __.:For:: liste :: bla bla {0[item]} bla :: separator :.__ : Allows iterating through a list. 
* __.:RecursiveFor:: arbre :: opening :: bla {0[item]} bla bla :: separator :: closing :.__ : Allows iterating through a tree, a particular type of list.

Note that in general the second parameter for the _For_ function actually is free text, to access the current iteration's item we use the context variable {0[item]}.
Ditto for the last parameter, the separator. The separator allows inserting some text after the current's iteration's free text.

Similarily, for the _RecursiveFor_ function, The second, the fourth and fifth parameter are free text.

* __.:GetPreviousPage:: free text :.__ : Allow to get the previous page. Some variables are availables in _free text_ field:
  - __{0[destinationPage]}__ : Hold the number of the previous page. 
  - __{0[destinationPageUrl]}__ : Hold the url of the previous page.
  - __{0[entryName]}__ : In an entry page only, refer to the previous entry name. 
* __.:GetNextPage:: free text :.__ : Allow to get the next page. Some variables are availables in _free text_ field:
  - __{0[destinationPage]}__ : Hold the number of the next page. 
  - __{0[destinationPageUrl]}__ : Hold the url of the next page.
  - __{0[entryName]}__ : In an entry page only, refer to the next entry name. 
* __.:PagesList:: length :: free text :.__ : Allows getting a list of previous and next publications. The list's length is determined by __length__, which must be an integer. There is two contextual variable there: {0[pageUrl]} and {0[pageNumber]}. The first one give you the url of the destination page, and the last one give you it's number.
* __.:IfInThread:: free text if True :: free text if False:.__ : Conditionnal pattern which allows printing the free or not text whether we are in a publication's thread or in a publication. This allows for example to have a particular page layout for a unique publication or for a publication's thread including the corresponding style sheets.
* __.:CodeHighlight::language::True | False:: source code :.__ : Very handy syntax coloration feature based on the [pygments](http://pygments.org/) library  allowing you to publish and to shape some source code. This pattern, when detected, produces CSS style sheets in the extra directory of your blog, do not forget to include them in header.html.
  - The first parameter in the pattern is the language that we want to color.
  - The second parameter in the pattern indicates if we have to number the source code's lines. This parameter can either be True or False.
  - The last parameter is free text corresponding to your source code.

## Environment Variables

1. [blog_configuration.yaml](#blog_configurationyaml)
2. [Pattern variables](#pattern-variables)

### blog_configuration.yaml

Like in other VenC contexts. The blog's configuration file uses environment variables, the usage is detailed right below.

* __{page_number}__ : Defines the current page's number.
* __{category}__ : Defines the current publicating category.
* __{entry_id}__ : Defines the current publication's ID.

### Pattern variables

There also exist particular variables as lists. Those variables can be browsed iteratively and recursively to extract the content and to shape it. This extraction is done using special patterns _For_ and _RecursiveFor_. You can find out more on their functioning in the [Special Patterns](#spécial-patterns) part. But before, here are the available lists:

* __EntryTags__ : The current publication's keywords list. To access the current iteration's keyword use the contextual variable __{0[tag]}__.
* __EntryAuthors__ : the list of the current publication's authors. To access the current item use the contextual variable __{0[author]}__.
* __BlogDates__ : The list of the links to the publications grouped by date as defined in [blog_configuration.yaml](#main-config-file). There are several available items for a current iteration: __{0[date]}__, __{0[dateUrl]}__. Respectively the period as formatted [blog_configuration.yaml](#main-config-file) and the path to the directory associated to this period.
  - __{0[date]}__ : Time period as formatted in [blog_configuration.yaml](#main-config-file).
  -  __{0[dateUrl]}__ : The path to the directory associated with this time period.
  -  __{0[count]}__ : The number of publications in the archive.
  -  __{0[weight]}__ : the weight of publications contained in the current archive as an integer between 0 and 10

We now arrive in the particular case of categories. Categories form a tree as illustrated right below

- Materials
  - Metal
    - Steel
    - Gold
    - Platinum
  - Plastics
    - PLA
    - ABS
    - PP
- Art
  - Movie
  - Music

Down below, we call "_leave_" the end of a branch, a so called "_complete branch_" is the complete path from the root of a tree to a leave of that tree.

* __EntryCategories__ : The category list (complete branch) of the current publication. Is found as nested lists. There are several available items for a current iteration: 
  * __{0[relativeOrigin]}__ : The current's page relative path to the blog's root.
  * __{0[categoryPath]}__ : The current sub-category's relative path.
  * __{0[item]}__ : The current sub-category's name.
* __EntryCategoriesLeaves__ : The list of the current publication's categories (leaves). There are several available items for a current iteration: 
  * __{0[relativeOrigin]}__ : The current's page relative path to the blog's root.
  * __{0[categoryLeaf]}__ : The leaf category's name.
  * __{0[categoryLeafUrl]}__ : The URL towards the leaf's category.
* __BlogCategoriesLeafs__ : The list of your blog's categories (leaves). There are several available items for a current iteration:
  * __{0[relativeOrigin]}__ : The current's page relative path to the blog's root.
  * __{0[categoryLeaf]}__ : The leaf category's name.
  * __{0[weight]}__ : The weight of publications contained in the current category as an integer between 0 and 10.
  * __{0[count]}__ : The number of publications contained in the category.
  * __{0[categoryLeafUrl]}__: The URL towards the leaf's category.
* __BlogCategories__ : The list of the blog's categories (complete branches). Comes as nested lists. There are several available items for a current iteration:
  * __{0[relativeOrigin]}__ The current page's relative path to the blog's root.
  * __{0[categoryPath]}__ The current sub-category's relative path.
  * __{0[item]}__  The sub-category's name.

To use these patterns' special variables, go to the [Special Patterns](#special-patterns) part.

# Commands

1. [Print VenC's version](#print-vencs-version)
2. [New Blog](#new-blog)
3. [New publication](#new-publication)
4. [Exporting the blog](#exporting-the-blog)
5. [Exporting the blog online](#exporting-the-blog-online)
6. [Remote copy](#remote-copy)
7. [Edit a file from blog and recompile automatically](#edit-a-file-from-blog-and-recompile-automatically)
8. [Display reminder](#display-reminder)
9. [Installer theme](#install-theme)

## Print VenC's version

`$ venc -v`

or

`$ venc --version`

## New Blog

`$ venc -nb <name of the blog>`

or

`$ venc --new-blog <name of the blog>`

VenC creates the directory containing the blog's sources in the place where you type in the command.

`$ venc -nb "mySuperBlog"`

`$ cd mySuperBlog`

`$ ls`

`blog  blog_configuration.yaml  entries  extra  templates  theme`

You cannot create a blog without giving it a name. Once you have created your blog, the first thing to do in general is to edit the file __blog_configuration.yaml__. For more info on this config file, it is [here](EN.md#main-config-file).

## New publication

`$ venc -ne "<nom de la publication>" [nom du template]`

or

`$ venc --new-entry "<name of the publication>" [name of the template]`

To create a new publication, you __must__ be within the directory of your blog.

You cannot create a publication whithout giving it a title.

If you do not specify a template's name, VenC will make a publication totally blank. The template's name is in fact the filename of the desired template found in the __templates__ directory.

After this command VenC will try to open the new publication with the text editor specified in the main config file __blog_configuration.yaml__.

## Display available themes


	$ venc -t

ou

	$ venc --themes

Display available themes ship with VenC. Theses themes should be localted in 

> ~/.local/share/VenC/themes

## Exporting the blog

`$ venc -xb [theme]`

or

`$ venc --export-blog [theme]`

To export your blog you __must__ be in your blog's directory.

There, is located a directory soberly titled blog. It is in this directory that your website will be exported. Once the exportation finished you can copy this directory's content on your server.

For more info on the file tree, it is [here](#file-tree).

You can specify a theme to use while compile your blog. If none theme is given VenC will compile with your locale theme in the site folder.

## Remote copy

	$ venc -rc

or

	$ venc --remote-copy

This command allow you to copy in a remote location, via FTP, the content of the *blog* directory. By running this command an authentification prompt will bi issued.

To copy the blog into remote location you __must__ be in your blog directory.

## Exporting the blog online

`$ venc -xftp [theme]`

or

`$ venc --export-via-ftp [theme]`

To export your blog you __must__ be in your blog's directory.

There, is located a directory soberly titled blog. It is in this directory that your website will be exported. Once the exportation finished the directory will be copied to your server. At this moment an authentication invite will appear in the terminal.

Like for regular blog exportation, you can specify a theme.

## Edit a file from blog and recompile automatically

`$ venc -ex <file>`

or

`$ venc --edit-and-export <file>`

This command opens a folder passed as a parameter with your favorite text editor, defined in [blog_configuration.yaml](#main-config-file) then, once the edition completed, recompiles the whole blog.

## Display reminder

	$ venc -h

or

	$ venc --help

So you forget how to do something? This command display in the terminal the usual features you are looking for!

## Install theme

	$ venc -it <theme name>

or

	$ venc --install-theme <theme name>

This command move the current theme to a time-stamped folder in the root directory of your blog. The used theme, given in parameter, is then installed.

# Themes

1. [Installating](#installating-1)
2. [Plugins](#plugins)

## Installing

To install a theme on your blog, copy the directory __chunks__ and __assets__ (if this one exists) in the sub-directory __theme__ of your blog.
Default themes are located in

	~/.local/share/VenC/themes

A more convenient way to install theme is to use [the proper command for this purpose](#install-theme).

## Plugins

1. [Infinite Scrolling](#infinite-scrolling)
2. [Clientside Search Engine](#clientside-search-engine)

### Infinite Scrolling

It is an AJAX script which will automatically load the next pages' contents in the current page. This module is ideal for image galleries, for example. TO install this module, one just has to copy it

	VenC-Infinite-Scroll-<version>.js

from

	/usr/share/VenC/themes/dummy/assets

in 

	<blog>/themes/assets

Then add in __header.html__ 
    
	<script type="text/javascript" src=".:Get::RelativeOrigin:.VenC-Infinite-Scroll-<version>.js"></script>

Voilà, now the magic happens. But be careful. Check that the following are respected in your theme.

- The element containing your publication must have the class name "entry" or else the module won't be able to detect and get the publications of your blog.
- You can have a loading image anywhere in your page, but if you want to make it interact with the module it must have as ID name "__VENC_LOADING__".
- You can simply want to delete an element containing navigation links, for that the element will have to have as ID name "__VENC_NAVIGATION__".

### Clientside search engine

Not implemented yet
