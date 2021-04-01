# Will Scheib wms9gv

import urllib.request
import re

job_title_finder = re.compile('Job title: (.*)<br')
money_finder = re.compile('gross pay: \$(.*)" /')
rank_finder = re.compile('rank</td><td>(.*) of ')


def name_to_url(name):
    """
    Normalizes name inputs.
    :param name:
    :return:
    """
    name = name.lower()

    if "," in name:
        url_name = name[name.find(", ") + 2:len(name)] + " " + name[0:name.find(",")]
        url_name = url_name.replace(" ", "-")
    else:
        url_name = name.replace(" ", "-")

    return url_name


def report(name):
    """
    Finds job title, salary, and rank for a name that is entered.
    :param name: 
    :return: job title, salary, and rank
    """
    name = name_to_url(name)
    title = None
    money = 0
    rank = 0
    try:
        url = 'https://cs1110.cs.virginia.edu/files/uva2016/' + name
        stream = urllib.request.urlopen(url)
        for line in stream:
            decoded = line.decode('UTF-8').strip()
            name_match = job_title_finder.search(decoded)
            money_match = money_finder.search(decoded)
            rank_match = rank_finder.search(decoded)
            if name_match is not None:
                title = name_match.group(1)
                if "&amp;" in title:
                    title = title.replace("&amp;", "&")
                if "&lt;" in title:
                    title = title.replace("&lt;", "<")
                if "&gt;" in title:
                    title = title.replace("&gt;", ">")
            if money_match is not None:
                money = money_match.group(1)
                money = float(money.replace(",", ""))
            if rank_match is not None:
                rank = rank_match.group(1)
                rank = int(rank.replace(",", ""))
    finally:
        return title, money, rank
