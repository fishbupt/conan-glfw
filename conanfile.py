#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class GlfwConan(ConanFile):
    name = "glfw"
    version = "3.2.1"
    description = "Cross platform API for creating windows, contexts and surfaces, reading input, handling events, etc."
    url = ""
    homepage = "https://github.com/glfw/glfw"
    author = "fishbupt <fishbupt@gmail.com>"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    extracted_dir = "glfw-" + version
    no_copy_source = True
    generators = "cmake"

    def source(self):
        source_url = "https://github.com/glfw/glfw"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.version))

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder = self.extracted_dir)
        cmake.build()
        cmake.install()

    def package(self):
        pass

    def package_info(self):
        self.cpp_info.libs = ["glfw3"]
