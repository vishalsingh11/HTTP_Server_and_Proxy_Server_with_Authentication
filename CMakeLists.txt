cmake_minimum_required(VERSION 3.4)

project(MySimpleProxyAndServer)
find_package(CURL REQUIRED)

add_executable(${PROJECT_NAME} main.cpp)

target_link_libraries(MySimpleProxyAndServer curl)