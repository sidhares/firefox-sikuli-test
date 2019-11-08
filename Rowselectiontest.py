#-----------------------------------------------------------------------------
# Owner : sidhares
# Description : Demo Test for Firefox web-browser automation using SIKULI/JYTHON
# Test case: Firefox Home Content - Firefox can select which Highlights to display. #3115
# * Launch Firefox browser
# * Open Firefox options using top right button
# * Click on Home link to open home options
# * Click on Highlights button twice
# * click different buttons in loop for 2 times
# * click on VisitedPages and Bookmars 2 times in loop
#-----------------------------------------------------------------------------
from org.sikuli.script import Finder
from org.hsid.auto.sikuli.iris.firefox import test_home

firex = test_home()
firex.init_test()
firex.launchbrowser('https://github.com/')
firex.perfromSikuliOperation("click()","image:####:OptionButton.png");
firex.perfromSikuliOperation("click()","image:####:OptionImage.png");
firex.sleep(1*500);
firex.perfromSikuliOperation("click()","image:####:Home.png");
firex.sleep(1*500);

firex.perfromSikuliOperation("findClick()", "image:####:1row.png:####:2") 
firex.perfromSikuliOperation("click()", "image:####:2rows.png")

firex.perfromSikuliOperation("click()", "image:####:2rows.png") 
firex.perfromSikuliOperation("click()", "image:####:Dropdown1row.png")

firex.closebrowser()