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
from org.hsid.auto.sikuli.iris.firefox import test_home
firex = test_home()
firex.init_test()
firex.launchbrowser('https://github.com/')
firex.perfromSikuliOperation("click()","image:####:OptionButton.png");
firex.perfromSikuliOperation("click()","image:####:OptionImage.png");
firex.sleep(2*500);
firex.perfromSikuliOperation("click()","image:####:Home.png");
firex.sleep(1*500);
firex.perfromSikuliOperation("click()","image:####:Highlights.png");
firex.sleep(1*500);
firex.perfromSikuliOperation("click()","image:####:Highlights.png");
firex.sleep(1*500);


i=0
while i<2:
    firex.perfromSikuliOperation("click()","image:####:VisitedPages.png");
    firex.sleep(1*1000);
    firex.perfromSikuliOperation("click()","image:####:Bookmarks.png");
    firex.sleep(1*1000);
    firex.perfromSikuliOperation("click()","image:####:savedpages.png");
    firex.sleep(1*1000);
    firex.perfromSikuliOperation("click()","image:####:downloads.png");
    firex.sleep(1*1000);

    i=i+1
    
firex.closebrowser()