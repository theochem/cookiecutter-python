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


# Define test source files
set(TEST_SOURCE_FILES
${CMAKE_CURRENT_SOURCE_DIR}/<TEST1.cpp>
${CMAKE_CURRENT_SOURCE_DIR}/<TEST2.cpp>
)

# The testing executable
add_executable(test_{{cookiecutter.project_name}} ${TEST_SOURCE_FILES})
set_property(TARGET test_{{cookiecutter.project_name}} PROPERTY CXX_STANDARD 11)
# Google test uses many tricks that generate warnings, which cannot be fixed easily.
set_property(TARGET test_{{cookiecutter.project_name}} PROPERTY COMPILE_FLAGS -Wno-error)

# How the testing executable has to be linked...
if(UNIX AND NOT APPLE)
  set(GCOV gcov)
endif()

target_link_libraries(test_{{cookiecutter.project_name}} {{cookiecutter.project_name}} gtest gtest_main ${GCOV} pthread)

# Install the test in libexec
install (TARGETS test_{{cookiecutter.project_name}} DESTINATION libexec/{{cookiecutter.project_slug}})

# Use our own test target because ctest hides relevant output.
add_custom_target(check
                  COMMAND test_{{cookiecutter.project_name}}
                  DEPENDS test_{{cookiecutter.project_name}}
                  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
                  COMMENT "Running tests")
