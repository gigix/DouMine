#!/usr/bin/env python
import os

from model.crawler import Crawler

Crawler('1148282', 100000, os.path.dirname(__file__) + "/../data").run()