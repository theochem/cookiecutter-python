# -*- coding: utf-8 -*-
# {{cookiecutter.description}} 
# Copyright (C) {% now 'local', '%Y' %} {{cookiecutter.author}} <{{cookiecutter.email}}>
#
# This file is part of {{cookiecutter.project_name}}.
#
# {{cookiecutter.project_name}} is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# {{cookiecutter.project_name}} is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
# --

# Configure a header file to pass some of the CMake settings
# to the source code.
configure_file (
  ${CMAKE_CURRENT_SOURCE_DIR}/config.h.in
  ${CMAKE_CURRENT_BINARY_DIR}/config.h
)

# Explain that the current directory has to be in the source path/
# This allows use to use include "qcgrids/foo.h", which is consistent
# with the way external programs would compile against qcgrids.
include_directories(${PROJECT_SOURCE_DIR}) 

# Define source files
set(SOURCE_FILES
  ${CMAKE_CURRENT_SOURCE_DIR}/<SOURCEFILE1.CPP>
  ${CMAKE_CURRENT_SOURCE_DIR}/<SOURCEFILE2.CPP>
)

# Define header files
set(HEADER_FILES
  ${CMAKE_CURRENT_SOURCE_DIR}/<HEADER1.h>
  ${CMAKE_CURRENT_BINARY_DIR}/<HEADER2.h>
)

# Define the shared library
add_library({{cookiecutter.project_name}} SHARED ${SOURCE_FILES})
set_property(TARGET {{cookiecutter.project_name}} PROPERTY VERSION ${PROJECT_VERSION})
set_property(TARGET {{cookiecutter.project_name}} PROPERTY SOVERSION ${PROJECT_SOVERSION})
set_property(TARGET {{cookiecutter.project_name}} PROPERTY CXX_STANDARD 11)

# Install include files
install(FILES ${HEADER_FILES} DESTINATION include/{{cookiecutter.project_slug}})

# Install library
install(TARGETS {{cookiecutter.project_name}} DESTINATION lib)

# Unit Tests with Google testing framework
add_subdirectory(tests)
