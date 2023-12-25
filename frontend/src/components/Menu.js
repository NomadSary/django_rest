import React from 'react'


const MenuList = () => {
return(
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">        
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="news.html">Все пользователи</a>
                </li>
                <li class="nav-item ">
                    <a class="nav-link" href="courses_list.html">Листы</a>
                </li>
                
                <li class="nav-item ">
                    <a class="nav-link" href="contacts.html">TO-DO</a>
                </li>
            </ul>
            <span><a href="#">🇷🇺</a> <i class="fas fa-grip-lines-vertical"></i> <a href="#">🇬🇧</a></span>
        </div>
    </div>
</nav>
)}

export default MenuList