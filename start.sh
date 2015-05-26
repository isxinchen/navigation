#!/bin/bash                                                                                        
DESTDIR=.  
HOST='127.0.0.1'  
PORT='9002'
ROOT='.'
PROCESSNAME='navigation.py'  
sudo killall -9 $PROCESSNAME  
echo "=====killed====="  
RESTART="sudo spawn-fcgi -d $ROOT -a $HOST -p $PORT -f $DESTDIR/$PROCESSNAME -F 1"  
echo $RESTART  
$RESTART  
echo "======done======"  
ps -ef | grep $PROCESSNAME


