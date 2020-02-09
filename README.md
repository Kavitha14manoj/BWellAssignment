# BWellAssignment
Pre-requisites:

1.Install Java
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

2. Install Python
https://www.python.org/downloads/

3. Install Selenium
https://selenium-python.readthedocs.io/installation.html
On terminal "pip install selenium"

4. Install geckodriver
https://github.com/mozilla/geckodriver/releases
and save it in to your workspace.

5.Install Eclipse 
https://www.eclipse.org/downloads/download.php?file=/oomph/epp/neon/R2a/eclipse-inst-mac64.tar.gz
Eclipse – Python Setup
5.1.  Launch the Eclipse
5.2.  Select default workspace
5.3.  Set The python plug in for Eclipse.
5.4.  Select Help – Install New Software 
5.5.  On text window “Work with”
      type pydev-  http://www.pydev.org/updates
      and click “Add”
      Select “PyDev” and click Next and finish
5.6  Restart Eclipse after installation.
      Eclipse- File -New- Project – select - PyDev Project
      Type any Project name
      Select python and click on “Please configure an interpreter before proceeding
      Select – Interpreter - Python, Next and Finish
6. To run the python script,rightclick on script and select run as python run.

Test Framework:
Test Framework is designed using Page Object Model. Its designed as

PageObjects -
            -homePage.py
            -loginPage.py
            
TestSuite -
          - searchServie.py
          - signIn.py
          -sortServiceNameinAscOrder.py
Utility -
         -loginCredentials.py
         -loginUtility.py
         
         
homePage and loginPage contains element locators for home and sign in page. Which is called in tests.
login Credentials contains account name , email and passwords.Which is called in tests.
loginUtility contains sign in method, which is called and reused in tests.


         


      

     



