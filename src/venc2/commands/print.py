#! /usr/bin/env python3

#    Copyright 2016, 2018 Denis Salem
#
#    This file is part of VenC.
#
#    VenC is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    VenC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with VenC.  If not, see <http://www.gnu.org/licenses/>.

from venc2.datastore.theme import themes_descriptor
from venc2.prompt import msg_format
from venc2.l10n import messages;
from venc2 import venc_version

def print_version(argv):
    print("VenC", venc_version)

def print_help(argv=None):
    print("-v\t--version")
    print("-nb\t--new-blog <\""+messages.arg_blog_name.format("1")+"\"> [\""+messages.arg_blog_name.format("2")+"\" ... ]")
    print("-ne\t--new-entry <\""+messages.arg_entry_name+"\"> [\""+messages.arg_template_name+"\"]")
    print("-xb\t--export-blog ["+messages.theme_name+"]")
    print("-ex\t--edit-and-xport <\""+messages.arg_input_filename+"\">")
    print("-s\t--serv")
    print("-xftp\t--export-via-ftp")
    print("-rc\t--remote-copy")
    print("-h\t--help")
    print("-t\t--themes")
    print("-it\t--install-themes <"+messages.theme_name+">")

def print_themes(argv=None):
    for theme in themes_descriptor.keys():
        print ("- "+msg_format["GREEN"]+theme+msg_format["END"]+":", themes_descriptor[theme]["_themeDescription_"])
