cmake_minimum_required(VERSION 3.16)
project(FrogSocial)

find_package(oatpp REQUIRED)

# Add your source files
add_executable(FrogSocialExec
    app/main.cpp
)

target_link_libraries(FrogSocialExec PUBLIC oatpp::oatpp)
