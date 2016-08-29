#!/bin/bash
source /etc/gate_control/envvars

while true; do
    timeout 5 avconv -re -rtsp_transport tcp -i rtsp://${USERNAME}:${PASSWORD}@${CAM_URL} -f image2 -vframes 1 -pix_fmt yuvj420p gate-new.jpg 2>&1 > /dev/null
    if [ -e gate-new.jpg ]
    then
        mv gate-new.jpg gate.jpg
    fi
done

