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

#a little prep for the sorted function to get the y coord of the icon
def byY(icon):
    return icon.y

#findAll() on your two identical icons and make them into a list
bothIcons = list([x for x in findAll("1row.png")]) 
#then sort them
sortedIcons = sorted(bothIcons, key=byY)
iconOnTop = sortedIcons[0]  
iconOnBottom = sortedIcons[1]
click(iconOnBottom);

firex.perfromSikuliOperation("click()","image:####:2rows.png");
firex.sleep(1*500);
firex.perfromSikuliOperation("click()","image:####:2rows.png");
firex.sleep(1*500);
firex.perfromSikuliOperation("click()","image:####:Dropdown1row.png");
firex.sleep(1*500);

firex.closebrowser()