.PHONY: all build-maya build-my_package build-my_tool clean-maya clean-my_package clean-my_tool clean build-all run

build-all: build-maya build-my_package build-my_tool

build-maya:
	cd packages/maya && rez-build --install

build-my_package:
	cd packages/my_package && rez-build --install

build-my_tool:
	cd packages/my_tool && rez-build --install

clean-maya:
	rm -rf packages/maya/build

clean-my_package:
	rm -rf packages/my_package/build

clean-my_tool:
	rm -rf packages/my_tool/build

clean: clean-maya clean-my_package clean-my_tool

run: clean build-all
	rez env my_package my_tool -- python ./scripts/main.py