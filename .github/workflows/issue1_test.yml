# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: issue1_test

on:
  push:
    branches:
      - feature1_new_title
  pull_request:
    types: [ opened ]

jobs:
  build:
    runs-on: ubuntu-latest
    if: github.head_ref == 'feature1_new_title' || github.ref == 'refs/heads/feature1_new_title'
    strategy:
      matrix:
        python-version: [ '3.x' ]
    name: Python ${{ matrix.python-version }} sample
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v1
        with:
          python-version: '3.x' # Version range or exact version of a Python version to use, using SemVer's version range syntax
          architecture: 'x64' # optional x64 or x86. Defaults to x64 if not specified
      - uses: actions/setup-node@v1
        with:
          node-version: '10.x'

      - run: python tests/Aufgabe1_test.py > test-output.txt
      - run: echo ::set-output name=result::$(grep "Yes" test-output.txt | wc -l)
        id: test
        shell: bash

      - run: echo ::set-output name=comment::$(< ./fail.md)
        id: fail
        shell: bash
        working-directory: ./.github/COMMENT_TEMPLATES

      - run: cat ./.github/COMMENT_TEMPLATES/success.md > comment.txt
        shell: bash
      - run: node ./.github/misc/answers.js 1 >> comment.txt
        if: steps.test.outputs.result == '1'
      - run: echo ::set-output name=comment::$(< comment.txt)
        id: success
        shell: bash

      - name: PR Comment Fail
        uses: Janealter/branch-pr-comment@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          message:  ${{ steps.fail.outputs.comment }}
          branch: feature1_new_title
        if: steps.test.outputs.result != '1'
      - name: PR Comment Success
        uses: Janealter/branch-pr-comment@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          message:  ${{ steps.success.outputs.comment }}
          branch: feature1_new_title
        if: steps.test.outputs.result == '1'

      - run: exit 1
        if: steps.test.outputs.result != '1'
