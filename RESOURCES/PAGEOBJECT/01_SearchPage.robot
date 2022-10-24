*** Settings ***
Library  SeleniumLibrary
Resource  ../CONFIG/config.robot
*** Variables ***
${Search_Bar}  //input[@name='q']
${Search_button}  //input[@value='Google Search']
${Links_Count}  //a[string-length(@data-ved)>0]/h3


*** Keywords ***

Search text     [Arguments]     ${arg1}
    input text  ${Search_Bar}   ${arg1}
    Wait Until Element Is Visible    //ul/div/ul/li
    click element   //ul/div/ul/li[1]
    capture page screenshot     ${ScreenShotPath}/SearchText.png

Count Links
    ${AllLinksCount}=    Get element Count       xpath:${Links_Count}
    return from keyword     ${AllLinksCount}
