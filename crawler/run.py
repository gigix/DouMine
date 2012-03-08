#!/usr/bin/env python
import os

from model.crawler import Crawler

Crawler('1229923', 7, os.path.dirname(__file__) + "/../data").run()
