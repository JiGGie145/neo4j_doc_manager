from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)


import logging
import os
import sys

logging.basicConfig(stream=sys.stdout)

doc_id = "1234a234b2342c3e"
simple_doc = {'_id': "123a456b", 'session': {'title': 'simpel title'}}
doc_test = {'_id': doc_id, 'session': {'title': '12 Years of Spring: An Open Source Journey', 'abstract': 'Spring emerged as a core open source project in early 2003 and evolved to a broad portfolio of open source projects up until 2015. This keynote reflects upon the journey so far, with a focus on the open source ecosystem that Spring lives within, including stories and anecdotes from the old days as well as from recent times. Not getting stuck in history, we’ll also look at the continuity of Spring’s philosophy and its immediate applicability to Java development challenges in 2015 and beyond.'}, 'room': 'Auditorium', 'topics': ['keynote', 'spring'], 'speaker': {'twitter': 'https://twitter.com/springjuergen', 'name': 'Juergen Hoeller', 'picture': 'http://www.springio.net/wp-content/uploads/2014/11/juergen_hoeller-220x220.jpeg', 'bio': 'Juergen Hoeller is co-founder of the Spring Framework open source project and has been serving as the project lead and release manager for the core framework since 2003. Juergen is an experienced software architect and consultant with outstanding expertise in code organization, transaction management and enterprise messaging.'}, 'timeslot': 'Wed 29th, 09:30-10:30'}
doc_array_test = {'_id': doc_id, 'session': {'title': '12 Years of Spring: An Open Source Journey', 'abstract': 'Spring emerged as a core open source project in early 2003 and evolved to a broad portfolio of open source projects up until 2015. This keynote reflects upon the journey so far, with a focus on the open source ecosystem that Spring lives within, including stories and anecdotes from the old days as well as from recent times. Not getting stuck in history, we’ll also look at the continuity of Spring’s philosophy and its immediate applicability to Java development challenges in 2015 and beyond.'}, 'room': 'Auditorium', 'topics': ['keynote', 'spring'], "tracks": [{ "main":"Java" }, { "second":"Languages" }], 'speaker': {'twitter': 'https://twitter.com/springjuergen', 'name': 'Juergen Hoeller', 'picture': 'http://www.springio.net/wp-content/uploads/2014/11/juergen_hoeller-220x220.jpeg', 'bio': 'Juergen Hoeller is co-founder of the Spring Framework open source project and has been serving as the project lead and release manager for the core framework since 2003. Juergen is an experienced software architect and consultant with outstanding expertise in code organization, transaction management and enterprise messaging.'}, 'timeslot': 'Wed 29th, 09:30-10:30'}


if sys.version_info[0] == 3:
  unicode = str

if sys.version_info[:2] == (2, 6):
  import unittest2 as unittest
  from unittest2.case import SkipTest
else:
  import unittest
  from unittest.case import SkipTest