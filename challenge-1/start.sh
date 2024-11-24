#!/bin/bash

set -e

FLAG=$(< flag.txt) socat tcp-listen:5555,reuseaddr,fork SYSTEM:"/app/super_service"
