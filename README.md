# .github-workflows-build.yml
build.yml
# Пример правильной структуры:
name: Build APK
on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'
        
    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          python3-pip \
          openjdk-8-jdk \
          zip \
          unzip
          
    - name: Install Buildozer and dependencies
      run: |
        pip3 install --user buildozer
        pip3 install -r requirements.txt
        
    - name: Build APK
      run: |
        export PATH=$PATH:~/.local/bin
        buildozer -v android debug
