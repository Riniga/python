*** Settings ***
Library           SeleniumLibrary
Library           BuiltIn
Library           String

*** Variables ***
${url}  https://www.google.com
${searchfor}    nisses-gagner
${searchfieldid}    APjFqb

*** Test Cases ***
Open google.com and verify content
    Open browser    ${url}    chrome
    Maximize Browser Window
    Wait Until Element Is Visible   //*[@id="L2AGLb"]/div      10
    Click Element    xpath=//*[@id="L2AGLb"]/div
    Title Should Be    Google
    Page should contain    Google
    sleep    2
    
Search for nisses-gagner and verify that I exist
    Input Text    ${searchfieldid}    ${searchfor}
    Press Keys    ${searchfieldid}    ENTER
    sleep    2
    Page should contain    Rickard Nisses-Gagner
    Capture Page Screenshot
    Close browser
	
*** Keywords ***

Test TearDown
    Run keyword If Test Failed    Capture Page Screenshot