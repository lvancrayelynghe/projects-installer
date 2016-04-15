# Ansible Projects Installer

## Usage

### 1. Create a group configuration file

The file must be named `_group_variables.yml`. It inherit from `_global_variables.yml`, so just update the needed vars.

Save the file in the `projects` directory or in a subdirectory (to create "groups" of projects)


### 2. Create a project configuration file

Create a file named `project-name.yml` in a group's directory. It inherit from the previous `_group_variables.yml`, again, update only the needed variables.

The filename is used as project name.


### 3. Run the playbook

Run `./run.sh projects/group` for a full group or `./run.sh projects/group/project.yml` for a single project
