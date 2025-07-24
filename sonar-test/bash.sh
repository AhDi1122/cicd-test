#!/bin/bash
echo "Enter file:"
read f
cat $f # Command injection

DB_USER="root"
DB_PASS="toor" # Hardcoded password

