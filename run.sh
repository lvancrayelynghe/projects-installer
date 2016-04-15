#!/bin/bash

PROJECTS=$1
COMMAND="ansible-playbook playbook.yml -e"

cd "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

###################
# Install Ansible #
if [ ! hash ansible >/dev/null 2>&1 ]; then
    echo "You need to install Ansible first..." >&2
    exit 1
fi

###############
# Run Ansible #
if [ ! "${PROJECTS}" ]; then
    PROJECTS="projects"
fi

if [ -d "${PROJECTS}" ]; then
    FILES=($(cd ${PROJECTS} && ls -1 *.yml 2>/dev/null | grep -v "_projects_variables.yml"))
    if (( ${#FILES[@]} == 0 )); then
        echo "No file in directory \"${PROJECTS}\"" >&2
        exit 1
    fi

    for FILE in ${FILES[@]}; do
        if [ -f "${PROJECTS}/${FILE}" ]; then
            ${COMMAND} "projects_path=${PROJECTS} project=${FILE%.*}"
        fi
    done

    exit 0
fi

if [ -f "${PROJECTS}" ]; then
    ${COMMAND} "projects_path=$(dirname "${PROJECTS}") project=$(basename ${PROJECTS} .${PROJECTS##*.})"
else
    echo "No file \"${PROJECTS}\" found" >&2
    exit 1
fi
