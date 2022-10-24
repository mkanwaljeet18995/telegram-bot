*** Settings ***
Resource  ../PAGEOBJECT/01_SearchPage.robot

*** Keywords ***
Search Google page       [Arguments]    ${arg1}
    Search text     ${arg1}
    ${Link_count}     Count Links
    log to console      ${Link_count}
