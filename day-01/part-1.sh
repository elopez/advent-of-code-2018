#!/bin/sh
(echo 0; cat in.txt) | xargs echo | bc
