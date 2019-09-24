module load spark
module load python/3.5.2

# those 3 are only necessary on lab computers ... on my laptop it's fine since I have set my bash_rc as shown below defining all these paths already:
# setenv SPARK_HOME /encs/pkg/spark-2.2.0/root
# setenv PYTHONPATH ${SPARK_HOME}/python/:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip
# setenv PYTHONPATH ${PYTHONPATH}:./answers


#===========

# NB: might not need the curly braces around variables ... depends on OS linux or OSX etc.

##### ==> on lab computer:
# before starting, optionally I can do this on orwell server, by connecting through ssh (it's better because it's exactly the test environment that will be used by graders to test my code):
# ssh n_chauss@orwell.encs.concordia.ca
# ...... then:
# run git clone repourl.git
# or run git pull in the local repo folder (if already cloned locally).
# source this file (only what's above for the lab computer, not what's below ... which is my bash_profile file for my own laptop mac osx.)
# source env.sh
# then install pytest:
# pip install --user pytest
# pip install -r requirements.txt --user
# and then:
# setenv PATH ${PATH}:${HOME}/.local/bin
# then finally run pytest from the root of the repo's local folder:
# python -m pytest tests/

#### ==> on my computer, some of these things might matter, but also, my .bash_profile file is:

#=============================================================
# added by Anaconda2 4.3.0 installer
#export PATH="/Users/nicolasg-chausseau/anaconda/bin:$PATH"

# Setting PATH for Python 3.5
# The orginal version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH
#export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_112.jdk/Contents/Home
#export JAVA_HOME=/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
#export JAVA_HOME=/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home
#export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_80.jdk/Contents/Home

#export SPARK_HOME= fill it after installing spark!
#export PATH=$SPARK_HOME/bin:$PATH


export SPARK_VERSION=`ls /usr/local/Cellar/apache-spark/ | sort | tail -1`
export SPARK_HOME="/usr/local/Cellar/apache-spark/$SPARK_VERSION/libexec"
export PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
export PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.9-src.zip:$PYTHONPATH
export PYTHONPATH=$PYTHONPATH:./answers
# NB remove this last one later, it sets the python run folder to that big data LAB1 answers folder...

#xport SPARK_HOME=/usr/local/Cellar/apache-spark/2.2.1/libexec
#xport PYTHONPATH=$SPARK_HOME/python/:$SPARK_HOME/python/lib/py4j-0.10.4-src.zip
# PYTHONPATH $PYTHONPATH:./answers

#export SPARK_HOME="$HOME/Downloads/spark-1.4.0-bin-hadoop2.4"
export IPYTHON=1
export PYSPARK_PYTHON=/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
#/usr/bin/python3
export PYSPARK_DRIVER_PYTHON=ipython3
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
#=============================================================