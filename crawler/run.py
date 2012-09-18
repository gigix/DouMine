#!/usr/bin/env python
import os

from model.crawler import Crawler

Crawler('4262627', 10, os.path.dirname(__file__) + "/../data").run()
