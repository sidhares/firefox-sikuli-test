
set SIKULIJARPATH=C:\sikulix\sikulixapi-2.0.0.jar
set JYTHONJARPATH=C:\jython2.7.1\jython.jar
set COMMONIOJARPATH=C:\sikulix\commons-io-2.6.jar
set JNAPJARPATH=C:\sikulix\jna-platform-5.5.0.jar
set JNAJARPATH=C:\sikulix\jna.jar

java -classpath %JYTHONJARPATH%;%SIKULIJARPATH%;%COMMONIOJARPATH%;%JNAPJARPATH%;%JNAJARPATH% org.python.util.jython Rowselectiontest.py
java -cp %JYTHONJARPATH%;%SIKULIJARPATH%;%COMMONIOJARPATH%;%JNAPJARPATH%;%JNAJARPATH% org.python.util.jython Firefox-HomeContent-Highlight.py