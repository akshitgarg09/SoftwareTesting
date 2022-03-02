# Assignment  2 (19103008)
Create README file using Mark-down language and upload UML diagrams (Use-case and Squence) on README page.

## 1. Sequence Diagram
### Diagram
![Sequence Diagram](https://github.com/akshitgarg09/SoftwareTesting/blob/main/Assignment%201/SequenceDiagram.png)

### Code
```
@startuml
actor User as user
participant "Login/Signup" as auth
participant "Home Page" as home
participant "Server" as server
participant "Favourites" as fav
participant "E-commerce Websites" as ecom
participant "Blog Websites" as blog
participant "Boards" as boards

user -> auth : Enter Mobile Number
auth -> server : Verify Number
server -> auth : Send otp
auth -> user : Request otp
user -> auth : Fill otp
auth -> server : Get otp

alt If Otp is valid
    server -> auth : Otp okay
else Else
    server -> auth : Invalid Otp, please retry
end

server -> ecom : Request data to fill in ecom models
ecom -> server : Return data
server -> blog : Request data to fit in NLP models
blog -> server : Return data
server -> home : Display content on screen
home -> fav : Add to favourites
fav -> server : Save in server
home -> boards : Request new boards / Add to already existing board
boards -> home : New / Already Existing
home --> boards : Feedback
boards --> server : Save in server

@enduml
```

## 2. UseCase Diagram
### Diagram
![UseCase Diagram](https://github.com/akshitgarg09/SoftwareTesting/blob/main/Assignment%201/UseCase.png)

### Code
```
@startuml
left to right direction

actor User as user
actor Server as server
actor "E-commerce Website" as ecom
actor Blogs as blog

rectangle TrendMate{
(Login) as login
(Create New Account) as register
(Verify Credentials) as verify
(Display Login Errors) as error
(Apply Filters) as filters
(View Trendy Products) as viewProducts
(View Celebrity Blogs) as viewBlogs
(Add to favourites) as addfav
(Remove from favourites) as remfav
(Provide Live Data to Server) as serve
}

login ..> verify : include
register ..> verify : include
login <.. error : extend

user -- login
user -- register
user -- filters
user -- viewProducts
user -- viewBlogs
user -- addfav
user -- remfav
server -- serve
server -- filters
server -- viewProducts
server -- viewBlogs
server -- addfav
server -- remfav
ecom -- serve
blog -- serve

@enduml
```
