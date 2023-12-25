import React from 'react'

const AuthorItem = ({ author }) => {
    return (
        <tr>
            <td>
                {author.username}
            </td>
            <td>
                {author.first_name}
            </td>
            <td>
                {author.last_name}
            </td>
            <td>
                {author.email}
            </td>
        </tr>
    )
}
const AuthorList = ({ authors }) => {
    return (
    <div class="container-lg mt-auto">  
        <table>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    </div>    
    )
}

export default AuthorList