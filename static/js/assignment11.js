
function get_users(){
    fetch('https://reqres.in/api/users/?page=2').then(
        response => response.json()
    ).then(response_obj => put_users_inside_html(response_obj.data)
    ).catch(err=>console.log(err)
    )

}

function put_users_inside_html(res_data) {
    let id=document.getElementById('id').value;
    let userID=parseInt(id);
    console.log(userID);
    const curr_main = document.querySelector("main");
         let user = Object.values(res_data).find(obj=>obj.id === userID);
    const section = document.createElement('section');
            section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
               <span>${user.first_name} ${user.last_name}</span>
               <br>
               <a href="send_to:${user.email}"> Send Email</a>
        </div>    `;

            curr_main.appendChild(section);
}