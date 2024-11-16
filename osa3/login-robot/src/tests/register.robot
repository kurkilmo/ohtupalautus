*** Settings ***
Resource  resource.robot
Test Setup  Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  username  pass1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  user  password123
    Input New Command And Create User  user  passtwo123
    Output Should Contain  User with username user already exists

Register With Too Short Username And Valid Password
    Input Credentials  ga  password1337
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  KEKKONEN  salasana123
    Output Should Contain  Username must only contain letters a-z
    Input New Command And Create User  .2a  slasanassad12231
    Output Should Contain  Username must only contain letters a-z

Register With Valid Username And Too Short Password
    Input Credentials  username  kissa
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  username  sinihomejuusto
    Output Should Contain  Password must contain special characters or numbers

*** Keywords ***
Input New Command And Create User
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}