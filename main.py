#!/usr/bin/env python
# -*- coding: utf-8 -*-

import html2text

print('First test converting HTML to MD:')
print(html2text.html2text("<p><strong>Zed's</strong> dead baby, <em>Zed's</em> dead.</p>"))

