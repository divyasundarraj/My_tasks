const register = document.getElementById("register");
const login = document.getElementById("login");

if(register){
    register.addEventListener("submit", function(event){
        event.preventDefault();
        const name = document.getElementById("txt1").value;
        const number = document.getElementById("txt2").value;
        const email = document.getElementById("txt3").value;
        const password = document.getElementById("txt4").value;

        const stored = JSON.parse(localStorage.getItem(email));
        if(stored){
            alert("User is Already Exsist. Please Login!!!..");
        }
        else{
            localStorage.setItem(email, JSON.stringify(name,number,password));
            alert("Registration Successful....!!!");
            window.location.href = "login_page.html";

        }
    });

    }

    if(login){
        login.addEventListener("submit",function(event){
            event.preventDefault();
            const email = document.getElementById("txt3").value;
            const password = document.getElementById("txt4").value;
            const stored = JSON.parse(localStorage.getItem(email));
            if(stored){
                alert("Login Successfully..!!!");
            }
            else{
                localStorage.setItem(email, JSON.stringify(password));
                alert("Invalid Username or Password. please Check..!!!")
            }
            window.location.href = "home_page.html";



        })
    }
    


