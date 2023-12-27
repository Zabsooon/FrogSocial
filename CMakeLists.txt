cmake_minimum_required(VERSION 3.16)
project(FrogSocial)

find_package(oatpp REQUIRED)

# Add your source files
add_executable(FrogSocialExec
    src/App.cpp
    src/AppComponent.hpp
    src/controller/MyController.hpp
    src/dto/DTOs.hpp
)

add_executable(FrogSocialTest
    test/Tests.cpp
    test/MyControllerTest.hpp
    test/MyControllerTest.cpp
    test/app/TestComponent.hpp
    test/app/MyApiTestClient.hpp
    src/dto/DTOs.hpp
)

target_include_directories(FrogSocialExec PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_include_directories(FrogSocialTest PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/src)

target_link_libraries(FrogSocialExec PUBLIC oatpp::oatpp)
target_link_libraries(FrogSocialTest
    PRIVATE
    oatpp::oatpp
    oatpp-test
    )
