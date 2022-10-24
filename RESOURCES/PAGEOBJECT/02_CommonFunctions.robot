*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Resource  ../CONFIG/config.robot
*** Variables ***

*** Keywords ***
begin test
    Set Environment Variable  webdriver.chrome.driver  ${chromeDriverPath}
    Open Browser    ${Web_URL}  ${Browser}
    Maximize browser window
End test
    Close Browser
