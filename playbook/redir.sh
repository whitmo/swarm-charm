#!/bin/bash
socat TCP-LISTEN:2375,fork,reuseaddr UNIX:/var/run/docker.sock
