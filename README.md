# FrogSocial

# Build:
For now this project is developed on Fedora linux-distro, so here is the guide for building:

# Fedora:
## 1. Install Dependencies:
```
sudo dnf install cmake gcc-c++ boost-devel
```
## 2. Download Wt:
```
git clone https://github.com/emweb/wt.git
cd wt
```
## 3. Build and Install:
```
mkdir build
cd build
cmake ..
make
sudo make install
```
