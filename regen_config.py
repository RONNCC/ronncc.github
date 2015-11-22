defconfig = """
#
# This file contains configuration flags to customize your site
#

# Name of your site (displayed in the header)
name: Ronnie Ghose

# Short bio or description (displayed in the header)
description: Lambda Llama

# URL of your avatar or profile pic (you could use your GitHub profile pic)
avatar: http://i.imgur.com/HW0TXQB.png
#
# Flags below are optional
#

categories: {}

# Includes an icon in the footer for each username you enter
footer-links:
  dribbble:
  email: ghoses@cmu.edu
  facebook:
  flickr:
  github: ronncc
  instagram:
  linkedin:
  pinterest:
  rss: # just type anything here for a working RSS icon, make sure you set the "url" above!
  twitter: 
  stackoverflow: # your stackoverflow profile, e.g. "users/50476/bart-kiers"
  youtube: # channel/<your_long_string> or user/<user-name>
  googleplus: # anything in your profile username that comes after plus.google.com/


# Enter your Disqus shortname (not your username) to enable commenting on posts
# You can find your shortname on the Settings page of your Disqus account
disqus: sghose

# Enter your Google Analytics web tracking code (e.g. UA-2110908-2) to activate tracking
google_analytics: UA-36442208-2

# Your website URL (e.g. http://barryclark.github.io or http://www.barryclark.co)
# Used for Sitemap.xml and your RSS feed
url:

# If you're hosting your site at a Project repository on GitHub pages
# (http://yourusername.github.io/repository-name)
# and NOT your User repository (http://yourusername.github.io)
# then add in the baseurl here, like this: "/repository-name"
baseurl: ""

#
# !! You don't need to change any of the configuration flags below !!
#

markdown: redcarpet
highlighter: pygments
permalink: /:title/

# The release of Jekyll Now that you're using
version: v1.1.0

# Set the Sass partials directory, as we're using @imports
sass:
  style: :expanded # You might prefer to minify using :compressed

# Use the following plug-ins
gems:
  - jekyll-sitemap # Create a sitemap using the official Jekyll sitemap gem

# Exclude these files from your production _site
exclude:
    - Gemfile
    - Gemfile.lock
    - LICENSE
    - README.md
    - CNAME
"""
import glob
import json
from string import capwords

get_posts = glob.glob('_posts/*.md')
categories = []
for path in get_posts:
    with open(path) as f:
        k = filter(lambda x: 'category:' in x,f.readlines())
        if len(k) == 0:
            continue
        k=k[0]
        q = k[k.find('category:') + len('category:'):]
        categories.extend(json.loads(q))
        print k
print categories
categories = map(lambda x: capwords(x.encode('ascii','ignore')), categories)
print categories
with open('_config.yml','w') as a:
    a.write(defconfig.format(categories))
