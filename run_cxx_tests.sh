#!/bin/sh

cd build
rm -f failing.txt; for i in `ls bin/*Test | grep -E 'bin/[^C]*[^U]*[^R]*[^L]*Test'`; do $i | grep FAILED >> failing.txt; done
