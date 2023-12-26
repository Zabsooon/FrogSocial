from conan import ConanFile
from conan.tools.cmake import cmake_layout

class FrogSocialRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("oatpp/1.3.0")

    def build_requirements(self):
        self.tool_requires("cmake/[>3.11]")

    def layout(self):
        cmake_layout(self)
