# Base on image_full_name (e.g., ubuntu:18.04) docker image
FROM python:3.8.12
# Switch to root
USER root
# Copy all sources files to workdir
ADD /Users/shind/IdeaProjects/IOT8112 /usr/local/source
# Change working dir
WORKDIR /usr/local/source
# Prepare project required running system environments
# requirements.txt is a document that pre-define any
# python dependencies with versions required of your code
RUN pip3 install -r requirements.txt
