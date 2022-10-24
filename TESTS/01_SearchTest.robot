*** Settings ***
Library  SeleniumLibrary
Resource  ../RESOURCES/DEFINITION/01_SearchFunction.robot
Resource  ../RESOURCES/PAGEOBJECT/02_CommonFunctions.robot

Suite Setup     begin test
Suite Teardown  end test

*** Test Cases ***
Search Test in Google Page
    Search Google page      h