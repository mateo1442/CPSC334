#!/bin/bash
cd "$(dirname "$0")";
chromium-browser --start-maximized --start-fullscreen file://$(pwd)/Documents/cpsc334-project1/index.html;
