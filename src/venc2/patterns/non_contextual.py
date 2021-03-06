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

import hashlib
import json
import os
import requests
from venc2 import venc_version
from venc2.l10n import messages
from venc2.patterns.exceptions import PatternInvalidArgument
from venc2.patterns.exceptions import PatternMissingArguments
from venc2.helpers import GenericMessage
from venc2.prompt import notify
from urllib.parse import urlparse

def try_oembed(providers, url):
    try:
        key = [ key for key in providers["oembed"].keys() if url.netloc in key][0]

    except IndexError:
        raise PatternInvalidArgument("url", url.geturl(), messages.unknown_provider.format(url.netloc))
    
    try:
        r = requests.get(providers["oembed"][key][0], params={
            "url": url.geturl(),
            "format":"json"
        })

    except requests.exceptions.ConnectionError as e:
        raise GenericMessage(messages.connectivity_issue+'\n'+str(e))

    if r.status_code != 200:
        raise GenericMessage(messages.ressource_unavailable.format(url.geturl()))

    try:
        html = json.loads(r.text)["html"]
        
    except Exception as e:
        raise GenericMessage(messages.response_is_not_json.format(url.geturl()))
        
    try:
        cache_filename = hashlib.md5(url.geturl().encode('utf-8')).hexdigest()
        os.makedirs("caches/embed", exist_ok=True)
        f = open("caches/embed/"+cache_filename, "w")
        f.write(html)
        f.close()

    except PermissionError:
        notify(messages.wrong_permissions.format("caches/embed/"+cache_filename), color="YELLOW")

    return html

def get_embed_content(providers, argv):
    try:
        url = urlparse(argv[0])

    except IndexError:
        raise PatternMissingArguments()
        
    return try_oembed(providers, url)

def get_venc_version(argv):
    return venc_version

""" Need to handle missing args in case of unknown number of args """
def set_color(argv):
    return "<span style=\"color: "+('::'.join(argv[1:]))+";\">"+argv[0]+"</span>"

def set_style(argv):
    ID = argv[0].strip()
    CLASS = argv[1].strip()
    ID = "id=\""+ID+"\"" if ID != '' else ''
    CLASS = "class=\""+CLASS+"\"" if CLASS != '' else ''
    return "<span "+ID+' '+CLASS+">"+('::'.join(argv[2:]))+"</span>"

def include_file(argv):
    try:
        filename = argv[0]
        include_string = open("includes/"+filename, 'r').read()
        return include_string

    except IndexError:
        raise PatternMissingArguments()

    except PermissionError:
        raise PatternInvalidArgument("path", filename, messages.wrong_permissions.format(argv[0]))
    
    except FileNotFoundError:
        raise PatternInvalidArgument("path", filename, messages.file_not_found.format(filename))

def table(argv):
    output = "<table class=\"__VENC_TABLE__\">"
    tr = [[]]
    append_td = tr[-1].append
    append_tr = tr.append
    for cell in argv:
        if cell == 'NewRow':
            append_tr([])
            append_td = tr[-1].append

        else:
            append_td("<td>"+cell+"</td>")
    
    join = ''.join
    for row in tr:
        output += "<tr>"+join(row)+"</tr>"
        
    return output + "</table>"
