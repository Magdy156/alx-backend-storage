#!/usr/bin/env python3
"""
test file
"""
import redis

html_content = __import__('web').get_page("http://slowwly.robertomurray.co.uk")

print(html_content)
