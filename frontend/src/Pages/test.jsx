import { useState, useEffect } from "react";
import getToken from '../Components/useToken.jsx';
import {useAuth} from '../Components/Auth.jsx';

const Test = () => {
    const [data, setData] = useState([]);

    const token = getToken()
    const userUseAuth = useAuth()


    useEffect(() => {
        fetch("http://127.0.0.1:5000/test", {
            'methods':'GET',
            headers: {
                'Authorization': `Bearer ${token.token}`
            }
        }).then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        ).catch(err => {
            console.log(err)
        })
    }, [])

    return ( 
        <div>
            <ul>
                <li>ID: {data.ID}</li>
                <li>Name: {data.Name}</li>
            </ul>
        </div>
    );
}
 
export default Test;