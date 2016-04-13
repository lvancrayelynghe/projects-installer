# Ansible Projects Installer

## Usage

### 1. Create a configuration file

See the provided template `configuration.template.yml`. Save your configuration file anywhere (in your dotfiles ?).

### 2. Run the playbook

Run `ansible-playbook playbook.yml -e "config_file=/path/to/configuration.yml"`

Or create an alias `alias projects='ansible-playbook playbook.yml -e "config_file=/path/to/configuration.yml"'`
