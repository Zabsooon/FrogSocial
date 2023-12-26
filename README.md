# FrogSocial

# Project Layout
The project layout is taken from the Oat++ documentation, so is the setup...
```
|- CMakeLists.txt                        // projects CMakeLists.txt
|- src/
|    |
|    |- dto/                             // Folder containing DTOs definitions
|    |    |
|    |    |- DTOs.hpp                    // DTOs are declared here
|    |     
|    |- controller/                      // Folder containing API Controllers where all endpoints are declared
|    |    |
|    |    |- MyController.hpp            // Sample - MyController is declared here
|    |     
|    |- AppComponent.hpp                 // Application Components configuration 
|    |- App.cpp                          // main() is here
|
|- test/                                 // test folder
     |
     |- app/
     |    |
     |    |- MyApiTestClient.hpp         // Api client for test API calls is declared here
     |    |- TestComponent.hpp           // Test application components configuration
     |                                   
     |- MyControllerTest.cpp             // MyController test logic is here
     |- MyControllerTest.hpp             // MyController test header
     |- Tests.cpp                        // tests main() is here
```

# Build:
For now this project is developed on Fedora linux-distro, so here is the guide for building.

# Fedora
If you don't have conan installed you can do it by using pip:
```
$ pip install conan
```
You can check what packages we use in file CMakeLists.txt and also what Conan installs in conanfile.py.

To build the project you need to execute this commands:
```
$ conan install conanfile.py --build=missing
$ cd build
```
If you want to build release version execute:
```
$ cmake .. -DCMAKE_TOOLCHAIN_FILE=./Release/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release
```
By now you should have generated Makefile, now you just need to execute:
```
$ cmake --build .
```
OR
```
$ make
```
