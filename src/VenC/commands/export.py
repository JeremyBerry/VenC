#! /usr/bin/python3

import os
import time
import yaml
import base64
import shutil
import subprocess

import VenC.l10n
import VenC.datastore.pattern

#from VenC.blog import Blog
from VenC.datastore.datastore import DataStore
from VenC.datastore.configuration import GetBlogConfiguration
from VenC.datastore.theme import ThemesDescriptor
from VenC.helpers import Die
from VenC.helpers import RmTreeErrorHandler 
from VenC.l10n import Messages

def ExportAndRemoteCopy(argv=list()):
    Notify(Messages.blogRecompilation)
    ExportBlog(argv)
    RemoteCopy()

def ExportBlog(argv=list()):

    ''' Initialisation of environment '''

    if len(argv) == 1:
        if not argv[0] in ThemesDescriptor.keys():
            Die(Messages.themeDoesntExists.format(argv[0]))
        
        else:
            themeFolder = os.path.expanduser("~")+"/.local/share/VenC/themes/"+argv[0]+"/"
    
    datastore = DataStore()
    for param in ThemesDescriptor[argv[0]].keys():
        if param[0] != "_": # marker to detect field names we do not want to replace
            datastore.blogConfiguration[param] = ThemesDescriptor[argv[0]][param]
    
        

    # cleaning direcoty
    #shutil.rmtree("blog", ignore_errors=False, onerror=RmTreeErrorHandler)
    #os.makedirs("blog")
    #currentBlog = Blog(themeFolder, blogConfiguration)
    #currentBlog.export()

def EditAndExport(argv):
    blogConfiguration = GetBlogConfiguration()

    if len(argv) != 1:
        Die(Messages.missingParams.format("--edit-and-export"))
    
    try:
        proc = subprocess.Popen([blogConfiguration["textEditor"], argv[0]])
        while proc.poll() == None:
            pass

    except TypeError:
        Die(Messages.unknownTextEditor.format(blogConfiguration["textEditor"]))
    
    except:
        raise
    
    ExportBlog()