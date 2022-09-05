# PHP Brew Config


## Notes

Added these lines to my .bashrc (not yet in the repo)

```bash

# PHPBrew
export PHPBREW_ROOT=/opt/phpbrew
export PHPBREW_HOME=$XDG_CONFIG_HOME/phpbrew
[[ -e ~/.config/phpbrew/bashrc ]] && source ~/.config/phpbrew/bashrc

```


## Changelog

  - **2022-09-05** Added PHP brew (had to import this PR [PHP8.1 compatibility by dmnlk · Pull Request #1264 · phpbrew/phpbrew](https://github.com/phpbrew/phpbrew/pull/1264) to make it work with PHP 8.1

