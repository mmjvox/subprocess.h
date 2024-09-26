from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import copy, get, apply_conandata_patches, export_conandata_patches, rmdir
from conan.tools.scm import Git


class subprocessRecipe(ConanFile):
    name = "subprocess.h"
    version = "1.0.0"
    package_type = "library"

    # Optional metadata
    license = "unlicense.org"
    author = "  Neil Henning (sheredom)"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/sheredom/subprocess.h"
    description = "single header process launching solution for C and C++"
    topics = ("c", "cpp", "process", "subprocess", "subprocess-run")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def export_sources(self):
        export_conandata_patches(self)

    def source(self):
        source_data = self.conan_data["sources"][self.version]
        git = Git(self)
        git.clone(url="https://github.com/sheredom/subprocess.h.git")



    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        apply_conandata_patches(self)
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "subprocess.h"
        self.cpp_info.names["cmake_find_package_multi"] = "subprocess.h"
        self.cpp_info.libs = []  # No actual libraries, it's header-only
        self.cpp_info.includedirs = ["include"]


    

    

