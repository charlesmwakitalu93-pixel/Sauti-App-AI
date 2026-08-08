name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y openjdk-17-jdk unzip libltdl-dev zlib1g-dev

    - name: Install Buildozer and prerequisites
      run: |
        pip install --upgrade pip
        pip install --upgrade cython==0.29.36
        pip install buildozer

    - name: Build with Buildozer
      run: |
        buildozer -v android debug

    - name: Upload APK Artifact
      uses: actions/upload-artifact@v4
      with:
        name: package
        path: bin/*.apk
