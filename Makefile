# Makefile for javascript resources
PATH_BASE=$(PWD)
PATH := $(PWD)/node_modules/.bin:$(PWD)/bin:$(PATH)
B=node_modules/.bin/

all: buildout resources

$(B)/buildout:
	python bootstrap.py

bin/npm: bin/buildout
	bin/buildout -c buildout-dev.cfg install nodejs

npm_install: bin/npm
	npm install -d
$(B)/bower: npm_install
$(B)/gulp: npm_install

resources: $(B)/bower $(B)/gulp  bin/npm
	npm install
	bower install
	gulp

watch: resources
	gulp watch
